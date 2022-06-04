from .splitter import Splitter
from .merger import Merger
from .crypt import Crypter
from .effects import Effects
from .compress import PdfOptimizer
# from .tools import Tools

class Doc(Merger, Splitter, Crypter, Effects, PdfOptimizer):
	"""Parent class of PDF4Cat.doc submodule"""
	def __init__(self, *args, **kwargs):
		super(Doc, self).__init__(*args, **kwargs)
		