import os

from ..cat import PDF4Cat

class Rotate(PDF4Cat):

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
		super(Rotate, self).__init__(*args, **kwargs)
		
	@PDF4Cat.run_in_subprocess
	def rotate_doc_to(self, angle: int, output_pdf=None):
		"""Rotate document to n angle
		
		Args:
			angle (int): Angle multiple of 90
			output_pdf (None, optional): Output pdf file
		
		Raises:
			TypeError: "Angle must be a multiple of 90!"
		"""
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")
		output_pdf = os.path.join(os.getcwd(), output_pdf)

		pdf = self.pdf_open(self.doc_file, passwd=self.passwd)
		pdf2 = self.pdf_open()

		if not angle % 90 == 0:
			raise TypeError("Angle must be a multiple of 90!")
		for num in range(pdf.page_count):
			pdf2.insert_pdf(pdf, from_page=num, to_page=num, rotate=angle)

			self.counter += 1
			self.progress_callback(self.counter, pdf.page_count)
		pdf2.save(output_pdf)