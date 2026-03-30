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

def create_xml():

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

create_xml()

with open(xml_file, "r", encoding="utf-8") as xml_data:
    print(xml_data.read())

os.remove(xml_file)

# JSON
json_file = "andres.json"

def create_json():
    with open(json_file, "w", encoding="utf-8") as json_data:
        json.dump(data, json_data, ensure_ascii=False)


create_json()

with open(json_file, "r", encoding="utf-8") as json_data:
    print(json_data.read())

os.remove(json_file)

"""
Extra

Utilizando la lógica de creación de los archivos anteriores, crea un
programa capaz de leer y transformar en una misma clase custom de tu 
lenguaje los datos almacenados en el XML y el JSON.
Borra los archivos.
"""

create_xml()
create_json()

class Data:

    def __init__(self, name, age, birth_date, programming_languages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages


with open(xml_file, "r", encoding="utf-8") as xml_data:    

    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    xml_class = Data(name, age, birth_date, programming_languages)
    print(xml_class.__dict__)


with open(json_file, "r", encoding="utf-8") as json_data:   
    json_dict = json.load(json_data)
    json_class = Data(
        json_dict["name"], 
        json_dict["age"], 
        json_dict["birth_date"], 
        json_dict["programming_languages"]
    )
    print(json_class.__dict__)


os.remove(xml_file)
os.remove(json_file)