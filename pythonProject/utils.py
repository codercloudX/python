from data import data

# 公有变量
jSessionID = "F504E990B316FA5D6CA6B212E1CEEED7"
beginTime = "2021-06-03 02:30:00"
endTime = "2021-06-03 08:30:00"
selectTime = 6
time: ""

# 页面元素
jIdInput = {}
startDateInput = {}
startTimeInput = {}
endDateInput = {}
endTimeInput = {}
selectTimeInput = {}
bigTextBox = {}


# 将选择的时间转成字符串，拼接到url里
def timeTransform(beginTime, endTime, selectTime):
    if endTime == "":
        endTime = "undefined"
    if selectTime == "":
        selectTime = "undefined"
    beginTime = str(beginTime).replace(" ", "%20")
    endTime = str(endTime).replace(" ", "%20")
    selectTime = str(selectTime)

    if selectTime == "undefined":
        url = "&beginTime=" + beginTime + "&endTime=" + endTime + "&selectTime=" + selectTime
    else:
        url = "&beginTime=" + beginTime + "&endTime=" + endTime + "&selectTime=" + selectTime + "_hours"

    return url
