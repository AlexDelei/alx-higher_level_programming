#!/usr/bin/python3
"""Adds items from arguments"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
existing_data = load_from_json_file(filename)

# Add the command-line arguments to the list
new_data = existing_data + sys.argv[1:]

# Save the updated list to the JSON file
save_to_json_file(new_data, filename)
