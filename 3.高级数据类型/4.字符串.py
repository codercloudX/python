# 1.字符串定义和遍历
str1 = "hello python"
str2 = '我的外号是"大西瓜"'

print(str2)
print(str1[5])#从0开始

for i in str2:
    print(i)
print()

# 2.字符串统计
print(len(str1))
print(str1.count("hello"))#统计某个词或者某个字符出现的次数
print(str1.index("python"))#统计某个词或者某个字符第一次出现的位置,如果使用index方法传递的子字符串不存在，程序会报错！
print()

# 3.字符串判断方法
space_str=" "
print(space_str.isspace())

# 4.查找对应字符串
print(str1.find("llo"))#如果没有，返回-1;有则返回该字符串第一次出现的位置
print()

# 5.替换
print(str1.replace("python","world"))#返回一个字符串，不会改变原来的字符串
print()

# 6.字符串文本对齐
poem = ["\t\n登鹳雀楼",
         "王之涣",
         "白日依山尽\t\n",
         "黄河入海流",
         "欲穷千里目",
         "更上一层楼"]

for poem_str in poem:
    print("|%s|" % poem_str.strip().center(10, "　"))
    # 先使用strip方法去除字符串中的空白字符
    # 再使用center方法居中显示文本
print()
    
# 7.拆分字符串
poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t\t\n更上一层楼"
print(poem_str)
poem_list = poem_str.split()
print(poem_list)# 1. 拆分字符串
result = " ".join(poem_list)
print(result)# 2. 合并字符串
print()