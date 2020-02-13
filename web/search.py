from elasticsearch import Elasticsearch

class ElasticObj:
    def __init__(self, index_name, ip='127.0.0.1'):
        self.index_name = index_name
        self.es = Elasticsearch([ip], http_auth=('elastic', 'password'), port=9200)

    def search(self, keyword):
        doc = {
            'query': {
                'multi_match': {
                    'query': keyword,
                    'fields': ['title']
                }
            },
            'size': 1000
        }
        _searched = self.es.search(index=self.index_name, body=doc)
        return _searched['hits']['hits']