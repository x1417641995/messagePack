import json
import msgpack

def load_json(path):

  with open(path) as f:
    data = json.load(f)

  return data 

def json_to_messagepack(data):
  return msgpack.packb(data)
  

if __name__ == '__main__':
  
  data = load_json('data1.json')
  messagepack =  json_to_messagepack(data)
  print(messagepack)


