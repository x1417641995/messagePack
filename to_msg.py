import struct
import json

# this def check the data type
def type_check(msg, data):
    if(type(data) == list):
        list_transform(msg, data)
    if(type(data) == dict):
        dict_transform(msg, data)
    if(type(data) == str):
        str_transform(msg, data)
    if(type(data) == int):
        int_transform(msg, data)
    if(type(data) == bool):
        bool_transform(msg, data)
    if(type(data) == float):
        float_transform(msg, data)
    if(data is None):
        msg.extend(bytearray([0xc0]))

# this def transform str to messagepack
def str_transform(msg, data):
    if(len(data) <= 0x1F):
        strlength = 0xa0 + len(data)
        msg.extend(bytearray([strlength]))
        msg.extend(str.encode(data))
    elif(len(data) <= 0xFF):
        msg.extend(struct.pack(">BB", 0xD9, len(data)))
        msg.extend(bytearray(data, "utf8"))  
    elif(len(data) <= 0xFFFF):
        msg.extend(struct.pack(">BH", 0xDA, len(data)))
        msg.extend(bytearray(data, "utf8"))
    elif(len(data) <= 0xFFFFFFFF):
        msg.extend(struct.pack(">BI", 0xDB, len(data)))
        msg.extend(bytearray(data, "utf8"))

# this def transform list to messagepack
def list_transform(msg, data):
    if len(data) <= 0x0F:
        listlength = 0x90 + len(data)
        msg.extend(bytearray([listlength]))
    elif len(data) <= 0xFFFF:
        msg.extend(struct.pack(">BH", 0xDC, len(data)))
    elif len(data) <= 0xFFFFFFFF:
        msg.extend(struct.pack(">BI", 0xDD, len(data)))

    for i in data:
        type_check(msg, i)
    

# this def transform dict to messagepack
def dict_transform(msg, data):
    if (len(data) <= 0x0F):
        dictlength = 0x80 + len(data)
        msg.extend(bytearray([dictlength]))
    elif (len(data) <= 0xFFFF):
        msg.extend(struct.pack(">BH", 0xDE, len(data)))
    elif (len(data) <= 0xFFFFFFFF):
        msg.extend(struct.pack(">BI", 0xDF, len(data)))

    for key, value in data.items():
        type_check(msg, key)
        type_check(msg, value)

# this def transform int to messagepack
def int_transform(msg, data):
    if 0 <= data < 0x80:
        msg.extend(struct.pack("B", data))
    if -0x20 <= data < 0:
        msg.extend(struct.pack("b", data))
    if 0x80 <= data <= 0xFF:
        msg.extend(struct.pack("BB", 0xCC, data))
    if -0x80 <= data < 0:
        msg.extend(struct.pack(">Bb", 0xD0, data))
    if 0xFF < data <= 0xFFFF:
        msg.extend(struct.pack(">BH", 0xCD, data))
    if -0x8000 <= data < -0x80:
        msg.extend(struct.pack(">Bh", 0xD1, data))
    if 0xFFFF < data <= 0xFFFFFFFF:
        msg.extend(struct.pack(">BI", 0xCE, data))
    if -0x80000000 <= data < -0x8000:
        msg.extend(struct.pack(">Bi", 0xD2, data))
    if 0xFFFFFFFF < data <= 0xFFFFFFFFFFFFFFFF:
        msg.extend(struct.pack(">BQ", 0xCF, data))
    if -0x8000000000000000 <= data < -0x80000000:
        msg.extend(struct.pack(">Bq", 0xD3, data))

# this def transform bool to messagepack
def bool_transform(msg, data):
    if(data == True):
        msg.extend(bytearray([0xc3]))
    if(data == False): 
        msg.extend(bytearray([0xc2]))

# this def transform float to messagepack
def float_transform(msg, data):
    # python float 32
    msg.extend(struct.pack(">Bd", 0xCB, data))

# this def covert messagepack to json
def json_to_msg(data):  
    msg = bytearray()
    type_check(msg, data)
    return bytes(msg) 

# this def read json file
def load_json(path):
    with open(path) as f:
        data = json.load(f)

    return data  


if __name__ == '__main__':

    data = {
        "error_no":0,
        "message":"",
        "result":{
            "data":[
            {
                "datatype":1,
                "itemdata":
                    {
                    "sname":"\u5fae\u533b",
                    "packageid":"330611",
                    "tabs":[
                                {
                                "type":1,
                                "f":"abc"
                                },
                    ]
                    }
            },

            ],
            "hasNextPage":True,
            "dirtag":"soft"
        },
    }
    #data = load_json('data1.json')
    messagepack =  json_to_msg(data)
    print(messagepack)