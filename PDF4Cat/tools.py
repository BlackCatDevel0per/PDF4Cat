import os

from .cat import PDF4Cat

class Tools(PDF4Cat):

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
		super(Tools, self).__init__(*args, **kwargs)

	@PDF4Cat.run_in_subprocess
	def extract_pages2pdf(self, 
		output_pdf = None,
		pages: list = []) -> None:
		"""Extract list of selected pages like [1, 3, 5, 15] and save to pdf file
		
		Args:
			output_pdf (None, optional): Output pdf file
			pages (list, optional): List of pages to select like [1, 3, 5, 15]
		"""
		pdf = self.pdf_open(self.doc_file, passwd=self.passwd)

		output_pdf = os.path.join(os.getcwd(), output_pdf)

		pdf.select(pages)
		pdf.save(output_pdf)

	@PDF4Cat.run_in_subprocess
	def delete_pages2pdf(self, 
		output_pdf = None,
		pages: list = []) -> None:
		"""Delete list of selected pages like [1, 3, 5, 15] and save to pdf file
		
		Args:
			output_pdf (None, optional): Output pdf file
			pages (list, optional): List of pages to select like [1, 3, 5, 15]
		"""
		pdf = self.pdf_open(self.doc_file, passwd=self.passwd)

		output_pdf = os.path.join(os.getcwd(), output_pdf)

		pdf.delete_pages(pages)
		pdf.save(output_pdf)



# generator decorator & save2zip soon..