import requests
import wiget
import utils
from bs4 import BeautifulSoup
from record import record


# 页面类
class data:
    id = 0
    name = ""  # 资源名称
    templateId = 0  # 页号
    dataArray = []  # 数据

    def __init__(self, id, name, templateId, dataArray):
        self.id = id
        self.name = name
        self.templateId = templateId
        self.dataArray = dataArray

    def getInformation(self, t, jID):
        url = "http://10.99.69.229:8082/oceanserver/report/topNReport.do?method=search&menuId=7&menuider=b77&templateId=" \
              + str(self.templateId) \
              + "&TopN=10" \
              + str(t) \
              + "&sortType=desc"

        htmlTxt = self.getHtml(url, jID)  # 获取页面的html
        columns = self.getTable(htmlTxt)  # 获取表格

        if len(self.dataArray) <= 0:
            return False
        tableData = []
        i = 2
        for i in range(i, len(columns)):
            newRecord = record("", "", "", [])
            # 当页面为CPU时，执行以下逻辑
            if self.id == 1:
                newRecord.ipAddr = columns[i].select("td")[self.dataArray[0]].get_text()
                newRecord.serverType = columns[i].select("td")[self.dataArray[1]].get_text()
                newRecord.serverName = columns[i].select("td")[self.dataArray[2]].get_text()
                newRecord.myData = [columns[i].select("td")[self.dataArray[3]].get_text(),
                                    columns[i].select("td")[self.dataArray[4]].get_text(),
                                    columns[i].select("td")[self.dataArray[5]].get_text()]
            # 当页面为内存时，执行以下逻辑
            elif self.id == 2:
                newRecord.ipAddr = columns[i].select("td")[self.dataArray[0]].get_text()
                newRecord.serverType = columns[i].select("td")[self.dataArray[1]].get_text()
                newRecord.serverName = columns[i].select("td")[self.dataArray[2]].get_text()
                newRecord.myData = [columns[i].select("td")[self.dataArray[3]].get_text(),
                                    columns[i].select("td")[self.dataArray[4]].get_text()]
            # 当页面为磁盘时，执行以下逻辑
            elif self.id == 3:
                newRecord.ipAddr = columns[i].select("td")[self.dataArray[0]].get_text()
                newRecord.serverType = columns[i].select("td")[self.dataArray[1]].get_text()
                newRecord.serverName = columns[i].select("td")[self.dataArray[2]].get_text()
                newRecord.myData = [columns[i].select("td")[self.dataArray[3]].get_text(),
                                    columns[i].select("td")[self.dataArray[4]].get_text()]
            # 当页面为linux负载时，执行以下逻辑
            elif self.id == 4:
                newRecord.ipAddr = columns[i].select("td")[self.dataArray[0]].get_text()
                newRecord.serverType = columns[i].select("td")[self.dataArray[1]].get_text()
                newRecord.serverName = columns[i].select("td")[self.dataArray[2]].get_text()
                newRecord.myData = [columns[i].select("td")[self.dataArray[3]].get_text(),
                                    columns[i].select("td")[self.dataArray[4]].get_text(),
                                    columns[i].select("td")[self.dataArray[5]].get_text()]
            # 当页面为数据库大小增长Top时，执行以下逻辑
            elif self.id == 5:
                newRecord.ipAddr = columns[i].select("td")[self.dataArray[0]].get_text()
                newRecord.serverType = columns[i].select("td")[self.dataArray[1]].get_text()
                newRecord.serverName = columns[i].select("td")[self.dataArray[2]].get_text()
                newRecord.myData = [columns[i].select("td")[self.dataArray[3]].get_text(),
                                    columns[i].select("td")[self.dataArray[4]].get_text()]
            # 当页面为表空间数据增长Top时，执行以下逻辑
            elif self.id == 6:
                newRecord.ipAddr = columns[i].select("td")[self.dataArray[0]].get_text()
                newRecord.serverType = columns[i].select("td")[self.dataArray[1]].get_text()
                newRecord.serverName = columns[i].select("td")[self.dataArray[2]].get_text()
                newRecord.myData = [columns[i].select("td")[self.dataArray[3]].get_text(),
                                    columns[i].select("td")[self.dataArray[4]].get_text()]
            # 当页面为表空间数据使用率Top时，执行以下逻辑
            elif self.id == 7:
                newRecord.ipAddr = columns[i].select("td")[self.dataArray[0]].get_text()
                newRecord.serverType = columns[i].select("td")[self.dataArray[1]].get_text()
                newRecord.serverName = columns[i].select("td")[self.dataArray[2]].get_text()
                newRecord.myData = [columns[i].select("td")[self.dataArray[3]].get_text(),
                                    columns[i].select("td")[self.dataArray[4]].get_text()]

            tableData.append(newRecord)

        return tableData

    # 获取整个网页的html代码
    def getHtml(self, checkurl, jID):
        # 1.cehchurl是要访问表格所在的页面
        # checkurl = "http://10.99.69.229:8082/oceanserver/report/topNReport.do?method=search&menuId=7&menuider=b77&templateId=7&TopN=10&beginTime=2021-05-04%2020:24:07&endTime=2021-05-05%2000:24:07&selectTime=4_hours&sortType=desc"

        # 2. payload是访问页面时需要发送的：用户名，密码和验证码
        # 如果有JsessionId，则无需用户名和密码也可以登录，
        payload = {

        }

        # 3.header是访问页面时需要发送的头部信息，jession也在里面，很重要
        # 每次的JsessionID不一样；
        # 如果不输入headers返回的是登录界面
        headers = {
            "Host": "10.99.69.229:8082",
            "Connection": "keep-alive",
            "Content-Length": "61",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "http://10.99.69.229:8082",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 "
                          "Safari/537.36 Edg/90.0.818.49",
            "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                      'application/signed-exchange;v=b3;q=0.9',
            "Referer": "http://10.99.69.229:8082/oceanserver/index.do?method=index&menuId=1",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cookie": "JSESSIONID=" + str(jID) + "; nmsUserName=admin; nmsPassword=empndDIwMjE=",
        }

        html = requests.post(checkurl,
                             json=payload,
                             headers=headers,
                             verify=False)
        if html == {}:
            print("无法获取网页！")
            return False

        return html.text

    # 获取需要获取的元素的html代码
    def getTable(self, htmlTxt):
        if not htmlTxt:
            return False
        soup = BeautifulSoup(htmlTxt, 'lxml').select("body div.ruanjian_index .jq_table")[0]
        if len(soup) is None:
            return False

        columns = soup.select("tr")

        return columns

    # 点击事件：将获取的数据做处理;
    def save_OnClick(self, event):
        utils.jSessionID = utils.jIdInput.GetValue()

        utils.beginTime = utils.startDateInput.GetValue().FormatISODate() + " " + utils.startTimeInput.GetValue().FormatISOTime()
        utils.endTime = utils.endDateInput.GetValue().FormatISODate() + " " + utils.endTimeInput.GetValue().FormatISOTime()
        utils.selectTime = utils.selectTimeInput.GetValue()

        utils.time = utils.timeTransform(utils.beginTime, utils.endTime, utils.selectTime)

        if utils.jSessionID == "":
            s = "请输入正确的jSessionID！"
            wiget.mainFrame.Children[wiget.findPanel("bigTextBox")].SetValue(s)
            return False

        d = self.getInformation(utils.time, utils.jSessionID)  # 获取数据
        s = ""
        for i in range(0, len(d)):
            s += d[i].ToString()
        wiget.mainFrame.Children[wiget.findPanel("bigTextBox")].SetValue(s)
