#pip install requests
import os
import requests
import json
from base64 import b64encode

CONSUL_ADDRESS = "http://localhost:8500/v1/kv" 
ROOT_DIRECTORY = "./example"

def import_json_files(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                key = file_path.replace(ROOT_DIRECTORY, "").replace(os.sep, "/").lstrip("/")
                with open(file_path, 'r', encoding='utf-8') as f:
                    json_content = json.load(f)
                json_string = json.dumps(json_content)
                # encoded_value = b64encode(json_string.encode('utf-8')).decode('utf-8')
                # response = requests.put(f"{CONSUL_ADDRESS}/{key}", data=encoded_value)
                response = requests.put(f"{CONSUL_ADDRESS}/{key}", data=json_string)
                print(f"Imported {key}: {response.status_code}")

if __name__ == "__main__":
    import_json_files(ROOT_DIRECTORY)