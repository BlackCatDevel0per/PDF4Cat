import os
import multiprocessing
from pikepdf import Pdf

class PDF4Cat:
	def __init__(self, pdf_file=None, input_pdf_list: list=None, progress_callback=None):
		if not pdf_file and input_pdf_list:
			pdf_file = input_pdf_list[0]
		elif pdf_file:
			pass
		else:
			raise TypeError("Required 1 argument of pdf_file, input_pdf_list. ")
		self.input_pdf_list = input_pdf_list
		self.pdf_file = pdf_file
		self.pdf_path = os.path.split(pdf_file)[0]
		self.pdf_name = os.path.basename(os.path.splitext(pdf_file)[0])
		self.pdf_filename = os.path.basename(pdf_file)

		self.pdf_new = Pdf.new
		self.pdf_open = Pdf.open
		self.pdf = self.pdf_open(pdf_file)

		self.progress_callback = progress_callback
		self.counter = 0
		if not progress_callback:
			self.progress_callback = self.pc

	def pc(self, current, total) -> None:
		#
		print(f'Progress: {current} of {total} complete', end="\r")
		# if current != total:
		# 	print(f'Progress: {current} of {total} complete', end="\r")
		# else:
		# 	print(f'Progress: {current} of {total} complete')

	@property
	def pages_count(self) -> int:
		return len(self.pdf.pages)
