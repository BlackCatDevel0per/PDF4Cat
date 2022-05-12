import os
import io
import zipfile

from .cat import PDF4Cat

class Splitter(PDF4Cat):
	def __init__(self, *args, **kwargs):
		super(Splitter, self).__init__(*args, **kwargs)

	# Generate name with BytesIO object (it is faster)
	def gen_split(self, fpages, start_from) -> tuple:
		for num, page in enumerate(self.pdf.pages): ###
			dst = self.pdf_new()
			dst.pages.append(page)
			io_data = io.BytesIO()
			dst.save(io_data)
			dst.close()
			del dst

			pdfn = fpages.format(name=self.pdf_filename, num=num+start_from)
			pdfp = io_data
			yield pdfn, pdfp

	@PDF4Cat.run_in_subprocess # need add range
	def split_pages2zip(
		self,
		out_zip_file: str, 
		fpages: str = '{name}_{num}.pdf',
		start_from: int = 0) -> None:

		# Compression level: zipfile.ZIP_DEFLATED (8) and disable ZIP64 ext.
		with zipfile.ZipFile(out_zip_file, 'w', zipfile.ZIP_DEFLATED, False) as zf:

			for file_name, io_data in self.gen_split(fpages, start_from):
				zf.writestr(file_name, io_data.getvalue())
				self.counter += 1 #need enumerate
				self.progress_callback(self.counter, self.pages_count)

		self.counter = 0
	
