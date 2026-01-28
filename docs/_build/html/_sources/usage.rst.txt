Usage
=====

Command-line Interface
----------------------

Reference Point Analysis
~~~~~~~~~~~~~~~~~~~~~~~~

Analyze peaks around a reference point (e.g., TSS)::

    peaktools reference-point \
        <bed_file> \
        <bam_file> \
        <heatmap_output> \
        <profile_output> \
        --output <csv_output> \
        -p <num_processes>

Scale Region Analysis
~~~~~~~~~~~~~~~~~~~~~

Analyze peaks across scaled regions::

    peaktools scale_region \
        <bed_file> \
        <bam_file> \
        <csv_output> \
        <heatmap_output> \
        <profile_output> \
        -p <num_processes>

Python Package
--------------

You can also use peaktools as a Python package::

    import peaktools
    
    # Your code here