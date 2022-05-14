# PDF4Cat
PDF4Cat Simple and Power tool for processing pdf docs using PyMuPDF

# Planing add
- [ ] CLI
- [ ] Async work & optimizations
## PDF:
- [X] Merge
- [X] Split
- [X] Rotate
- [ ] Edit Pages
- [X] Delete Pages and save to pdf(from pdf)
- [X] Extract Pages and save to pdf(from pdf)
- [X] Protect (Encrypt)
- [X] Unlock (Decrypt)
- [X] Compress (Flate)

## Other things:
- [X] OCR pdf
- [X] Pdf to Images
- [X] Images to pdf
### Add actions with docs:
- [ ] DOCX
- [ ] EXCEL
- [ ] POWER POINT
- [ ] OPEN OFFICE

Note: before use OCR run: 

1.  Install Tesseract.

2.  Locate Tesseract’s language support folder. Typically you will find it here:
        Windows: C:\Program Files\Tesseract-OCR\tessdata
        Unix systems: /usr/share/tesseract-ocr/4.00/tessdata

3.  Set the environment variable TESSDATA_PREFIX
        Windows: set TESSDATA_PREFIX=C:\Program Files\Tesseract-OCR\tessdata
        Unix systems: export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata

