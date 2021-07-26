# messagePack
 
 this transfer using msgpack.  
 If you do not install msgpack, you can use  
```
$ pip install msgpack
```

### How to use  
* json_to_MessagePack 
  
  run `json_to_MessagePack.py`  
  load data1.json covert to messagePack and save as data.msgpack  

* MessagePack_to_json
  
  run `MessagePack_to_json.py`  
  load data.msgpack covert to json and save as savedata.json
  
### How to use without msgpack
* to_msg 
  
  run `json_to_MessagePack.py`  
  load data1.json covert to messagePack and return bytes by messagepack format without using msgpack
