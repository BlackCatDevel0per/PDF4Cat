import PDF4Cat

import resource
from time import time
from time import sleep

filenames = [
'pdf_file.pdf', 
'pdf_file.pdf', 
'pdf_file.pdf', 
]

imgfilenames = [
'test_data/test.png',
'test_data/test.png',
'test_data/test.png'
]

def example_callback(current, total) -> None:
    percentage = int('{:.0%}'.format(current / total)[:-1]) # XD
    if percentage % 5 == 0:
        print(f'Process reading.. {percentage}')
    # or you can
    # print(f'Process reading.. {percentage}')

def example_callback2(current, total) -> None:
    print(f'Process reading.. {current} of {total}')
    # or you can
    # print(f'Process reading.. {percentage}')

""" Simple Use Example """
s_time = time()
# Merge pdf files
PDF4Cat.Doc(filenames[0]).merge_file_with(filenames[0], output_pdf='test_data/merge_file_with.pdf')
# Merge multiple pdf files
PDF4Cat.Doc(None, filenames).merge_files_to('test_data/merge_files.pdf')
# Split pdf Pages and compress to zip
PDF4Cat.Doc(filenames[0]).split_pages2zip('test_data/splitted.zip', '{num}.pdf', 1)
# Rotate pdf Pages
PDF4Cat.Doc(filenames[0]).rotate_doc_to(90, 'test_data/rotated.pdf')
# Flate Compress pdf
PDF4Cat.Doc(filenames[0]).ReFlate_to('test_data/re_flated.pdf')
# Recompress pdf flate (optimize & compress)
PDF4Cat.PdfOptimizer(filenames[0]).ReFlate_to('test_data/re_flated.pdf')
# Rotate pdf Pages
PDF4Cat.Effects(filenames[0]).rotate_doc_to(180, 'test_data/rotated.pdf')
# Convert image to pdf
PDF4Cat.Converter('test_data/test.png').img2pdf('test_data/img2pdf.pdf')
# Convert images to pdf
PDF4Cat.Converter(None, imgfilenames).imgs2pdf('test_data/imgs2pdf.pdf')
# Multiple convert images to pdfs and compress to zip
PDF4Cat.Converter(None, imgfilenames).imgs2pdfs_zip('test_data/imgs2pdfs.zip')
c_time = time()
print()
print(int(c_time - s_time), "s.")
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")

#

""" Advanced Use Example"""
# """ Merge pdf files """
# s_time = time()
# PDF4Cat.Merger(filenames[0]).merge_file_with(filenames[0], output_pdf='test_data/merge_file_with.pdf')
# c_time = time()
# print()
# print(int(c_time - s_time), "s.")
# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")

# print()

# """ Merge pdf files 2 """
# s_time = time()
# PDF4Cat.Merger(None, filenames).merge_files('test_data/merge_files.pdf')
# c_time = time()
# print()
# print(int(c_time - s_time), "s.")
# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")

# print()

# """ Split pdf Pages """
# s_time = time()
# pdfs = PDF4Cat.Splitter(filenames[0])
# pdfs.split_pages2zip('test_data/splitted.zip', '{num}.pdf', 1)
# c_time = time()
# print()
# print(int(c_time - s_time), "s.")
# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")

#######################################
# """ Decrypt pdf """
# s_time = time()
# PDF4Cat.Crypter('test_data/encrypted.pdf', passwd="test000000").decrypt_to(output_pdf='test_data/decrypted.pdf')
# # need save_to or save
# c_time = time()
# print()
# print(int(c_time - s_time), "s.")
# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")

# """ Rotate pdf Pages """
# s_time = time()
# PDF4Cat.Effects(filenames[0]).rotate_doc_to(180, 'test_data/rotated.pdf')
# c_time = time()
# print()
# print(int(c_time - s_time), "s.")
# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")

# """ Convert Image to Pdf """
# s_time = time()
# PDF4Cat.Converter('test_data/test.png').img2pdf('test_data/img2pdf.pdf')
# c_time = time()
# print()
# print(int(c_time - s_time), "s.")
# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")

# """ Convert Images to Pdf """
# s_time = time()
# PDF4Cat.Converter(None, imgfilenames).imgs2pdf('test_data/imgs2pdf.pdf')
# c_time = time()
# print()
# print(int(c_time - s_time), "s.")
# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")

# """ Convert Images to Pdfs and compress to zip """
# s_time = time()
# PDF4Cat.Converter(None, imgfilenames).imgs2pdfs_zip('test_data/imgs2pdfs.zip')
# c_time = time()
# print()
# print(int(c_time - s_time), "s.")
# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")