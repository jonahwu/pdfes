import os
import glob
import PyPDF2
import pandas as pd

os.chdir('./pdfdata')
pdfbooks=glob.glob('*.*')
print(len(pdfbooks))
print(pdfbooks)

def extractPdfFiles(files):
    this_loc=1
    df=pd.DataFrame(columns=("name", "content"))
    for file in files:
        pdfFileObj=open(file, 'rb')
        pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
        n_pages=pdfReader.numPages
        this_doc=""
        for i in range(n_pages):
            pageObj=pdfReader.getPage(i)
            this_text=pageObj.extractText()
            print('------ utf-8 -----')
            print(str(this_text.encode('utf-8')))
            print('------ origin -----')
            print(this_text)
            this_doc+=this_text

        df.loc[this_loc] = file, this_doc
        this_loc=this_loc+1
    return df

for book in pdfbooks:
    print(book)
df=extractPdfFiles(pdfbooks)
print(df.head())

col_name = df.columns
for row_number in range(df.shape[0]):
    for name in col_name:
        print(str(df.iloc[row_number][name]))
        #body=dict([name, str(df.iloc[row_number][name])) for name in col_names])
        #print(body)
