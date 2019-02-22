from PyQt5.Qt import *
import requests
import os
import json


class Config(object):
    @staticmethod
    def get_station_file_path():
        current_path = os.path.realpath(__file__)
        current_dir = os.path.split(current_path)[0]
        station_file_path = current_dir + r"\stations.json"
        return station_file_path

    @staticmethod
    def get_yzm_file_path():
        current_path = os.path.realpath(__file__)
        current_dir = os.path.split(current_path)[0]
        #print(current_dir)
        yzm_file_path = current_dir + r"\yzm.jpg"
        return yzm_file_path


class API(object):

    # 下载验证码 GET
    GET_YZM_URL = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"

    #answer: 58, 51, 249, 109, 167, 126
    #login_site: E
    #rand: sjrand
    # 验证码验证 POST
    CHECK_YZM_URL = "https://kyfw.12306.cn/passport/captcha/captcha-check"

    # 登录验证 POST
    CHECK_ACCOUNT_PWD = "https://kyfw.12306.cn/passport/web/login"

    # 问好信息 POST
    HELLO_URL = "https://kyfw.12306.cn/otn/index/initMy12306Api"

    # uamtk POST
    # appid : otn
    UAMTK_URL = "https://kyfw.12306.cn/passport/web/auth/uamtk"

    # author_client POST
    # tk :
    AUTHOR_URL = "https://kyfw.12306.cn/otn/uamauthclient"

    # 获取所有的城市站点 GET
    STATIONS_URL = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9093"

    # 查询车票 GET
    # leftTicketDTO.train_date: 2019-02-22
    # leftTicketDTO.from_station: SHH
    # leftTicketDTO.to_station: TJP
    # purpose_codes: ADULT
    QUERY_TICKETS_URL = "https://kyfw.12306.cn/otn/leftTicket/queryX"


class APITool(QObject):
    session = requests.session()

    @classmethod
    def download_yzm(cls):
        response = cls.session.get(API.GET_YZM_URL)
        #print(response.content)
        yzm_file_path = Config.get_yzm_file_path()
        with open(yzm_file_path, "wb") as f:
            f.write(response.content)

        #print(cls.session.cookies)

        return yzm_file_path

    @classmethod
    def check_yzm(cls, yzm):
        data_dic = {
            "answer": yzm,
            "login_site": "E",
            "rand": "sjrand"
        }
        response = cls.session.post(API.CHECK_YZM_URL, data=data_dic)

        dic = response.json()
        return dic["result_code"] == "4"

    @classmethod
    def check_account_pwd(cls, account, pwd):

        data_dic = {
            "username": account,
            "password": pwd,
            "appid": "otn"
        }
        response = cls.session.post(API.CHECK_ACCOUNT_PWD, data=data_dic)
        #dic = response.json()
        #print(dic)

        result_code = response.json()["result_code"]

        #print(cls.session.cookies)

        if result_code == 0:
            cls.author()
            return cls.get_hello()
        else:
            return None

        #cls.get_hello()

    @classmethod
    def author(cls):
        response = cls.session.post(API.UAMTK_URL, data={"appid" : "otn"})
        newapptk = response.json()["newapptk"]

        #print(response.text)
        #print(cls.session.cookies)

        response = cls.session.post(API.AUTHOR_URL, data={"tk" : newapptk})

        #print(response.text)
        #print(cls.session.cookies)

        #cls.get_hello()

    @classmethod
    def get_hello(cls):
        response = cls.session.post(API.HELLO_URL)
        dic = response.json()

        if dic["httpstatus"] == 200:
            return dic["data"]["user_name"] + dic["data"]["user_regard"]

        return None

    @staticmethod
    def get_all_stations():
        # 1 检查本地是否有该信息的缓存

            # 1.1 有 直接从本地加载
        if os.path.exists(Config.get_station_file_path()):
            print("读取缓存")
            with open(Config.get_station_file_path(), "r", encoding="utf-8") as f:
                stations = json.loads(f.read(), encoding="utf-8")
            #print(stations)
            return stations
        else:
            # 1.2 没有 从网络请求，并缓存到本地
            print("从网络请求")
            station_dic = {}
            response = requests.get(API.STATIONS_URL)
            #print(response.text)
            items =response.text.split("@")
            for item in items:
                station_list = item.split("|")

                if len(station_list) != 6:
                    continue

                #print(station_list)

                station_name = station_list[1]
                station_code = station_list[2]
                station_dic[station_name] = station_code

            #print(station_dic)
            with open(Config.get_station_file_path(), "w", encoding="utf-8") as f:
                json.dump(station_dic, f)

            return station_dic

    @staticmethod
    def get_all_stations_revere():
        station_dic = APITool.get_all_stations()
        station_dic_reverse = {value: key for key, value in station_dic.items()}
        #print(station_dic_reverse)
        return station_dic_reverse

    @staticmethod
    def query_tickts(train_date, from_station, to_station, purpose_codes):
        query_params = {
            "leftTicketDTO.train_date": train_date,
            "leftTicketDTO.from_station": from_station,
            "leftTicketDTO.to_station": to_station,
            "purpose_codes": purpose_codes
        }

        response = requests.get(API.QUERY_TICKETS_URL, params=query_params)
        #print(response.text)
        result = response.json()
        code2station = APITool.get_all_stations_revere()
        trainDicts = []
        if result["httpstatus"] == 200:
            items = result["data"]["result"]
            #print(items)
            for item in items:
                trainDict = {}
                trainInfo = item.split('|')
                if trainInfo[11] == "Y":
                    trainDict['secret_str'] = trainInfo[0] # 车次密文
                    trainDict['train_num'] = trainInfo[2] # 车号
                    trainDict['train_name'] = trainInfo[3] # 车次
                    trainDict['from_station_code'] = trainInfo[6] # 出发地电报码
                    trainDict['to_station_code'] = trainInfo[7] # 到达地电报码
                    trainDict['from_station_name'] = code2station[trainInfo[6]] # 出发地名称，通过反转键值取得
                    trainDict['to_station_name'] = code2station[trainInfo[7]] # 到达地名称，通过反转键值取得
                    trainDict['start_time'] = trainInfo[8] # 出发时间
                    trainDict['arrive_time'] = trainInfo[9] # 到达时间
                    trainDict['total_time'] = trainInfo[10] # 总用时
                    trainDict['left_tickets'] = trainInfo[12] # 余票
                    trainDict['train_date'] = trainInfo[13] # 车辆日期
                    trainDict['train_location'] = trainInfo[15] # P4 暂且不用
                    trainDict['vip_soft_bed'] = trainInfo[21] # 会员软卧
                    trainDict['other_seat'] = trainInfo[22] # 其他
                    trainDict['soft_bed'] = trainInfo[23] # 软卧
                    trainDict['no_seat'] = trainInfo[26] # 无座
                    trainDict['hard_bed'] = trainInfo[28] # 硬卧
                    trainDict['hard_seat'] = trainInfo[29] # 硬座
                    trainDict['second_seat'] = trainInfo[30] # 二等座
                    trainDict['first_seat'] = trainInfo[31] # 一等座
                    trainDict['business_seat'] = trainInfo[32] # 商务座
                    trainDict['move_bed'] = trainInfo[33] # 动卧
                trainDicts.append(trainDict)
        else:
            print("数据请求出错!")

        return trainDicts, len(trainDicts)

if __name__ == '__main__':
    #APITool.get_all_stations()
    #Config.get_yzm_file_path()
    APITool.get_all_stations_revere()
