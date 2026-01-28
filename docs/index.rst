.. peaktools documentation master file, created by
   sphinx-quickstart on Wed Jan 28 11:46:26 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

peaktools documentation
=======================

**peaktools** is a Python package & command-line tool for peak visualization from ChIP-seq and ATAC-seq data.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api

Quick Start
-----------

Install via pip::

    pip install peaktools-wrc

Basic Usage
~~~~~~~~~~~

For reference point analysis::

    peaktools reference-point \
        hg38_refseq_gene_TSS_TES.protein_only.chr21.bed \
        ./bam_files/K562-ATACSeq-rep1.ENCFF534DCE_chr21_chr22.bam \
        ATAC_heatmap.pdf ATAC_profile.pdf \
        --output ./signal_ATACSeq.RefPoint.csv -p 4

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. toctree::
   :maxdepth: 2
   :caption: Contents:

