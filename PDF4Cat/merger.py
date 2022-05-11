import os

from .cat import PDF4Cat

class Merger(PDF4Cat):
	def __init__(self, *args, **kwargs):
		super(Merger, self).__init__(*args, **kwargs)

	# need in_memory merge func

	@PDF4Cat.run_in_subprocess
	def merge_file_with(self, input_pdf, output_pdf = None) -> None:
		if not output_pdf:
			output_pdf = os.path.join(self.pdf_path, self.pdf_name+"_out.pdf")
		pdf = self.pdf_new()

		input_pdf_pages_count = len(self.pdf_open(input_pdf).pages)
		total = self.pages_count + input_pdf_pages_count
		for file in (self.pdf_file, input_pdf):
			src = self.pdf_open(file)
			for page in src.pages: ###
				pdf.pages.append(page)
				del page
				self.counter += 1
				self.progress_callback(self.counter, total)
			src.close()
			del src

		self.counter = 0

		pdf.save(output_pdf)
		pdf.close()
		del pdf

	@PDF4Cat.run_in_subprocess
	def merge_files_to(self, output_pdf = None) -> None:
		if not output_pdf:
			output_pdf = os.path.join(self.pdf_path, self.pdf_name+"_out.pdf")
		pdf = self.pdf_new()

		input_pdf_pages_count = 0
		for ipdf in self.input_pdf_list:
			input_pdf_pages_count += len(self.pdf_open(ipdf).pages)
		total = input_pdf_pages_count
		for file in self.input_pdf_list:
			src = self.pdf_open(file)
			for page in src.pages: ###
				pdf.pages.append(page)
				del page
				self.counter += 1
				self.progress_callback(self.counter, total)
			src.close()
			del src

		self.counter = 0

		pdf.save(output_pdf)
		pdf.close()
		del pdf