import json

def load_json(file_path):
   
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json(file_path, data):
  
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def update_data(file_path, new_entry):
   
    data = load_json(file_path)

    if isinstance(data, list):
        data.append(new_entry)
    else:
        print("Error: JSON data list nahi hai.")
        return

    save_json(file_path, data)

file_path = "data.json"
new_data = {"name": "Ali", "age": 30, "city": "Lahore"}
update_data(file_path, new_data)

print("Data JSON file me successfully update ho gaya hai!")
