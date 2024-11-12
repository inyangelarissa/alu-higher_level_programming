#!/usr/bin/python3
'''script to create object from json file'''


import json


def load_from_json_file(filename):
    '''creates object from json file'''
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
