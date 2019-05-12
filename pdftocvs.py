import tabula
import os

input_path = "pdfs"
output_path = "result"

input_file_list = [file for file in os.listdir(input_path) if file.endswith(".pdf")]

for pdf in input_file_list:
    tabula.convert_into(input_path + "/" + pdf, output_path + "/" + pdf.replace(".pdf", ".cvs"), output_format="csv", pages='all')
    print("complete!")