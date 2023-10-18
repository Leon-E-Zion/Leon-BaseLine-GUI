import json

# 1. 存储字典到JSON文件
def save_dict_to_json(data, file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {str(e)}")

# 2. 从JSON文件读取字典
def load_dict_from_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found. Returning an empty dictionary.")
        return {}
    except Exception as e:
        print(f"Error loading data from {file_path}: {str(e)}")
        return {}

# 示例用法
if __name__ == "__main__":
    # 1. 存储字典到JSON文件
    sample_data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    json_file_path = "sample_data.json"
    save_dict_to_json(sample_data, json_file_path)
    
    # 2. 从JSON文件读取字典
    loaded_data = load_dict_from_json(json_file_path)
    print("Loaded Data:", loaded_data)
