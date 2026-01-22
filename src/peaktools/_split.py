import os
import logging
import random
import gzip
import string

def split_file_and_make_temp(input_filename: str, temp_dir: str = None, n_part: int = 1) -> list:
    """
    Split input file into n_part temporary files.
    
    :param input_filename: Input bed file to be split.
    :param temp_dir: Directory to store temporary files. If None, uses the same directory as input file.
    :param n_part: Number of parts to split the input file into.
    :return: List of paths to the temporary files created.
    """
    if temp_dir is None:
        temp_dir = os.path.abspath(os.path.dirname(input_filename))
    else:
        temp_dir = os.path.abspath(temp_dir)

    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
        logging.info(f"Created temporary directory: {temp_dir}")

    if temp_dir[-1] != "/":
        temp_dir += "/"

    # count the number of lines in the input file
    logging.info(f"Counting lines in input file: {input_filename}")
    input = open(input_filename, 'rt') if not input_filename.endswith('.gz') else gzip.open(input_filename, 'rt')

    line_count = 0
    for line in input:
        line_count += 1

    input.close()

    if line_count % n_part == 0:
        lines_per_file = line_count // n_part
    else:
        lines_per_file = line_count // n_part + 1

    # create temporary files
    logging.info(f"Splitting input file into {n_part} parts, each with approximately {lines_per_file} lines.")

    input = open(input_filename, 'rt') if not input_filename.endswith('.gz') else gzip.open(input_filename, 'rt')
    input_file_basename = os.path.basename(input_filename)

    temp_filename_list = []
    temp_file_list = []

    for i in range(n_part):
        temp_file_basename = "temp_" + input_file_basename + "." + str(i) + "." + "".join(random.sample(string.ascii_letters + string.digits, 16))
        temp_file_name = os.path.join(temp_dir, temp_file_basename)
        temp_filename_list.append(temp_file_name)

        temp_file = open(temp_file_name, 'wt') if not input_filename.endswith('.gz') else gzip.open(temp_file_name, 'wt')
        temp_file_list.append(temp_file)

    # write lines to temporary files
    for index, line in enumerate(input):
        file_index = index // lines_per_file
        temp_file_list[file_index].write(line)

    logging.info(f"Finished writing lines to temporary files.")

    input.close()
    [file.close() for file in temp_file_list]

    return temp_filename_list