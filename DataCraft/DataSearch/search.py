from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date,Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch,helpers
from . import models
import json

connections.create_connection()

class PublishserDataIndex(DocType):
    publisher = Text()
    title = Text()
    description = Text()
    data_classification = Text()
    department = Text()
    subdepartment = Text()
    data_change_frequency = Text()
    automated_fashion = Text()
    dataset_come_from = Text()
    automation_option = Text()
    api_endpoint=Text()
    inventory_ID = Text()
    data_classification_comments = Text()
    class Meta:
        index = 'publishserdata-index'

def bulk_indexing():
    PublishserDataIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.PublishserData.objects.all().iterator()))

def search(title):
    s = Search().filter('term', title=title)
    response = s.execute()
    return response

# def depart(department):
#     s = Search().filter('term', department=department)
#     response = s.execute()
#     return response

# def description(description):
#     s=Search()
#     data=s.filter('term',tags=['title', 'description'])
#     response=s.execute()
#     return response
# from DataSearch.search import *