import os
import io
import zipfile
from PIL import Image

from ..cat import Base

class Img2Pdf(Base):
	def __init__(self, *args, **kwargs):
		super(Img2Pdf, self).__init__(*args, **kwargs)

	@Base.run_in_subprocess
	def img2pdf(self, output_pdf = None):
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")

		Image.open(self.doc_file).convert('RGB').save(output_pdf)

	@Base.run_in_subprocess
	def imgs2pdf(self, 
		output_pdf: str) -> None:
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")

		input_imgs_list = []
		for img in self.input_doc_list:
			img = Image.open(self.doc_file).convert('RGB')
			input_imgs_list.append(img)

		input_imgs_list[0].save(output_pdf, save_all=True, append_images=input_imgs_list[1:])

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

