import os

from .cat import PDF4Cat

class PdfOptimizer(PDF4Cat):

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
		super(PdfOptimizer, self).__init__(*args, **kwargs)
		
	@PDF4Cat.run_in_subprocess
	def DeFlate_to(self, output_pdf = None) -> None:
		"""Deflate pdf to file
		
		Args:
			output_pdf (None, optional): Output pdf file
		"""
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")

		pdf = self.pdf_open(self.doc_file, passwd=self.passwd)
		pdf.save(output_pdf, 
			deflate=True,
			deflate_images=True,
			deflate_fonts=True,
			garbage=4,
			clean=1) # clean is compressing
		pdf.close()
