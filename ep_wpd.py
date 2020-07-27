import os
import glob
import PyPDF2
import pandas as pd
import pdftotext
import time



def getTextFromPDF(pdfbook, pageNum=0):
    #file='pdfdata/TestingDoc.pdf'
    file=pdfbook
    with open(file, "rb") as f:
        pdf = pdftotext.PDF(f)
    npage=1
    totPages=len(pdf)
    for page in pdf:
        print('-----individual page---------', npage)
        print(npage)
        print(page)
        npage=npage+1
    print(pageNum)
    if pageNum==0:
        print('------ all pages data ------')
        print("\n\n".join(pdf))
        alltext="\n\n".join(pdf)
    else:
        alltext=pdf[pageNum]
    return alltext, totPages

def PdfToTextToPD(files):
    this_loc=1
    df=pd.DataFrame(columns=("name", "content"))
    for file in files:
        this_doc=""
        this_text, n_pages=getTextFromPDF(file)
        this_doc+=this_text

        df.loc[this_loc] = file, this_doc
        this_loc=this_loc+1
    return df


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


os.chdir('./pdfdata')
pdfbooks=glob.glob('*.*')
print(len(pdfbooks))
print(pdfbooks)
df = PdfToTextToPD(pdfbooks)


print('---------show head-----------')
print(df.head())
print('--------- show head end ---------')
col_name = df.columns
print('------ show total col -----------')
print(df.shape[0])
totPdfBooks=df.shape[0]
for row_number in range(totPdfBooks):
    body={
        "name": str(df.iloc[row_number]['name']),
        "content":str(df.iloc[row_number]['content'])
          }
    print(body)
    print('-------------------------------')
    # insert es here for each PdfFile and also can insert by pages.
"""
for book in pdfbooks:
    print(book)
    #textpdf, totPages = getTextFromPDF(book)
    textpdf, totPages = PdfToTextToPD(book)
    print(textpdf)
    print('total pages:',totPages)
df=extractPdfFiles(pdfbooks)
print(df.head())

col_name = df.columns
for row_number in range(df.shape[0]):
    for name in col_name:
        print(str(df.iloc[row_number][name]))
        #body=dict([name, str(df.iloc[row_number][name])) for name in col_names])
        #print(body)
"""
