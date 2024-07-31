#pip install python-consul
import os
import json
from consul import Consul

CONSUL_ADDRESS = "localhost"  
CONSUL_PORT = 8500 
OUTPUT_DIRECTORY = "example-copy"  

def get_keys_from_consul(prefix=''):
    consul = Consul(host=CONSUL_ADDRESS, port=CONSUL_PORT)
    keys = []
    
    index, entries = consul.kv.get(prefix, recurse=True)
    if entries:
        for entry in entries:
            keys.append(entry['Key'])
    return keys

def fetch_and_save_json(key):
    consul = Consul(host=CONSUL_ADDRESS, port=CONSUL_PORT)
    index, response = consul.kv.get(key)
    if response and 'Value' in response:
        json_string = response['Value']
        json_content = json.loads(json_string.decode('utf-8'))
        
        output_path = os.path.join(OUTPUT_DIRECTORY, key)
        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path))
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(json_content, f, indent=4)
        
        print(f"Saved {key} to {output_path}")
    else:
        print(f"Failed to retrieve data for key {key}")

def main():
    # Optionally, set a prefix if you want to fetch keys under a specific path
    prefix = '' #subfolder
    keys = get_keys_from_consul(prefix)
    for key in keys:
        fetch_and_save_json(key)

if __name__ == "__main__":
    main()