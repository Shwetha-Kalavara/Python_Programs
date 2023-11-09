def sample(a, b):
    yield a + b
    yield a


res = sample(1, 2)      # generator object
print(res)
# print(list(res))
print(next(res))
print(next(res))
print(next(res))
