#!/usr/bin/env python3
from elasticsearch import Elasticsearch

es_host = Elasticsearch(["https://elastic:-Rel0twWMUk8L-ZtZr=I@192.168.2.126:9200/"],
                        ca_certs=False, verify_certs=False)

res = es_host.search(index="kibana*", body={"query": {"match_all": {}}})
print("Hits Total: " + str(res['hits']['total']['value']))


