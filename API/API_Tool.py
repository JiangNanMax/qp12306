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


if __name__ == '__main__':
    APITool.get_all_stations()
    #Config.get_yzm_file_path()
