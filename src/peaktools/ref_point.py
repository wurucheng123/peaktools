import gzip
import os
import sys
import logging

from ._logging import set_logging_level
from ._split import split_file_and_make_temp
from ._multiprocess import multi_region_compute_ref_point_matrix
from ._error import RemoveTempError
from ._plot import plot_heatmap_and_profile

def main(
    input: str,
    input_bam: str,
    output: str,
    output_heatmap: str,
    output_profile: str,
    ref_point: str = "TSS",
    up_extend_length: int = 3000,
    down_extend_length: int = 3000,
    extend_binsize: int = 100,
    count_norm_method: str = "RPKM",
    verbose: str = "ERROR",
    processes: int = 1,
    temp_dir: str = None,
    vmin: int = 0,
    vmax: int = None,
    cmap: str = "Purples",
):
    # set up logging level
    set_logging_level(level=verbose)

    region_split_filename_list = split_file_and_make_temp(
        input_filename=input, temp_dir=temp_dir, n_part=processes
    )

    all_info_list = multi_region_compute_ref_point_matrix(
        input_bed_list=region_split_filename_list,
        input_bam=input_bam,
        ref_point=ref_point,
        up_extend_length=up_extend_length,
        down_extend_length=down_extend_length,
        extend_binsize=extend_binsize,
        count_norm_method=count_norm_method,
        processes=processes,
    )

    # merge file
    out_file = open(output, "wt") if not output.endswith(".gz") else gzip.open(output, "wt")
    bed_header = ["chrom", "start", "end", "name", "score", "strand"]
    scale_region_headers = [f"bin_{i+1}" for i in range(len(all_info_list[0]) - 6)]
    out_header = bed_header + scale_region_headers
    out_header_str = ",".join(out_header)
    out_file.write(out_header_str + "\n")

    for info in all_info_list:
        out_line = ",".join(map(str, info))
        out_file.write(out_line + "\n")

    # ---------------------------->>>
    # close and clean temp file
    # ---------------------------->>>
    sys.stderr.write("-" * 80 + "\n")
    logging.info("Removing temp files...")

    for temp_filename in region_split_filename_list:
        if os.path.exists(temp_filename):
            if os.path.isfile(temp_filename):
                try:
                    os.remove(temp_filename)
                except Exception:
                    raise RemoveTempError

    out_file.close()

    # plot heatmap and profile
    plot_heatmap_and_profile(
        matrix_file=output,
        output_heatmap=output_heatmap,
        output_profile=output_profile,
        vmin=vmin,
        vmax=vmax,
        cmap=cmap,
    )

    logging.info("Everything is done!")