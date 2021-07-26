import pickle

d = {
    "name": "cyl",
    "age": 18,
    "score": 99
}
print(pickle.dumps(d))  # 序列化某个变量，返回序列化后的值

# 用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
f = open("1.txt", "wb")  # 以二进制写入方式打开1.txt
pickle.dump(d, f)
f.close()
# 用反序列方法pickle.load()把文件的内容进行反序列
f = open("1.txt", "rb")  # 以二进制读取方式打开1.txt
string = pickle.load(f)
print(string)
f.close()
