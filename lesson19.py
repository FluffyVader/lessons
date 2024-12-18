import json

dictionary = {"name": "Vova", "Age": 64, "birthYear": 2014}
my_list = [37,"weather", dictionary]

json_text = json.dumps(dictionary)
print(json_text)

json_list_text = json.dumps(my_list)
print(my_list)

with open("file.json","wt") as file_json:
    file_json.write(json_text)
    
with open("file_list.json","wt") as file_list_json:
    file_list_json.write(json_list_text)