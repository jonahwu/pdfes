import os
import glob2
from pathlib import Path
import pathlib




#os.chdir('./pdfdata')
pdfbooks=glob2.glob('./**/*.pdf', recursive=True)
print(len(pdfbooks))
print(pdfbooks)


"""
all_header_files = glob2.glob('./pdfdata/**/*.pdf',recursive=True)
print('--- new -----')
print(all_header_files)
print('----new new ----')
for file_path in Path('./pdfdata').glob('**/*.pdf'):
    print(file_path) # do whatever you need with these files

print('----new new new ----')
for p in pathlib.Path("./pdfdata").rglob("*.pdf"):
    print(p)
"""
