#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a fil."""
import sys
import os.path


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

lst = []

if os.path.exists("add_item.json"):
    lst = load_from_json_file("add_item.json")

for arg in sys.argv[1:]:
    lst.append(arg)

save_to_json_file(lst, "add_item.json")
