from .rotate import *

class Effects(Rotate):
	"""Parent class of PDF4Cat.Doc submodule"""
	def __init__(self, *args, **kwargs):
		super(Effects, self).__init__(*args, **kwargs)