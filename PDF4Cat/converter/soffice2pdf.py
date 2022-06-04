import os
import tempfile
import subprocess, shlex
import shutil

from ..cat import PDF4Cat

class soffice_convert(PDF4Cat):

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
		super(soffice_convert, self).__init__(*args, **kwargs)

	def soffice_convert_to(self, doc_type: str, output_doc: str):
		"""Libre Office converter wrapper for convert document to any supported by soffice
		
		Args:
			doc_type (str): Output document type to convert
			output_doc (str): Output document file
		"""
		temp_pdf = os.path.join(tempfile.gettempdir(), f"""{self.doc_name}.{doc_type}""")
		subprocess.run(shlex.split(f"""soffice --headless --convert-to {doc_type} {self.doc_file} --outdir {tempfile.gettempdir()}"""), 
			) # stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		shutil.move(temp_pdf, output_doc)
		
	def soffice_convert2pdf(self, output_pdf: str):
		"""Libre Office converter wrapper for convert document to pdf
		
		Args:
			output_pdf (str): Output pdf file
		
		Raises:
			NotImplementedError: If Libre Office not support this conversion
		"""
		if self.doc_fileext in self.libre_exts:
			temp_pdf = os.path.join(tempfile.gettempdir(), f"""{self.doc_name}.pdf""")
			subprocess.run(shlex.split(f"""soffice --headless --convert-to pdf {self.doc_file} --outdir {tempfile.gettempdir()}"""), 
				stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			shutil.move(temp_pdf, output_pdf)
		else:
			raise NotImplementedError(f"File extension '{self.doc_fileext}' => '.pdf' not supported")

	def soffice_convert2pdf_a(self, a: int, output_pdf: str):
		"""Libre Office converter wrapper for convert document to pdf/a
		
		Args:
			a (int): A type (1, 2)
			output_pdf (str): Output pdf file
		
		Raises:
			NotImplementedError: If Libre Office not support this conversion
		"""
		if not a:
			a = 1
		# soffice --headless --convert-to pdf:"writer_pdf_Export:SelectPdfVersion=1" --outdir outdir input.pdf
		if self.doc_fileext in self.libre_exts:
			temp_pdf = os.path.join(tempfile.gettempdir(), f"""{self.doc_name}.pdf""")
			subprocess.run(shlex.split(f"""soffice --headless --convert-to pdf:"writer_pdf_Export:SelectPdfVersion={a}" {self.doc_file} --outdir {tempfile.gettempdir()}"""), 
				stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			shutil.move(temp_pdf, output_pdf)
		else:
			raise NotImplementedError(f"File extension '{self.doc_fileext}' => '.pdf' not supported")



