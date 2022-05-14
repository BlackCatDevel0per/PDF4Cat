from .images import *
from .ocr import *

class Converter(Img2Pdf, Pdf2Img, OCR):
	def __init__(self, *args, **kwargs):
		super(Converter, self).__init__(*args, **kwargs)