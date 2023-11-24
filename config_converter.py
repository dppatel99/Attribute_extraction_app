import json

config = "config_ethos.json"
with open(config, 'r') as json_file:
    config_data = json.load(json_file)
output_json = {}
for attribute_dict in config_data["prompt"]["attributes"]:
  attribute_name = attribute_dict["name"]
  attribute_desc = attribute_dict["description"]
  if "options" in attribute_dict:
    attribute_options = attribute_dict["options"]
    attribute_desc += f"\nOptions:\n{','.join(attribute_options)}"
  output_json[attribute_name] = attribute_desc
config_data["prompt"]["attributes"] = [json.dumps(output_json, indent=4)]
with open("testop.json", 'w') as json_file:
    json.dump(config_data, json_file, indent=2)