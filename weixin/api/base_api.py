import logging

import requests
import yaml


class BaseApi(object):
    logging.basicConfig(level=logging.DEBUG)
    
    def request(self, method, url, **kwargs):
        self.result_data = requests.request(method=method, url=url, **kwargs)
        return self.result_data

    def load_yaml(self, po_path, **kwargs):
        file = open(po_path, 'r', encoding='UTF-8')
        po_data = yaml.load(file)


