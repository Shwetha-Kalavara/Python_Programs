import pickle

# serialization
data = "hello"
x = pickle.dumps(data)
print(x, type(x))

# de-serialization
y = pickle.loads(x)
print(y, type(y))

#############################################################

with open("example.pkl", "wb+") as file:
    pickle.dump(data, file)
    file.seek(0)
    data = pickle.load(file)
    print(data)









