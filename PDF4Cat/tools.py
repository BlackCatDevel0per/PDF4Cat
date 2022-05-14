import os

from .cat import PDF4Cat

class Tools(PDF4Cat):
	def __init__(self, *args, **kwargs):
		super(Tools, self).__init__(*args, **kwargs)

	@PDF4Cat.run_in_subprocess
	def extract_pages2pdf(self, 
		output_pdf = None,
		pages: list = []) -> None:
		fitz_pdf = self.fitz_open(self.doc_file)

		output_pdf = os.path.join(os.getcwd(), output_pdf)

		fitz_pdf.select(pages)
		fitz_pdf.save(output_pdf)

	@PDF4Cat.run_in_subprocess
	def delete_pages2pdf(self, 
		output_pdf = None,
		pages: list = []) -> None:
		fitz_pdf = self.fitz_open(self.doc_file)

		output_pdf = os.path.join(os.getcwd(), output_pdf)

		fitz_pdf.delete_pages(pages)
		fitz_pdf.save(output_pdf)



# generator decorator & save2zip soon..