import os

from ..cat import PDF4Cat

class Rotate(PDF4Cat):
	def __init__(self, *args, **kwargs):
		super(Rotate, self).__init__(*args, **kwargs)
		self.pdf = self.pike_open(self.doc_file)

	@PDF4Cat.run_in_subprocess
	def rotate_doc_to(self, angle: int, output_pdf=None):
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")

		if not angle % 90 == 0:
			raise TypeError("Angle must be a multiple of 90!")
		for page in self.pdf.pages:
			page.Rotate = angle
		self.pdf.save(output_pdf)