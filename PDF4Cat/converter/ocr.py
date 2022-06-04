import os
import io

from ..cat import PDF4Cat

class OCR(PDF4Cat):

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
		super(OCR, self).__init__(*args, **kwargs)

	# (it is faster)
	def gen_pdfImagesOCR(self, pages: list = [], 
		language: str = 'eng', 
		zoom: float = 1.5) -> tuple:
		"""Generator, generate BytesIO object
		
		Args:
			pages (list, optional): List of pages to select like [1, 3, 5, 15]
			language (str, optional): Language to ocr (look fitz.pdfocr_tobytes)
			zoom (float, optional): Zoom image (look fitz.Matrix docs)
		
		Yields:
			tuple: BytesIO
		"""
		pdf = self.pdf_open(self.doc_file, passwd=self.passwd)
		mat = self.fitz_Matrix(zoom, zoom)
		noOfPages = range(pdf.page_count)
		if pages:
			noOfPages = pages
		for pageNo in noOfPages:
			if pages and pageNo not in pages:
				continue
			io_data = io.BytesIO()
			#
			page = pdf.load_page(pageNo) #number of page
			pix = page.get_pixmap(matrix = mat)
			bytes_ = pix.pdfocr_tobytes(language=language)
			#

			yield bytes_

	@PDF4Cat.run_in_subprocess
	def pdfocr(self, 
		language: str = 'eng',
		output_pdf = None,
		pages: list = [],
		start_from: int = 0,
		zoom: float = 1.5) -> None:
		"""OCR pdf to file
		
		Args:
			language (str, optional): Language to ocr (look fitz.pdfocr_tobytes)
			output_pdf (None, optional): Output pdf file
			pages (list, optional): List of pages to select like [1, 3, 5, 15]
			start_from (int, optional): Enumerate from n
			zoom (float, optional): Zoom image (look fitz.Matrix docs)
		"""
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")
		output_pdf = os.path.join(os.getcwd(), output_pdf) #doc.insert_pdf(imgpdf)

		pdf_doc = self.pdf_open(self.doc_file)
		pdf = self.pdf_open()
		if not pages:
			pcount = pdf_doc.page_count
		else:
			pcount = len(pages)

		for bytes_ in self.gen_pdfImagesOCR(pages, language, zoom):
			with self.pdf_open("pdf", bytes_) as ocr_processed:
				pdf.insert_pdf(ocr_processed)

			self.counter += 1 #need enumerate
			self.progress_callback(self.counter, pcount)

		pdf.save(output_pdf)

		self.counter = 0



