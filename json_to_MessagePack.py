import json
import msgpack

# this def read json file
def load_json(path):
  with open(path) as f:
    data = json.load(f)

  return data 

# this def write messagepack file
def seve_messagepack(data, path = "data.msgpack"):
  with open(path, "wb") as outfile:
      outfile.write(data)


# this def covert json to  messagepack
def json_to_messagepack(data):
  return msgpack.packb(data)
  

if __name__ == '__main__':

  data = load_json('data1.json')
  messagepack =  json_to_messagepack(data)
  print(messagepack)
  seve_messagepack(messagepack)



