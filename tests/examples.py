import PDF4Cat

import resource
from time import time
from time import sleep

filenames = [
'pdf_file.pdf', 
'pdf_file.pdf', 
'pdf_file.pdf', 
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
# Merge Files
PDF4Cat.Doc(filenames[0]).merge_file_with(filenames[0], output_pdf='test_data/merge_file_with.pdf')
# Merge multiple Files
PDF4Cat.Doc(None, filenames).merge_files_to('test_data/merge_files.pdf')
# Split File Pages
PDF4Cat.Doc(filenames[0]).split_pages2zip('test_data/splitted.zip', '{num}.pdf', 1)
c_time = time()
print()
print(int(c_time - s_time), "s.")
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")

# """ Merge Files Example """
# s_time = time()
# PDF4Cat.Merger(filenames[0]).merge_file_with(filenames[0], output_pdf='test_data/merge_file_with.pdf')
# c_time = time()
# print()
# print(int(c_time - s_time), "s.")
# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")

# print()

# """ Merge Files Example 2 """
# s_time = time()
# PDF4Cat.Merger(None, filenames).merge_files('test_data/merge_files.pdf')
# c_time = time()
# print()
# print(int(c_time - s_time), "s.")
# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")

# print()

# """ Split File Pages Example """
# s_time = time()
# pdfs = PDF4Cat.Splitter(filenames[0])
# pdfs.split_pages2zip('test_data/splitted.zip', '{num}.pdf', 1)
# c_time = time()
# print()
# print(int(c_time - s_time), "s.")
# print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, "KB.")
