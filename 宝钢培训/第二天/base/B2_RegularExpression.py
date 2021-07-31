import re # 正则表达式

'''搜索'''
# 正则表达式知识大全参见《正则表达式.pptx》
pattern="([0-9]*)([a-z]*)([0-9]*)"
txt="123abc456"
mathResult=re.match(pattern,txt).group(0) # 等同于group()找到整个匹配字符串
print(mathResult)
mathResult=re.match(pattern,txt).group(1) # 找到第1个匹配值 123
print(mathResult)
mathResult=re.match(pattern,txt).group(2) # 找到第2个匹配值 abc
print(mathResult)
mathResult=re.match(pattern,txt).group(3) # 找到第3个匹配值 456
print(mathResult)
mathResult=re.match(pattern,txt).groups() # 找到所有组匹配值 ('123', 'abc', '456')
print(mathResult)
'''
pattern="/(.*)/(.*)/(.*)" # 正则表达式搜索3个斜杠中间的任意字符
txt="/usr/home/jack"
mathResult=re.match(pattern,txt).groups() # 找到所有组匹配值 ('usr', 'home', 'jack')
print(mathResult)
'''