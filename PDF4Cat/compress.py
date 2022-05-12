import os

from .cat import PDF4Cat

class PdfOptimizer(PDF4Cat):
	def __init__(self, *args, **kwargs):
		super(PdfOptimizer, self).__init__(*args, **kwargs)
		self.pdf = self.pike_open(self.doc_file)

	@PDF4Cat.run_in_subprocess
	def ReFlate_to(self, output_pdf = None):
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")

		self.pdf.save(output_pdf, recompress_flate=True)