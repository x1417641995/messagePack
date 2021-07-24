import struct

def type_check(msg, data):
    if(type(data) == list):
        list_transform(msg, data)
        #return msg
    if(type(data) == dict):
        msg.extend(dict_transform(msg, data))
        #return msg
    if(type(data) == str):
        str_transform(msg, data)
        #return msg
    if(type(data) == int):
        int_transform(msg, data)
    if(type(data) == bool):
        bool_transform(msg, data)

    if(type(data) == float):
        float_transform(msg, data)
    if(data is None):
        msg.extend(bytearray([0xc0]))

def str_transform(msg, data):
    strlength = 0xa0 + len(data)
    msg.extend(bytearray([strlength]))
    msg.extend(str.encode(data))

def list_transform(msg, data):
    listlength = 0x90 + len(data)
    msg.extend(bytearray([listlength]))
    for i in data:
        type_check(msg, i)

def dict_transform(msg, data):
    dictlength = 0x80 + len(data)
    msg = bytearray([dictlength])
    for key, value in data.items():
        type_check(msg, key)
        type_check(msg, value)
    return  msg

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

def bool_transform(msg, data):
    if(data == True):
        msg.extend(bytearray([0xc3]))
    if(data == False): 
        msg.extend(bytearray([0xc2]))

def float_transform(msg, data):
    # python float 32
    msg.extend(struct.pack(">Bd", 0xCB, data))



def json_to_msg(data):
    
    l = len(data)
    a = 0x80 + l-1
    dictlength = 0x80 + len(data)
    
    msg = bytearray()#bytearray([dictlength])
    print(msg)
    print(type(data))
    type_check(msg, data)
    # for key, value in data.items():
    #     type_check(msg, key)
    #     type_check(msg, value)
    #     print(4)
    
    '''
    for key, value in data.items():
        print(key, value)
        strlength = 0xa0 + len(key)
        #a = str.encode(key)

        # key transform
        msg.extend(bytearray([strlength]))
        msg.extend(str.encode(key))
        #
        print(type(value))
        if(type(value) == str):
            strlength = 0xa0 + len(value)
            msg.extend(bytearray([strlength]))
            msg.extend(str.encode(value))
        if(type(value) == list):
            listlength = 0x90 + len(value)
            msg.extend(bytearray([listlength]))
            for i in value:
                if(type(i) == str):
                    strlength = 0xa0 + len(i)
                    msg.extend(bytearray([strlength]))
                    msg.extend(str.encode(i))
            #msg.extend(str.encode(value))
    '''    
    
    print(msg)
    print(bytes(msg))    


data = {
    "number":None,#128*2,
    "languages":"dfgd56444444444444444444444fdgdfgdfgdgfdgvvvscescescsevsvevvfsdvdfsvsfdsvdfvsdfvfvfsdvfsdfvds444",
    # "bool": True,
    # "bool3": False,
    # "name": "Bob", 
    # "languages": ["English", "Fench"],
    # "meta":{
    #     "type":"2",
    #     "f":"abc"
    # }
}
# data = {
#   "error_no":0,
#   "message":"",
#   "result":{
#     "data":[
#       {
#         "datatype":1,
#         "itemdata":
#             {
#               "sname":"\u5fae\u533b",
#               "packageid":"330611",
#               "tabs":[
#                         {
#                           "type":1,
#                           "f":"abc"
#                         },
#               ]
#             }
#       },

#     ],
#     "hasNextPage":True,
#     "dirtag":"soft"
#   }
# }


#json_to_msg(data)


def json_to_messagepack(data):
    import msgpack
    return msgpack.packb(data)

print(json_to_messagepack(data))
print(0x7f)
