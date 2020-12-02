import os
# print(os.path.abspath('.'))
# direction=os.path.join(os.path.abspath('.'), '2.txt')
# # os.mkdir(direction)# 新建文件夹
# # os.rmdir(direction)# 删除文件夹
# print(os.path.split(direction))# 把路径分成目录+文件名模式，返回两个元素的字符串列表
# print(os.path.splitext(direction)[1])# 把路径分成目录文件名+文件拓展名模式，返回两个元素的字符串列表
# # os.rename("2.txt","1.txt")# 文件改名
# # os.remove("1.txt")# 删除文件

# 输出目录下的所有py文件
for x in os.listdir("."):
    if os.path.isfile(x) and os.path.splitext(x)[1]=='.py':
        print(x)