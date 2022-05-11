from .merger import Merger
from .splitter import Splitter

class Doc(Merger, Splitter):
	def __init__(self, *args):
		super(Doc, self).__init__(*args)
		