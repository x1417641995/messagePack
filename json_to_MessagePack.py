

import json
import msgpack


with open('data1.json') as f:
  data = json.load(f)

#print(data)
a = msgpack.packb({
  "a" : 0
})

j = {
  "squadname": "super hero squad"
}

aa = {
  "a" : 0
}

ma = msgpack.packb(j)

mp = msgpack.dumps(j, use_bin_type=True)

print(ma)
print(mp)
print(len(mp))
up = msgpack.unpackb(mp)
print(up)


# for i in mp:
#     print(i)

