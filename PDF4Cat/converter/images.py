import os
import io
import zipfile
from PIL import Image

from ..cat import Base
from ..cat import PDF4Cat

class Img2Pdf(Base):
	def __init__(self, *args, **kwargs):
		super(Img2Pdf, self).__init__(*args, **kwargs)

	@Base.run_in_subprocess
	def img2pdf(self, 
		output_pdf = None,
		format: str = None) -> None:
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")
		if not format:
			format = os.path.splitext(self.doc_file)[1][1:]

		Image.open(self.doc_file).convert('RGB').save(output_pdf, format=format)

	@Base.run_in_subprocess
	def imgs2pdf(self, 
		output_pdf = None,
		format: str = None) -> None:
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")
		# if not format:
		# 	format = os.path.splitext(self.doc_file)[1][1:]

		input_imgs_list = []
		len_docs = len(self.input_doc_list)

		for img_path in self.input_doc_list:
			input_imgs_list.append(Image.open(img_path).convert('RGB'))
			self.counter += 1
			self.progress_callback(self.counter, len_docs)

		input_imgs_list[0].save(output_pdf, 
			save_all=True, 
			append_images=input_imgs_list[1:]) # No format

	# Generate name with BytesIO object (it is faster)
	def gen_images(self, fimages, start_from) -> tuple:
		for num, img in enumerate(self.input_doc_list): ###
			io_data = io.BytesIO()
			img_ext = os.path.splitext(img)[1][1:]
			Image.open(img).convert('RGB').save(io_data, format=img_ext)

			imfn = fimages.format(name=os.path.basename(img), num=num+start_from)
			imfi = io_data
			yield imfn, imfi

	@Base.run_in_subprocess
	def imgs2pdfs_zip(self, 
		out_zip_file: str, 
		fimages: str = '{name}_{num}.pdf',
		start_from: int = 0) -> None:

		# Compression level: zipfile.ZIP_DEFLATED (8) and disable ZIP64 ext.
		with zipfile.ZipFile(out_zip_file, 'w', zipfile.ZIP_DEFLATED, False) as zf:

			for file_name, io_data in self.gen_images(fimages, start_from):
				zf.writestr(file_name, io_data.getvalue())
				self.counter += 1 #need enumerate
				self.progress_callback(self.counter, len(self.input_doc_list))

		self.counter = 0

#

class Pdf2Img(Base):
	def __init__(self, *args, **kwargs):
		super(Pdf2Img, self).__init__(*args, **kwargs)
		# self.pdf = self.pdf_open(self.doc_file, password=self.passwd)
		self.pdf = self.pdf_open(self.doc_file)

	# Generate name with BytesIO object (it is faster)
	def _gen_images(self, fimages, start_from) -> tuple:
		ext_from_fimages = os.path.splitext(fimages)[1][1:]
		zoom = 2 # to increase the resolution
		mat = self.fitz_Matrix(zoom, zoom)
		noOfPages = self.pdf.pageCount
		for pageNo in range(noOfPages):
			io_data = io.BytesIO()
			#
			page = self.pdf.load_page(pageNo) #number of page
			pix = page.get_pixmap(matrix = mat)
			io_data.write(pix.tobytes(output=ext_from_fimages))
			#

			imfn = fimages.format(name=os.path.basename(self.doc_file), num=pageNo+start_from)
			imfi = io_data
			yield imfn, imfi

	@Base.run_in_subprocess
	def pdf2imgs_zip(self, 
		out_zip_file: str, 
		fimages: str = '{name}_{num}.png',
		start_from: int = 0) -> None:
		
		pcount = self.pdf.pageCount

		# Compression level: zipfile.ZIP_DEFLATED (8) and disable ZIP64 ext.
		with zipfile.ZipFile(out_zip_file, 'w', zipfile.ZIP_DEFLATED, False) as zf:
		
			for file_name, io_data in self._gen_images(fimages, start_from):
				zf.writestr(file_name, io_data.getvalue())
				self.counter += 1 #need enumerate
				self.progress_callback(self.counter, pcount)

		self.counter = 0
		
