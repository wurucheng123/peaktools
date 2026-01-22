from fire import Fire
from .ref_point import main as run_reference_point
from .scale_region import main as run_scale_region

class CLI:
    """Cli interface for python package bamtools.

    - peaktools is a commandline tool and a python package
    """

    def reference_point(
        self,
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
        """Query bam file info.

        Args:
            input (str): Input bed
            input_bam (str): Input bam file
            output (str, optional): Output csv file.
            output_heatmap (str, optional): Output heatmap pdf file.
            output_profile (str, optional): Output profile pdf file.
            up_extend_length (int, optional): upstream region extend length. Defaults to 3000.
            down_extend_length (int, optional): downstream region extend length. Defaults to 3000.
            extend_binsize (int, optional): region extend binsize. Defaults to 100.
            count_norm_method (str, optional): Can be RPKM, Raw or CPM. Defaults to "RPKM".
            verbose (str, optional): The logging level as a string. Defaults to "ERROR".
            processes (int, optional): Number of processes to use. Defaults to 1.
            temp_dir (str, optional): folder to put temp files, use input dir if not defined. Defaults to None.
            vmin (int, optional): Lower boundary of scale bar. Defaults to 0.
            vmax (int, optional): Upper boundary of scale bar. Defaults to 99% quantile.
            cmap (str, optional): Color theme of heatmap. Defaults to "Purples".
        """
        run_reference_point(
            input=input,
            input_bam=input_bam,
            output=output,
            ref_point=ref_point,
            up_extend_length=up_extend_length,
            down_extend_length=down_extend_length,
            extend_binsize=extend_binsize,
            count_norm_method=count_norm_method,
            verbose=verbose,
            processes=processes,
            temp_dir=temp_dir,
            vmin=vmin,
            vmax=vmax,
            cmap=cmap,
            output_heatmap=output_heatmap,
            output_profile=output_profile,
        )

    def scale_region(
        self,
        input: str,
        input_bam: str,
        output: str,
        output_heatmap: str,
        output_profile: str,
        up_extend_length: int = 3000,
        down_extend_length: int = 3000,
        extend_binsize: int = 100,
        split_num: int = 100,
        count_norm_method: str = "RPKM",
        verbose: str = "ERROR",
        processes: int = 1,
        temp_dir: str = None,
        vmin: int = 0,
        vmax: int = None,
        cmap: str = "Purples",
    ):
        """Query bam file info.

        Args:
            input (str): Input bed
            input_bam (str): Input bam file
            output (str, optional): Output csv file.
            output_heatmap (str, optional): Output heatmap pdf file.
            output_profile (str, optional): Output profile pdf file.
            up_extend_length (int, optional): upstream region extend length. Defaults to 3000.
            down_extend_length (int, optional): downstream region extend length. Defaults to 3000.
            extend_binsize (int, optional): region extend binsize. Defaults to 100.
            split_num (int, optional): number of bins to split the region. Defaults to 100.
            count_norm_method (str, optional): Can be RPKM, Raw or CPM. Defaults to "RPKM".
            verbose (str, optional): The logging level as a string. Defaults to "ERROR".
            processes (int, optional): Number of processes to use. Defaults to 1.
            temp_dir (str, optional): folder to put temp files, use input dir if not defined. Defaults to None.
            vmin (int, optional): Lower boundary of scale bar. Defaults to 0.
            vmax (int, optional): Upper boundary of scale bar. Defaults to 99% quantile.
            cmap (str, optional): Color theme of heatmap. Defaults to "Purples".
        """
        run_scale_region(
            input=input,
            input_bam=input_bam,
            output=output,
            up_extend_length=up_extend_length,
            down_extend_length=down_extend_length,
            extend_binsize=extend_binsize,
            split_num=split_num,
            count_norm_method=count_norm_method,
            verbose=verbose,
            processes=processes,
            temp_dir=temp_dir,
            vmin=vmin,
            vmax=vmax,
            cmap=cmap,
            output_heatmap=output_heatmap,
            output_profile=output_profile,
        )

def main():
    cli = CLI()
    Fire(cli)

if __name__ == "__main__":
    main()


# python ./query_BAM_with_ref_point.py -h
# usage: query_BAM_with_ref_point.py [-h] -i INPUT -b INPUT_BAM [-o OUTPUT] [--up_extend_length UP_EXTEND_LENGTH]
#                                    [--down_extend_length DOWN_EXTEND_LENGTH] [--extend_binsize EXTEND_BINSIZE]
#                                    [--count_norm_method COUNT_NORM_METHOD] [--verbose VERBOSE]

# Query BAM count info

# options:
#   -h, --help            show this help message and exit
#   -i, --input INPUT     Input bed
#   -b, --input_bam INPUT_BAM
#                         Input bam file
#   -o, --output OUTPUT   Output default=stdout
#   --up_extend_length UP_EXTEND_LENGTH
#                         upstream region extend length, default=3000
#   --down_extend_length DOWN_EXTEND_LENGTH
#                         downstream region extend length, default=3000
#   --extend_binsize EXTEND_BINSIZE
#                         region extend binsize, default=100
#   --count_norm_method COUNT_NORM_METHOD
#                         Can be RPKM, Raw or CPM, default=RPKM
#   --verbose VERBOSE     Larger number means out more log info, can be 0,1,2,3 default=3