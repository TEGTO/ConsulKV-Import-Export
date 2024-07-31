# ConsulKV Import-Export
 Python scripts for importing and exporting json keys in Consul KV

## Import to KV
**INSTALL**
```
pip install requests
```
**SET**
```
CONSUL_ADDRESS 
ROOT_DIRECTORY
```
**RUN**
```
python consul-put.py
```
## Export from KV
**INSTALL**
```
pip install python-consul
```
**SET**
```
CONSUL_ADDRESS
CONSUL_PORT 
OUTPUT_DIRECTORY
```
**RUN**
```
python consul-get.py
```
