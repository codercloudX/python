class record:
    ipAddr = ""
    serverName = ""
    serverType = ""
    myData = []

    def __init__(self, ipAddr, serverName, serverType, myData):
        self.ipAddr = ipAddr
        self.serverName = serverName
        self.serverType = serverType
        self.myData = myData

    def print(self):
        print("ip地址：", end='')
        print(self.ipAddr)
        print("服务器名称：", end='')
        print(self.serverName)
        print("服务器类型：", end='')
        print(self.serverType)
        print("需要的数据：", end='')
        print(self.myData)
        print("\n")

    def ToString(self):
        strin = "ip地址：" + self.ipAddr \
                + "\n服务器名称：" + self.serverName \
                + "\n服务器类型：" + self.serverType + \
                "\n需要的数据："
        strin += "[ "
        for i in range(0, len(self.myData)):
            strin += self.myData[i]
            if i != len(self.myData)-1:
                strin += ","
        strin += " ]\n\n"
        return strin
