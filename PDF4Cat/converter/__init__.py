from .images import *
from .ocr import *
from .any import *

class Converter(Img2Pdf, Pdf2Img, OCR, any_doc_convert):
	def __init__(self, *args, **kwargs):
		super(Converter, self).__init__(*args, **kwargs)