import os
import io
import zipfile

from .cat import PDF4Cat

class Splitter(PDF4Cat):

	"""Subclass of PDF4Cat parent class
	
	Args:
		doc_file (None, optional): Document file (for multiple operations, 'use input_doc_list')
		input_doc_list (list, optional): List of input docs
		passwd (str, optional): Document password (for crypt/decrypt)
		progress_callback (None, optional): Progress callback like:
	
	Raises:
		TypeError: If you use doc_file with input_doc_list (you can use only one)
	"""

	def __init__(self, *args, **kwargs):
		super(Splitter, self).__init__(*args, **kwargs)

	# (it is faster)
	def gen_split(self, 
		from_pdf = None, 
		pages: list = [], 
		fpages: str = '{name}_{num}.pdf', 
		start_from: int = 0) -> tuple: # pdfname & pdfbytes
		"""Generator, generate name with BytesIO object
		
		Args:
			from_pdf (None, optional): pdf document name (default use main doc from class param)
			pages (list, optional): List of pages to select like [1, 3, 5, 15]
			fpages (str, optional): Format pdf filenames
			start_from (int, optional): Enumerate from n
		
		Yields:
			tuple: filename, BytesIO
		"""
		if not from_pdf:
			from_pdf = self.pdf_open(self.doc_file, passwd=self.passwd)
		noOfPages = range(from_pdf.page_count)
		if pages:
			noOfPages = pages
		for pageNo in noOfPages: ###
			if pages and pageNo not in pages:
				continue
			# dst = from_pdf.convert_to_pdf() # if already pdf returns bytes
			# dst = self.pdf_open("pdf", stream=dst) # 
			dst = self.pdf_open()
			dst.insert_pdf(from_pdf, from_page=pageNo, to_page=pageNo) # need load page
			io_data = io.BytesIO()
			dst.save(io_data)
			dst.close()
			del dst

			pdfn = fpages.format(name=self.doc_filename, num=pageNo+start_from)
			pdfp = io_data
			yield pdfn, pdfp

	@PDF4Cat.run_in_subprocess # need add range
	def split_pages2zip(
		self,
		out_zip_file: str, 
		pages: list = [], 
		fpages: str = '{name}_{num}.pdf',
		start_from: int = 0) -> None:
		"""Split pages to different pdfs and compress to zip
		
		Args:
			out_zip_file (str): Output zip file
			pages (list, optional): List of pages to select like [1, 3, 5, 15]
			fpages (str, optional): Format pdf filenames
			start_from (int, optional): Enumerate from n
		"""
		pdf = self.pdf_open(self.doc_file, passwd=self.passwd)
		if not pages:
			pcount = pdf.page_count
		else:
			pcount = len(pages)

		# Compression level: zipfile.ZIP_DEFLATED (8) and disable ZIP64 ext.
		with zipfile.ZipFile(out_zip_file, 'w', zipfile.ZIP_DEFLATED, False) as zf:

			for file_name, io_data in self.gen_split(pdf, pages, fpages, start_from):
				zf.writestr(file_name, io_data.getvalue())
				self.counter += 1 #need enumerate
				self.progress_callback(self.counter, pcount)

				del io_data

		self.counter = 0
	