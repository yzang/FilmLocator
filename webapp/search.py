from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, A, Q, Field

client = Elasticsearch()
INDEX_NAME = 'filmlocator'
DOC_TYPE = 'film'
PAGE_SIZE = 100


def elastic_retrieve():
    s = Search(using=client, index=INDEX_NAME, doc_type=DOC_TYPE)
    s = s[0:PAGE_SIZE]
    dataset = []
    for hit in s.scan():
        dataset.append(hit)
    return dataset


def elastic_retrieve(filters):
    pass


def elastic_suggest(prefix, field):
    s = Search(using=client, index=INDEX_NAME, doc_type=DOC_TYPE)
    q = Q({"match_phrase_prefix": {field: prefix}})
    s = s.query(q)
    s = s.fields(field)
    s = s[0:PAGE_SIZE]
    dataset = set()
    for hit in s.scan():
        dataset.add(hit.to_dict().get(field)[0])
    return dataset