import logging
import multiprocessing
from ._count import compute_ref_point_matrix, compute_scale_region_matrix

def multi_region_compute_ref_point_matrix(
    input_bed_list: list,
    input_bam: str,
    ref_point: str,
    up_extend_length: int,
    down_extend_length: int,
    extend_binsize: int,
    count_norm_method: str,
    processes: int,
) -> list:
    """Compute count matrix of reference point.

    Args:
        input_bed_list (list): a list of temp bed files.
        input_bam (str): input bam file
        ref_point (str): reference point, TSS, TES, or center.
        up_extend_length (int): upstream region extend length.
        down_extend_length (int): downstream region extend length.
        extend_binsize (int): region extend binsize.
        count_norm_method (str): Can be RPKM, Raw or CPM.
        processes (int): Number of processes to use.

    Returns:
        list: a list containing region information and signal values of each region.
    """
    # Placeholder for actual implementation
    logging.info(f"Counting matrices in {input_bam} with {processes} threads.")

    pool = multiprocessing.Pool(processes=processes)

    # record info
    process_info_list = []

    # count reads for each region
    for input_bed in input_bed_list:
        process_info = pool.apply_async(
            func=compute_ref_point_matrix,
            args=(
                input_bed,
                input_bam,
                ref_point,
                up_extend_length,
                down_extend_length,
                extend_binsize,
                count_norm_method,
            ),
        )
        process_info_list.append(process_info)

    # wait for all tasks to complete
    pool.close()
    pool.join()

    # out pool result
    merge_process_info_list = []
    for process_info in process_info_list:
        merge_process_info_list.extend(process_info.get())
    merge_process_info_list.sort(key=lambda x: sum(x[6:] ) / (len(x) - 6), reverse=True)
    logging.info(f"{input_bam} calculation done!")

    return merge_process_info_list

def multi_region_compute_scale_region_matrix(
    input_bed_list: list,
    input_bam: str,
    up_extend_length: int,
    down_extend_length: int,
    extend_binsize: int,
    split_num: int,
    count_norm_method: str,
    processes: int,
) -> list:
    """Compute count matrix of reference point.

    Args:
        input_bed_list (list): a list of temp bed files.
        input_bam (str): input bam file
        up_extend_length (int): upstream region extend length.
        down_extend_length (int): downstream region extend length.
        extend_binsize (int): region extend binsize.
        split_num (int): number of bins to split region into.
        count_norm_method (str): Can be RPKM, Raw or CPM.
        processes (int): Number of processes to use.

    Returns:
        list: a list containing region information and signal values of each region.
    """
    # Placeholder for actual implementation
    logging.info(f"Counting matrices in {input_bam} with {processes} threads.")

    pool = multiprocessing.Pool(processes=processes)

    # record info
    process_info_list = []

    # count reads for each region
    for input_bed in input_bed_list:
        process_info = pool.apply_async(
            func=compute_scale_region_matrix,
            args=(
                input_bed,
                input_bam,
                up_extend_length,
                down_extend_length,
                extend_binsize,
                split_num,
                count_norm_method,
            ),
        )
        process_info_list.append(process_info)

    # wait for all tasks to complete
    pool.close()
    pool.join()

    # out pool result
    merge_process_info_list = []
    for process_info in process_info_list:
        merge_process_info_list.extend(process_info.get())
    merge_process_info_list.sort(key=lambda x: sum(x[6:] ) / (len(x) - 6), reverse=True)
    logging.info(f"{input_bam} calculation done!")

    return merge_process_info_list