import os
import io
from PIL import Image
import zipfile

from ..cat import PDF4Cat

class Img2Pdf(PDF4Cat):
	def __init__(self, *args, **kwargs):
		super(Img2Pdf, self).__init__(*args, **kwargs)

	@PDF4Cat.run_in_subprocess
	def img2pdf(self, 
		output_pdf = None) -> None:
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")

		pic = self.fitz_open(self.doc_file)
		pdf = self.fitz_open("pdf", pic.convert_to_pdf())
		pdf.save(output_pdf)

	@PDF4Cat.run_in_subprocess
	def imgs2pdf(self, 
		output_pdf = None) -> None:
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")

		len_docs = len(self.input_doc_list)

		result = self.fitz_open()
		for img_path in self.input_doc_list:
			pic = self.fitz_open(self.doc_file)
			pdf = self.fitz_open("pdf", pic.convert_to_pdf())
			result.insert_pdf(pdf)
			self.counter += 1
			self.progress_callback(self.counter, len_docs)
		result.save(output_pdf)

	# Generate name with BytesIO object (it is faster)
	def gen_imagesi2p(self, fimages, start_from) -> tuple:
		for num, img in enumerate(self.input_doc_list): ###
			io_data = io.BytesIO()
			img_ext = os.path.splitext(img)[1][1:]
			pic = self.fitz_open(img)
			pdf = self.fitz_open("pdf", pic.convert_to_pdf())
			pdf.save(io_data)

			imfn = fimages.format(name=os.path.basename(img), num=num+start_from)
			imfi = io_data
			yield imfn, imfi

	@PDF4Cat.run_in_subprocess
	def imgs2pdfs_zip(self, 
		out_zip_file: str, 
		fimages: str = '{name}_{num}.pdf',
		start_from: int = 0) -> None:

		# Compression level: zipfile.ZIP_DEFLATED (8) and disable ZIP64 ext.
		with zipfile.ZipFile(out_zip_file, 'w', zipfile.ZIP_DEFLATED, False) as zf:

			for file_name, io_data in self.gen_imagesi2p(fimages, start_from):
				zf.writestr(file_name, io_data.getvalue())
				self.counter += 1 #need enumerate
				self.progress_callback(self.counter, len(self.input_doc_list))

		self.counter = 0

#

class Pdf2Img(PDF4Cat):
	def __init__(self, *args, **kwargs):
		super(Pdf2Img, self).__init__(*args, **kwargs)
		# self.pdf = self.pdf_open(self.doc_file, password=self.passwd)
		self.fitz_pdf = self.fitz_open(self.doc_file)

	# Generate name with BytesIO object (it is faster)
	def gen_imagesp2i(self, pages, fimages, start_from) -> tuple:
		ext_from_fimages = os.path.splitext(fimages)[1][1:]
		zoom = 2 # to increase the resolution
		mat = self.fitz_Matrix(zoom, zoom)
		noOfPages = range(self.fitz_pdf.pageCount)
		if pages:
			noOfPages = pages
		for pageNo in noOfPages:
			if pages and pageNo not in pages:
				continue
			io_data = io.BytesIO()
			#
			page = self.fitz_pdf.load_page(pageNo) #number of page
			pix = page.get_pixmap(matrix = mat)
			io_data.write(pix.tobytes(output=ext_from_fimages))
			#

			imfn = fimages.format(name=os.path.basename(self.doc_file), num=pageNo+start_from)
			imfi = io_data
			yield imfn, imfi

	@PDF4Cat.run_in_subprocess
	def pdf2imgs_zip(self, 
		out_zip_file: str, 
		pages: list = [],
		fimages: str = '{name}_{num}.png',
		start_from: int = 0) -> None:
		
		if not pages:
			pcount = self.fitz_pdf.pageCount
		else:
			pcount = len(pages)

		# Compression level: zipfile.ZIP_DEFLATED (8) and disable ZIP64 ext.
		with zipfile.ZipFile(out_zip_file, 'w', zipfile.ZIP_DEFLATED, False) as zf:
		
			for file_name, io_data in self.gen_imagesp2i(pages, fimages, start_from):
				zf.writestr(file_name, io_data.getvalue())
				self.counter += 1 #need enumerate
				self.progress_callback(self.counter, pcount)

		self.counter = 0

