# from elasticsearch_dsl.connections import connections
# from elasticsearch_dsl import DocType, Text, Date, Search

# from elasticsearch.helpers import bulk
# from elasticsearch import Elasticsearch
# from . import models

# connections.create_connection()

# class PostIndex(DocType):
#     user = Text()
#     timestamp = Date()
#     title = Text()
#     content = Text()

#     class Meta:
#         index = 'post-index'

# def bulk_indexing():
#     BlogPostIndex.init()
#     es = Elasticsearch()
#     bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))


# def search(author):
#     s = Search().filter('term', author=author)
#     response = s.execute()
#     return response