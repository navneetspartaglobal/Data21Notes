import json

pet_data = {"name": "Bob", "food": "carrots"}


with open("new_json_file", "w") as jsonfile:
    json.dump(pet_data, jsonfile)


with open("new_json_file.json", "w") as jsonfile:
    pet = json.load(jsonfile)
    print(type(pet))
    print(pet)

# print(pet_data)
# print(type(pet_data))
# # serializes the json into string
# pet_data_json_str = json.dumps(pet_data)
#
# print(pet_data_json_str)
# print(type(pet_data_json_str))
