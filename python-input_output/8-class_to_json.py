#!/usr/bin/python3
'''script from javascript object notation(JSON) to object'''


import json


def from_json_string(my_obj):
    '''from json to object'''
    return json.loads(my_obj)
