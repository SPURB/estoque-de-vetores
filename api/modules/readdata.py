#!/usr/bin/python
import json

def read(name):
    path = '../public/_data/' + name + '.json'
    with open(path) as json_data:
        d = json.load(json_data)
        return d