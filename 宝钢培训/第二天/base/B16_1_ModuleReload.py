message="hello msg"

def printer():
    print(message)

def printerOther():
    print("被调用的测试类="+__name__)

'''
模块的内置属性__name__经常用来单元测试
本类调用显示__main__
被其他类调用显示类名
'''
if __name__=="__main__":
    printerOther()