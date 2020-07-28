import os
import glob
import glob2
import PyPDF2
import pandas as pd
import pdftotext
import time
from elasticsearch import Elasticsearch

def initES():
    es=Elasticsearch()
    return es

def updateIndex(es, body):
    #body={'name':'aaa', 'content':'using id as key'}
    #es.index(index='pdfindex', doc_type='_doc', id='path-filename-page', body=body)
    es.index(index='pdfindex', doc_type='_doc', body=body)
    return

def getPdfPages(pdfbook):
    file=pdfbook
    with open(file, "rb") as f:
        pdf = pdftotext.PDF(f)
    npage=1
    totPages=len(pdf)
    return totPages

def getTextFromPDF(pdfbook, pageNum=0):
    #file='pdfdata/TestingDoc.pdf'
    file=pdfbook
    with open(file, "rb") as f:
        pdf = pdftotext.PDF(f)
    npage=1
    totPages=len(pdf)
    #for page in pdf:
        #print('-----individual page---------', npage)
        #print(npage)
        #print(page)
        #npage=npage+1
    #print(pageNum)
    if pageNum==0:
        print('------ all pages data ------')
        print("\n\n".join(pdf))
        alltext="\n\n".join(pdf)
    else:
        alltext=pdf[pageNum-1]
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

def storePdfToES(pdfbook, es, storeByPage=False):
    pdftext=None
    if not storeByPage:
        pdftext, pages = getTextFromPDF(pdfbook, 0)
        print('-----start store all page to 1 Docs-----------', pdfbook, pages)
        print(pdftext, pages)
        print('-----end ----------')
        body={'name':pdfbook, 'content': pdftext, 'page': 0}
        updateIndex(es, body)
    # store by page
    else:
        nPages=getPdfPages(pdfbook)
        #pages from 1 but array still from 0
        for nPage in range(1, nPages+1):
            pdftext, pages = getTextFromPDF(pdfbook, nPage)
            print('-------  start store pdfbook page -----',pdfbook, nPage)
            print(pdftext)
            print('-------  end ---------------')
    #body={'name':'aaa', 'content':'using id as key'}
            if pdftext:
                body={'name':pdfbook, 'content': pdftext, 'page': nPage}
                updateIndex(es, body)
            else:
                print('no context in the pdf file')
                body={'name':pdfbook, 'content': pdftext, 'page': nPage}
                updateIndex(es, body)

    return True

#os.chdir('./pdfdata')
#pdfbooks=glob.glob('*.*')
pdfbooks=glob2.glob('./**/*.pdf', recursive=True)

print(len(pdfbooks))
print(pdfbooks)

storeByPage=True
es = initES()
for pdfbook in pdfbooks:
    print(pdfbook)
    storePdfToES(pdfbook, es,  storeByPage)


"""
os.chdir('./pdfdata')
pdfbooks=glob.glob('*.*')
print(len(pdfbooks))
print(pdfbooks)
df = PdfToTextToPD(pdfbooks)

for row_number in range(totPdfBooks):
    body={
        "name": str(df.iloc[row_number]['name']),
        "content":str(df.iloc[row_number]['content'])
          }
    print(body)
    print('-------------------------------')
"""
