#!/usr/bin/env python3
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# disable https verification check warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def current_indices_list(es_host, index_prefix):
    current_indices = []
    http_header = {'content-type': 'application/json'}
    response = requests.get(es_host + "/_cat/indices/" + index_prefix + "*", headers=http_header, verify=False)
    for line in response.text.split('\n'):
        if line:
            current_indices.append(line.split()[2])
    return current_indices

if __name__ == "__main__":
    username = 'elastic'
    password = '-Rel0twWMUk8L-ZtZr=I'
    es_host = 'https://'+username+':'+password+'@192.168.2.126:9200'
    indices_list = current_indices_list(es_host, 'kibana')
    print(indices_list)

