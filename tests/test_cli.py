from peaktools import cli_main

if __name__ == "__main__":
    cli_main()

# NAME
#     test_cli.py reference-point - Query bam file info.

# SYNOPSIS
#     test_cli.py reference-point INPUT INPUT_BAM OUTPUT OUTPUT_HEATMAP OUTPUT_PROFILE <flags>

# DESCRIPTION
#     Query bam file info.

# POSITIONAL ARGUMENTS
#     INPUT
#         Type: str
#         Input bed
#     INPUT_BAM
#         Type: str
#         Input bam file
#     OUTPUT
#         Type: str
#         Output csv file.
#     OUTPUT_HEATMAP
#         Type: str
#         Output heatmap pdf file.
#     OUTPUT_PROFILE
#         Type: str
#         Output profile pdf file.

# FLAGS
#     -r, --ref_point=REF_POINT
#         Type: str
#         Default: 'TSS'
#     -u, --up_extend_length=UP_EXTEND_LENGTH
#         Type: int
#         Default: 3000
#         upstream region extend length. Defaults to 3000.
#     -d, --down_extend_length=DOWN_EXTEND_LENGTH
#         Type: int
#         Default: 3000
#         downstream region extend length. Defaults to 3000.
#     -e, --extend_binsize=EXTEND_BINSIZE
#         Type: int
#         Default: 100
#         region extend binsize. Defaults to 100.
#     --count_norm_method=COUNT_NORM_METHOD
#         Type: str
#         Default: 'RPKM'
#         Can be RPKM, Raw or CPM. Defaults to "RPKM".
#     --verbose=VERBOSE
#         Type: str
#         Default: 'ERROR'
#         The logging level as a string. Defaults to "ERROR".
#     -p, --processes=PROCESSES
#         Type: int
#         Default: 1
#         Number of processes to use. Defaults to 1.
#     -t, --temp_dir=TEMP_DIR
#         Type: Optional[str]
#         Default: None
#         folder to put temp files, use input dir if not defined. Defaults to None.
#     --vmin=VMIN
#         Type: int
#         Default: 0
#         Lower boundary of scale bar. Defaults to 0.
#     --vmax=VMAX
#         Type: Optional[int]
#         Default: None
#         Upper boundary of scale bar. Defaults to 99% quantile.
#     --cmap=CMAP
#         Type: str
#         Default: 'Purples'
#         Color theme of heatmap. Defaults to "Purples".

# NOTES
#     You can also use flags syntax for POSITIONAL ARGUMENTS


# NAME
#     test_cli.py scale_region - Query bam file info.

# SYNOPSIS
#     test_cli.py scale_region INPUT INPUT_BAM OUTPUT OUTPUT_HEATMAP OUTPUT_PROFILE <flags>

# DESCRIPTION
#     Query bam file info.

# POSITIONAL ARGUMENTS
#     INPUT
#         Type: str
#         Input bed
#     INPUT_BAM
#         Type: str
#         Input bam file
#     OUTPUT
#         Type: str
#         Output csv file.
#     OUTPUT_HEATMAP
#         Type: str
#         Output heatmap pdf file.
#     OUTPUT_PROFILE
#         Type: str
#         Output profile pdf file.

# FLAGS
#     -u, --up_extend_length=UP_EXTEND_LENGTH
#         Type: int
#         Default: 3000
#         upstream region extend length. Defaults to 3000.
#     -d, --down_extend_length=DOWN_EXTEND_LENGTH
#         Type: int
#         Default: 3000
#         downstream region extend length. Defaults to 3000.
#     -e, --extend_binsize=EXTEND_BINSIZE
#         Type: int
#         Default: 100
#         region extend binsize. Defaults to 100.
#     -s, --split_num=SPLIT_NUM
#         Type: int
#         Default: 100
#         number of bins to split the region. Defaults to 100.
#     --count_norm_method=COUNT_NORM_METHOD
#         Type: str
#         Default: 'RPKM'
#         Can be RPKM, Raw or CPM. Defaults to "RPKM".
#     --verbose=VERBOSE
#         Type: str
#         Default: 'ERROR'
#         The logging level as a string. Defaults to "ERROR".
#     -p, --processes=PROCESSES
#         Type: int
#         Default: 1
#         Number of processes to use. Defaults to 1.
#     -t, --temp_dir=TEMP_DIR
#         Type: Optional[str]
#         Default: None
#         folder to put temp files, use input dir if not defined. Defaults to None.
#     --vmin=VMIN
#         Type: int
#         Default: 0
#         Lower boundary of scale bar. Defaults to 0.
#     --vmax=VMAX
#         Type: Optional[int]
#         Default: None
#         Upper boundary of scale bar. Defaults to 99% quantile.
#     --cmap=CMAP
#         Type: str
#         Default: 'Purples'
#         Color theme of heatmap. Defaults to "Purples".

# NOTES
#     You can also use flags syntax for POSITIONAL ARGUMENTS

# python ./peaktools/tests/test_cli.py reference-point hg38_refseq_gene_TSS_TES.protein_only.chr21.bed ./bam_files/K562-ATACSeq-rep1.ENCFF534DCE_chr21_chr22.bam ATAC_heatmap.pdf ATAC_profile.pdf --output ./signal_ATACSeq.RefPoint.csv --verbose DEBUG -p 4
# python ./peaktools/tests/test_cli.py scale_region hg38_refseq_gene_TSS_TES.protein_only.chr21.bed ./bam_files/293.ChIP.H3K4me3.rep1.ENCFF449FCR.bam signal_H3K4me3.ScaleRegion.csv ./H3K4me3_heatmap.pdf ./H3K4me3_profile.pdf -p 4
# python ./peaktools/tests/test_cli.py scale_region hg38_refseq_gene_TSS_TES.protein_only.chr21.bed ./bam_files/293.ChIP.H3K36me3.rep1.ENCFF899GOH.bam signal_H3K36me3.ScaleRegion.csv ./H3K36me3_heatmap.pdf ./H3K36me3_profile.pdf -p 4