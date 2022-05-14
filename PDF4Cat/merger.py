import os

from .cat import PDF4Cat

class Merger(PDF4Cat):
	def __init__(self, *args, **kwargs):
		super(Merger, self).__init__(*args, **kwargs)

	# need in_memory merge func

	@PDF4Cat.run_in_subprocess
	def merge_file_with(self, input_pdf, output_pdf = None) -> None:
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")
		fitz_pdf = self.fitz_open(self.doc_file)
		
		output_pdf = os.path.join(os.getcwd(), output_pdf)
		input_pdf = os.path.join(os.getcwd(), input_pdf)

		input_pdf = self.fitz_open(input_pdf) # 2

		result = self.fitz_open()
		result.insert_pdf(fitz_pdf) # 1
		result.insert_pdf(input_pdf) # 2
		result.save(output_pdf)

	@PDF4Cat.run_in_subprocess
	def merge_files_to(self, output_pdf = None) -> None:
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")
		
		output_pdf = os.path.join(os.getcwd(), output_pdf)

		result = self.fitz_open()
		for pdf in self.input_doc_list:
			with self.fitz_open(pdf) as f:
				result.insert_pdf(f)
		result.save(output_pdf)