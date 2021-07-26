import pickle

tuple0 = (1, 2, 3, 4, 5)

with open('tuple.txt', 'wb') as f:
    pickle.dump(tuple0, f)

with open('tuple.txt', 'rb') as f:
    tuple1 = pickle.load(f)

print(tuple1)
