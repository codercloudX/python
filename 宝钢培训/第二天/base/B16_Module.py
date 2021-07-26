import base.B16_1_ModuleReload as b16
import importlib

'''
reload可以在服务器不重启服务的时候重新加载模块
这样当有部分功能覆盖时可以调用reload加载新的覆盖功能而无需重新停开服务
'''
importlib.reload(b16)
print(b16.message)
print(b16.printer())


'''
要导入包中的模块，包中必须包括__init__.py，否则导入包会失败
pycharm已经自动帮我们完成了
'''

'''
模块的内置属性__name__经常用来单元测试
本类调用显示__main__
被其他类调用显示类名
1.在B16_1_ModuleReload.py中添加
def printerOther():
    print("被调用的测试类="+__name__)

if __name__=="__main__":
    printerOther()
2.运行B16_1_ModuleReload.py，显示'被调用的测试类=__main__'
3.在B16_Module.py引入B16_1_ModuleReload.py
import base.B16_1_ModuleReload as b16
4.调用print(b16.printerOther())，显示'被调用的测试类=base.B16_1_ModuleReload'
'''
print(b16.printerOther())