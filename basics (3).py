# python - json --> serialization/ marshalling
# json - python --> deserialization/ unmarshalling

import json
# serialization

data = {"name": "abc", "id": 20}
x = json.dumps(data)
print(x, type(x))

# desrialization
y = json.loads(x)
print(y, type(y))

####################################################################

with open("sample.json", "w+") as file:
    json.dump(data, file)
    # json.dump([1, 2, 3, 4], file)
    file.seek(0)
    data = json.load(file)
    print(data)

# with open("sample.json") as file:
#     data = json.load(file)
#     print(data)

















