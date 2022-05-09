import os
import io
import zipfile

from .cat import PDF4Cat
from .helpers import run_in_subprocess

class Splitter(PDF4Cat):
   def __init__(self, *args):
      super(Splitter, self).__init__(*args)

   # Generate name with BytesIO object (it is faster)
   def gen_split(self, fpages, start_from) -> tuple:
      for num, page in enumerate(self.pdf.pages): ###
        dst = self.pdf_new()
        dst.pages.append(page)
        pdata = io.BytesIO()
        dst.save(pdata)
        del dst

        pdfn = fpages.format(name=self.pdf_filename, num=num+start_from)
        pdfp = pdata
        yield pdfn, pdfp

   @run_in_subprocess
   def split_pages2zip(
      self,
      zip_file: str, 
      fpages: str = '{name}_{num}.pdf',
      start_from: int = 0) -> None:

      # Compression level: zipfile.ZIP_DEFLATED (8) and disable ZIP64 ext.
      with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED, False) as zf:

         for file_name, data in self.gen_split(fpages, start_from):
            zf.writestr(file_name, data.getvalue())
            self.counter += 1
            self.progress_callback(self.counter, self.pages_count)

      self.counter = 0
   
