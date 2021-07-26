import sys

# 1.dir函数：抓取对象内可用所有属性列表
print(dir(sys)) # 抓取sys对象的属性
print(dir([])) # 抓取序列对象的属性

# 2.__doc__文档字符串
'''
除了#注释外，Python也支持可自动附加在对象上的文档，而且在运行时还可保存查看。
这类注释是写成字符串，放在模块文件、函数以及类语句的顶端
。python会自动封装这个字符串，也就是成为所谓的文档字符串，使其成为相应对象的__doc__属埤
'''
def square(x):
        '''
        :param x: 传入的整数
        :return: 返回平方数
        '''
        return x**2
class other:
        '''其他辅助类'''
        pass
print(square(4))
print(square.__doc__)
print(other.__doc__)

# 3.help函数
'''
getrefcount(...)
    getrefcount(object) -> integer
    
    Return the reference count of object.  The count returned is generally
    one higher than you might expect, because it includes the (temporary)
    reference as an argument to getrefcount().
'''
print(help(sys.getrefcount))

# 4.pydoc查看文档工具--参见ppt分析

