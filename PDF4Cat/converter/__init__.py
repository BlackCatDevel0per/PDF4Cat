from .images import *

class Converter(Img2Pdf, Pdf2Img):
	def __init__(self, *args, **kwargs):
		super(Converter, self).__init__(*args, **kwargs)