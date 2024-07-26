import yaml
import json

with open(r"C:/Users/white/OneDrive/Documents/Untitled-3.yaml", 'r') as stream:
    try:
        yaml_data = stream.read()
    except yaml.YAMLError as exc:
        print(exc)

parsed_data = yaml.safe_load(yaml_data)

def convert_json_to_yaml(json_str):
    # Load JSON data
    json_data = json.loads(json_str)

    # Convert JSON to YAML
    yaml_data = yaml.dump(json_data, sort_keys=False)
    return yaml_data

with open(r"C:/Users/white/OneDrive/Documents/Untitled-3.json", 'w') as stream:
    try:
        stream.write(json.dumps(parsed_data, indent=2))
    except yaml.YAMLError as exc:
        print(exc)
parsed_data = parsed_data[0]
print(parsed_data.keys())

def fixChildren(data):
    for key in data.keys():
        print(key)
        if "Children" in data[key]:
            for child in data[key]["Children"]:
                fixChildren(child)
        
        if data[key]['Control'] == "Classic/TextInput":
            data[key]['Control'] = "TextInput"
            data[key]['Properties']['Value'] = data[key]['Properties']['Default']
            data[key]['Properties']['Width'] = "=Parent.Width - 60"
            data[key]['Properties']['TriggerOutput'] = "='TextInputCanvas.TriggerOutput'.Delayed"
            if 'Mode' in data[key]['Properties'] and data[key]['Properties']['Mode'] == "=TextMode.MultiLine":
                data[key]['Properties']['Mode'] = "='TextInputCanvas.Mode'.Multiline"
            else:
                data[key]['Properties']['Mode'] = "='TextInputCanvas.Mode'.SingleLine"
        if data[key]['Control'] == "Classic/Icon":
            data[key]['Properties']['Color'] = data[key]['Properties']['Color'].replace('RGBA(236, 0, 140, 1)','ColorValue("#012169")')
            data[key]['Properties']['X'] = "=Parent.Width-30-Self.Width"
        

fixChildren(parsed_data)
fixedarray = []
fixedarray.append(parsed_data)
yaml_data = convert_json_to_yaml(json.dumps(fixedarray, indent=2))
with open(r"C:/Users/white/OneDrive/Documents/Untitled-4.yaml", 'w') as stream:
    try:
        stream.write(yaml_data)
    except yaml.YAMLError as exc:
        print(exc)
    

