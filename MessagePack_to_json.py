import json
import msgpack

# this def write json file
def save_json(data, path = 'savedata.json'):
    with open(path, 'w') as f:
        json.dump(data, f)

def load_messagepack():
    with open("data.msgpack", "rb") as data_file:
        byte_data = data_file.read()
    return byte_data

# this def covert messagepack to json   
def messagepack_to_json(data):
    return msgpack.unpackb(data)
  

if __name__ == '__main__':

  data = load_messagepack()#b'\x82\xa4name\xa3Bob\xa9languages\x92\xa7English\xa5Fench'
  messagepack =  messagepack_to_json(data)
  save_json(messagepack)
  print(messagepack)