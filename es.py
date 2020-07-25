from elasticsearch import Elasticsearch
es=Elasticsearch()
body={'name':'aaa', 'content':'bbb'}
es.index(index='pdfindex', doc_type='_doc', body=body)
body={'name':'aaa', 'content':'bbb'}
es.index(index='pdfindex', doc_type='_doc', id='1', body=body)

body={'name':'aaa', 'content':'using id as key'}
es.index(index='pdfindex', doc_type='_doc', id='path-filename-page', body=body)



