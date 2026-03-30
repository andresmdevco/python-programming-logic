"""
JSON Y XML
"""
import xml.etree.ElementTree as xml
import os
import json

data = {
    "name": "Andrés Muñoz",
    "age": 25,
    "birth_date": "06-08-2000",
    "programming_languages": ["Python", "Javascript", "C++"]
}

# XML
xml_file = "andres.xml"

def save_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:    
            child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(xml_file, encoding="utf-8")

save_xml()

with open(xml_file, "r", encoding="utf-8") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

# JSON
json_file = "andres.json"

with open(json_file, "w", encoding="utf-8") as json_data:
    json.dump(data, json_data, ensure_ascii=False)

with open(json_file, "r", encoding="utf-8") as json_data:
    print(json_data.read())

os.remove(json_file)