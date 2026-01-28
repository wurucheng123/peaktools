# Peaktools
## About peaktools
Brief: **peaktools**, a python **package** & **command-line tool** for **peak visualization** from ChIP-seq and ATAC-seq data.

Home: https://github.com/wurucheng123/peaktools

License: MIT License

## About Author
Name: Ru-Cheng Wu | Email: wrc1953@outlook.com

## Installation
You can install peaktools via pip:
```bash
pip install peaktools-wrc
```
## Usage
To use peaktools visualize peaks in a reference point:
```bash
peaktools reference-point \
    hg38_refseq_gene_TSS_TES.protein_only.chr21.bed \
    ./bam_files/K562-ATACSeq-rep1.ENCFF534DCE_chr21_chr22.bam \
    ATAC_heatmap.pdf ATAC_profile.pdf \
    --output ./signal_ATACSeq.RefPoint.csv -p 4
```
To use peaktools visualize peaks in a scale region:
```bash
peaktools scale_region \
    hg38_refseq_gene_TSS_TES.protein_only.chr21.bed \
    ./bam_files/293.ChIP.H3K4me3.rep1.ENCFF449FCR.bam \
    signal_H3K4me3.ScaleRegion.csv \
    ./H3K4me3_heatmap.pdf ./H3K4me3_profile.pdf -p 4
```
For more parameters and information, you can run:
```bash
peaktools reference-point -h
peaktools scale_region -h
```
## Doc
See [Doc](https://wurucheng123.github.io/peaktools/)