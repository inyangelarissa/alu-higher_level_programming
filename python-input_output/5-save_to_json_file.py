#!/usr/bin/python3
'''script to write an object to textfile using json'''


import json


def save_to_json_file(my_obj, filename):
    '''writes an object to textfile using json'''
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
