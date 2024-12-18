import json

with open("file.json","rt") as file_json:
    json_read_file = file_json.read()

dictionary = json.loads(json_read_file)

print(dictionary["Age"])

#####
with open("file_list.json") as readonly_file_list_json:
    content_of_file_list_json = readonly_file_list_json.read()

deserialized_content_of_file_list_json = json.loads(content_of_file_list_json)
print(deserialized_content_of_file_list_json[0])