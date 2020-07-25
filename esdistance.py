from elasticsearch import Elasticsearch
es=Elasticsearch()
body={'title':'elastic search python client integrated'}
s=es.index(index='distance', doc_type='_doc', body=body)
print(s)
#getData=es.get(index='distance', doc_type='_doc', id=7)
#print(getData)
"""
body={'title':'elastic search python client integrated33335'}
res=es.create(index='distance', doc_type='_doc', body=body, id='33335')
print(res)
"""
"""
body={'title':'透過python client產生中文，很多很多中文科科科'}
res=es.create(index='distance', doc_type='_doc', body=body, id='33336')
print(res)
"""
body={"doc":
    {'title':'haha透過python client產生中文，很多很多中文科科科'}}
res=es.update(index='distance', doc_type='_doc', body=body, id='33336')
print(res)
"""
body={"doc":
    {'title':'new 透過python client產生中文，很多很多中文科科科'}}
res=es.create(index='distance', doc_type='_doc', body=body, id='33337')
"""

# search, we can fit lots
result = es.search(
    index="distance",
    body={
        "query": {
            "match_all": {}
        }
    }
)
print(result)
