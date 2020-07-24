#Author : Icarus Caeser
#File created on 12 Jul 2020 9:17 AM

# Place the pdf file in the same directory as that of this script and run the script.

import pdf2image
import os
import time

delay_b4_exit = 10

dir2use = os.getcwd()

def clean_dir(dir_path, spare_files=[]):
    all_files = os.listdir(dir_path)
    for filename in all_files:
        if filename not in spare_files and not filename.startswith('.'):
            os.remove(os.path.join(dir_path, filename))

def get_pdf_to_use(dir2use):
    all_files = os.listdir(dir2use)
    pdf2convert = None
    for filename in all_files:
        if filename.endswith('.pdf'):
            if pdf2convert == None:
                pdf2convert = filename
            else:
                print('There are more than two pdf files in the directory')
                time.sleep(delay_b4_exit)
                exit()
    return pdf2convert

spare_files = [os.path.basename(__file__)]
pdf2use = get_pdf_to_use(dir2use)
if pdf2use == None:
    print('There are no pdf files in the current directory')
    time.sleep(delay_b4_exit)
    exit()
spare_files.append(pdf2use)

query = input("All the files in {} will be deleted except {}. Type yes to proceed and any other key to exit\n".format(dir2use, spare_files))
if query != 'yes':
    exit()
clean_dir(dir2use, spare_files=spare_files)
print('converting {} to images '.format(pdf2use))

output_file_name = str(pdf2use).replace('.pdf', '')
pdf2image.convert_from_path(os.path.join(dir2use, pdf2use), output_folder=dir2use, output_file=output_file_name, fmt='jpeg')

print('conversion successfull')
time.sleep(delay_b4_exit)




