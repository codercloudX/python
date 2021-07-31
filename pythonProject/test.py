import time


def timeTransform(beginTime, endTime, selectTime):
    beginTime = beginTime.replace(" ", "%20")
    endTime = endTime.replace(" ", "%20")
    selectTime = str(selectTime)
    url = "&beginTime=" + beginTime + "&endTime=" + endTime + "&selectTime=" + selectTime + "_hours"
    return url


if __name__ == '__main__':
    localtime = str(time.localtime(time.time()).tm_year)+"-"+str(time.localtime(time.time()).tm_mon)+"-"+str(time.localtime(time.time()).tm_mday)
    print(localtime)