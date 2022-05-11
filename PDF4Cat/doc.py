from .splitter import Splitter
from .merger import Merger
from .crypt import Crypter
from .effects import Effects

class Doc(Merger, Splitter, Crypter, Effects):
	def __init__(self, *args, **kwargs):
		super(Doc, self).__init__(*args, **kwargs)
		