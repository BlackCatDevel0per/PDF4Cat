import os

from .cat import PDF4Cat

class Crypter(PDF4Cat):

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
		super(Crypter, self).__init__(*args, **kwargs)

	@PDF4Cat.run_in_subprocess
	def crypt_to(self, 
		user_passwd: str = None, 
		owner_passwd: str = None, 
		perm: dict = None, 
		crypt_type: int = PDF4Cat.PDF_ENCRYPT_AES_256,
		output_pdf: str = None) -> None:
		"""Crypt pdf and save to file (don't forget give password in class parameter)

		Args:
			user_passwd (str, optional): Pdf user password
			owner_passwd (str, optional): Pdf owner password
			perm (dict, optional): Permissions see past example - :perm
			crypt_type (int, optional): Crypt type, default AES256 (PDF4Cat.PDF_ENCRYPT_AES_256)
			output_pdf (None, optional): Output pdf file
		
		Raises:
			TypeError: "Missing user and owner password!"
		
		perm = int(PDF4Cat.PDF_PERM_ACCESSIBILITY
				| PDF4Cat.PDF_PERM_PRINT
				| PDF4Cat.PDF_PERM_COPY
				| PDF4Cat.PDF_PERM_ANNOTATE)
		"""
		pdf = self.pdf_open(self.doc_file, passwd=self.passwd)

		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")
		output_pdf = os.path.join(os.getcwd(), output_pdf)


		if not user_passwd:
			user_passwd = owner_passwd+"_user"
		if not owner_passwd:
			owner_passwd = user_passwd+"_owner"
		if not user_passwd and not owner_passwd:
			raise TypeError("Missing user and owner password!")

		# print(user_passwd, owner_passwd)

		if not perm:
			perm = int(
				PDF4Cat.PDF_PERM_ACCESSIBILITY
				| PDF4Cat.PDF_PERM_PRINT
				| PDF4Cat.PDF_PERM_COPY
				| PDF4Cat.PDF_PERM_ANNOTATE
			)

		pdf.save(
			output_pdf,
			encryption=crypt_type,
			owner_pw=owner_passwd,
			user_pw=user_passwd,
			permissions=perm,
		)

	@PDF4Cat.run_in_subprocess
	def decrypt_to(self,
		output_pdf = None) -> None:
		"""Decrypt pdf and save to file (don't forget give password in class parameter)
		
		Args:
			output_pdf (None, optional): Output pdf file
		"""
		if not output_pdf:
			output_pdf = os.path.join(self.doc_path, self.doc_name+"_out.pdf")
		output_pdf = os.path.join(os.getcwd(), output_pdf)

		pdf = self.pdf_open(self.doc_file)
		# pdf = self.pdf_open(self.doc_file, passwd=self.passwd) # bug, saves blank(white pages) doc
		# the document should be password protected
		assert pdf.needsPass, "Document is not encrypted"

		pdf.authenticate(self.passwd)

		pdf.save(output_pdf)


