'''
name:第二天作业
author ：cloud
time:2021-07-24
'''

'''
1.用while循环语法计算1+2+....+100的基数结果和偶数结果
2.定义函数catchError(),该函数方法打印指定序列mlist的值，mlist序列包括值: jack,18,178三个值，
在catchError()函数中试图获取mlist的第4个值，
由于边界越界抛出打印'序列边界越界'字样，其他错误全部不报错，
退出函数时无论序列是否边界越界，都会打印"捕捉异常结束"。
'''


# 定义奇数/偶数和
def getSumOfOddAndEve():
    odd = eve = 0
    i = 0
    while i <= 100:
        if i % 2 == 0:
            eve += i
        else:
            odd += i
        i += 1
    return odd, eve


def catchError(mylist, index):
    try:
        print(mylist[index])
    except IndexError:
        print("序列边界越界")
    finally:
        print("捕捉异常结束")


if __name__ == '__main__':
    print("1：用while循环语法计算1+2+....+100的基数结果和偶数结果")
    print("奇数和=" + str(getSumOfOddAndEve()[0]))
    print("奇数和=" + str(getSumOfOddAndEve()[1]))
    print("\n")
    print("2：列表访问越界检测")
    mlist = ['jack', 18, 178]
    catchError(mlist, 4)
