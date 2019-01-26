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



if __name__ == '__main__':
    APITool.download_yzm()
