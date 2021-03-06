import PDF4Cat

import resource
from time import time
from time import sleep

filenames = [
'test_data/pdf_file.pdf', 
'test_data/pdf_file.pdf', 
'test_data/pdf_file.pdf', 
]

imgfilenames = [
'test_data/test.png',
'test_data/test.png',
'test_data/test.png',
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
PDF4Cat.Doc(filenames[0]).DeFlate_to('test_data/re_flated.pdf')
# or
PDF4Cat.PdfOptimizer(filenames[0]).DeFlate_to('test_data/re_flated.pdf')
# Rotate pdf Pages
PDF4Cat.Effects(filenames[0]).rotate_doc_to(180, 'test_data/rotated.pdf')
# Convert pdf to docx (images)
PDF4Cat.Converter(filenames[0]).pdf2docx("test_data/pdf2docx.docx")
# Convert pdf to pptx (images)
PDF4Cat.Converter(filenames[0]).pdf2pptx("test_data/pdf2pptx.pptx")
# Convert docx to html
PDF4Cat.Converter('test_data/pdf2docx.docx').docx2html("test_data/docx2html.html")
# Convert html to pdf
PDF4Cat.Converter('test_data/docx2html.html').convert2pdf('test_data/html_convert2pdf.pdf')

# Convert:
# [
# ".doc", ".odt", ".ott", 
# ".docx", ".fodp", ".dotx",
# ".csv", ".otp", ".ods",
# ".odp", ".odf", ".otg",
# ".xls", ".xlsx", ".ppt", 
# ".pptx", ".txt", ".xml",
# "epub"
# ]
# to pdf by libre-office (need installed)
# PDF4Cat.Converter('doc_name_or_path').soffice_convert2pdf('save_file_to.pdf')
PDF4Cat.Converter('test_data/pdf2docx.docx').soffice_convert2pdf("test_data/soffice_docx2pdf.pdf")
# in convert2pdf by param use_soffice=True
PDF4Cat.Converter('test_data/pdf2docx.docx').convert2pdf('test_data/docx_convert2pdf.pdf', use_soffice=True)
# and other soffice convert:
PDF4Cat.Converter('test_data/test.xlsx').soffice_convert_to("pdf", "test_data/soffice_xlsx2pdf.pdf")
# Convert pdf to pdf/a v. 1 or 2
PDF4Cat.Converter('test_data/pdf2docx.docx').soffice_convert2pdf_a(1, "test_data/soffice_pdf2pdf_a_v1.pdf")
# Convert image to pdf
PDF4Cat.Converter('test_data/test.png').img2pdf('test_data/img2pdf.pdf')
PDF4Cat.Converter('test_data/test.png').convert2pdf('test_data/img2pdf.pdf')
# Convert images to pdf
PDF4Cat.Converter(None, imgfilenames).imgs2pdf('test_data/imgs2pdf.pdf')
# Multiple convert images to pdfs and compress to zip
PDF4Cat.Converter(None, imgfilenames).imgs2pdfs_zip('test_data/imgs2pdfs.zip')
# Convert docx to pdf (images)
PDF4Cat.Converter('test_data/pdf2docx.docx').convert2pdf('test_data/docx_convert2pdf.pdf')
PDF4Cat.Converter('test_data/pdf2docx.docx').docx2pdf("test_data/docx2pdf.pdf")
# Convert image to pdf
PDF4Cat.Converter('test_data/test.png').img2pdf('test_data/img2pdf.pdf')
# Convert multiple images to pdf
PDF4Cat.Converter(None, imgfilenames).imgs2pdf('test_data/imgs2pdfs.pdf')
# # Convert multiple images to pdfs and compress to zip
# PDF4Cat.Converter(None, imgfilenames).imgs2pdfs_zip('test_data/imgs2pdf.zip')

# Convert pdf to images and compress to zip
PDF4Cat.Converter(filenames[0]).pdf2imgs_zip('test_data/pdf2imgs.zip')
# Convert pdf to images with select pages and compress to zip
PDF4Cat.Converter(filenames[0]).pdf2imgs_zip('test_data/pdf2imgs10515.zip', pages=[10, 5, 15])

# Extract pages and save to pdf
PDF4Cat.Tools(filenames[0]).extract_pages2pdf('test_data/ep2pdf.pdf', [5, 15, 27])
# Delete pages and save to pdf
PDF4Cat.Tools(filenames[0]).delete_pages2pdf('test_data/dp2pdf.pdf', [0, 1, 5, 15, 27])

# OCR pdf
PDF4Cat.Converter('test_data/img2pdf.pdf').pdfocr("rus", 'test_data/pdfocr.pdf')

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