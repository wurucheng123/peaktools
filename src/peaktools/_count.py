import pysam

from ._error import ParsingError

def query_region_count(
    bam_obj: pysam.AlignmentFile,
    query_region_list: list,
    norm_method: str="CPM",
) -> list:
    """Calculate the normalized read count for given query regions.

    Args:
        bam_obj (pysam.AlignmentFile): _pysam_ AlignmentFile object representing the BAM file.
        query_region_list (list): List of query regions, each defined as a tuple (chromosome, start, end).
        norm_method (str, optional): "CPM", "FPKM" or "Raw". Defaults to "CPM".
    Returns:
        list: List of normalized counts for each query region.
    """
    # count total 
    total_count = 0

    for info in bam_obj.get_index_statistics():
        total_count += info.mapped

    scale_value_list = []
    for region in query_region_list:
        
        region_chr_name = region[0]
        region_start = int(region[1])
        region_end = int(region[2])
        
        region_count = 0
        for align in bam_obj.fetch(contig=region_chr_name, start=region_start, end=region_end):
            region_count += 1
        
        if norm_method == "Raw":
            scale_value = region_count
        elif norm_method == "RPKM":
            region_length = region_end - region_start
            scale_value = region_count / 1.0 / (total_count / 1e6) / (region_length / 1e3)
        elif norm_method == "CPM":
            scale_value = region_count / 1.0 / (total_count / 1e6)
        else:
            raise ValueError("norm_method should be 'Raw', 'RPKM' or 'CPM'")

        scale_value_list.append(round(scale_value, 6))

    return scale_value_list


def compute_ref_point_matrix(
    input_bed: str,
    input_bam: str,
    ref_point: str,
    up_extend_length: int,
    down_extend_length: int,
    extend_binsize: int,
    count_norm_method: str,
) -> list:
    """Compute count matrix of reference point for a single region file.

    Args:
        input_bed (str): a temp bed file.
        input_bam (str): input bam file
        ref_point (str): reference point, TSS, TES, or center.
        up_extend_length (int): upstream region extend length.
        down_extend_length (int): downstream region extend length.
        extend_binsize (int): region extend binsize.
        count_norm_method (str): Can be RPKM, Raw or CPM.

    Returns:
        list: a list containing region information and signal values of each region.
    """
    in_bed_file = open(input_bed, "rt")
    bam_file = pysam.AlignmentFile(input_bam, "rb")

    all_info_list = []

    for region in in_bed_file:
        region_list = region.rstrip().split("\t")
        chrom = region_list[0]
        strand = region_list[5]

        if ref_point == "TSS":
            reference_point = int(region_list[1]) if strand == "+" else int(region_list[2])
        elif ref_point == "TES":
            reference_point = int(region_list[2]) if strand == "+" else int(region_list[1])
        elif ref_point == "center":
            reference_point = int((int(region_list[1]) + int(region_list[2])) / 2)
        else:
            raise ParsingError("ref_point should be TSS, TES, or center.")

        upstream_region_list = []
        downstream_region_list = []
        query_region_list = []

        if strand == "-":
            up_extend_length, down_extend_length = down_extend_length, up_extend_length

        # upstream
        for bin_start in range(reference_point - up_extend_length, reference_point, extend_binsize):
            bin_end = min(bin_start + extend_binsize, reference_point)
            upstream_region_list.append((chrom, bin_start, bin_end))

        # downstream
        for bin_start in range(reference_point, reference_point + down_extend_length, extend_binsize):
            bin_end = min(bin_start + extend_binsize, reference_point + down_extend_length)
            downstream_region_list.append((chrom, bin_start, bin_end))

        # reference point bin
        query_region_list.append((chrom, reference_point - extend_binsize / 2, reference_point + extend_binsize / 2))

        up_signal_val_list = query_region_count(
            bam_obj=bam_file,
            query_region_list=upstream_region_list,
            norm_method=count_norm_method,
        )

        query_signal_val_list = query_region_count(
            bam_obj=bam_file,
            query_region_list=query_region_list,
            norm_method=count_norm_method,
        )

        down_signal_val_list = query_region_count(
            bam_obj=bam_file,
            query_region_list=downstream_region_list,
            norm_method=count_norm_method,
        )

        merge_sinal_val_list = up_signal_val_list + query_signal_val_list + down_signal_val_list
        if strand == "-":
            merge_sinal_val_list.reverse()
        
        all_info_list.append(region_list + merge_sinal_val_list)


    in_bed_file.close()
    bam_file.close()
    return all_info_list


def compute_scale_region_matrix(
    input_bed: str,
    input_bam: str,
    up_extend_length: int,
    down_extend_length: int,
    extend_binsize: int,
    split_num: int,
    count_norm_method: str,
) -> list:
    """Compute count matrix of reference point for a single region file.

    Args:
        input_bed (str): a temp bed file.
        input_bam (str): input bam file
        up_extend_length (int): upstream region extend length.
        down_extend_length (int): downstream region extend length.
        extend_binsize (int): region extend binsize.
        split_num (int): number of bins to split region into.
        count_norm_method (str): Can be RPKM, Raw or CPM.

    Returns:
        list: a list containing region information and signal values of each region.
    """
    in_bed_file = open(input_bed, "rt")
    bam_file = pysam.AlignmentFile(input_bam, "rb")

    all_info_list = []

    for region in in_bed_file:
        region_list = region.rstrip().split("\t")
        chrom = region_list[0]
        strand = region_list[5]
        start = int(region_list[1])
        end = int(region_list[2])

        upstream_region_list = []
        downstream_region_list = []
        query_region_list = []

        if strand == "-":
            up_extend_length, down_extend_length = down_extend_length, up_extend_length

        # upstream
        for bin_start in range(start - up_extend_length, start, extend_binsize):
            bin_end = min(bin_start + extend_binsize, start)
            upstream_region_list.append((chrom, bin_start, bin_end))

        # downstream
        for bin_start in range(end, end + down_extend_length, extend_binsize):
            bin_end = min(bin_start + extend_binsize, end + down_extend_length)
            downstream_region_list.append((chrom, bin_start, bin_end))

        # gene body
        gene_body_length = end - start + 1
        bin_size = gene_body_length / split_num

        bin_start = start
        bin_count = 0
        while bin_start < end:
            bin_end = min(int(bin_start + bin_size), end)
            query_region_list.append((chrom, bin_start, bin_end))
            bin_start = bin_end
            bin_count += 1
            if bin_count >= split_num:
                break

        up_signal_val_list = query_region_count(
            bam_obj=bam_file,
            query_region_list=upstream_region_list,
            norm_method=count_norm_method,
        )

        query_signal_val_list = query_region_count(
            bam_obj=bam_file,
            query_region_list=query_region_list,
            norm_method=count_norm_method,
        )

        down_signal_val_list = query_region_count(
            bam_obj=bam_file,
            query_region_list=downstream_region_list,
            norm_method=count_norm_method,
        )

        merge_sinal_val_list = up_signal_val_list + query_signal_val_list + down_signal_val_list
        if strand == "-":
            merge_sinal_val_list.reverse()
        
        all_info_list.append(region_list + merge_sinal_val_list)


    in_bed_file.close()
    bam_file.close()
    return all_info_list