from PyQt5.Qt import *
import requests

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



class APITool(QObject):
    session = requests.session()

    @classmethod
    def download_yzm(cls):
        response = cls.session.get(API.GET_YZM_URL)
        #print(response.content)
        with open("API/yzm.jpg", "wb") as f:
            f.write(response.content)

        #print(cls.session.cookies)

        return "API/yzm.jpg"

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
        print(response.text)


if __name__ == '__main__':
    APITool.download_yzm()
