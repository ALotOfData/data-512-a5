import argparse
import os

input_path = '../raw_data/'
output_path = '../raw_data/txt_files/'

# Get all pdf files under path
file_paths = []
for root, directories, files in os.walk(input_path):
    for file in files:
        if ".pdf" in file:
            # Create file paths
            pdf_file_path = os.path.join(root, file)
            pdf_file_path = pdf_file_path.replace('(', '\(')
            pdf_file_path = pdf_file_path.replace(')', '\)')
            txt_file_path = pdf_file_path[:-3] + 'txt'

            # You will need to have the pdftotext command line command available
            pdf_to_text_cmd = f'pdftotext -l 1 {pdf_file_path}'
            os.system(pdf_to_text_cmd)

            mv_cmd = f'mv {txt_file_path} {output_path}'
            os.system(mv_cmd)
