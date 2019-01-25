from PyQt5.Qt import *
import requests

class API(object):

    # 下载验证码 GET
    GET_YZM_URL = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"



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


if __name__ == '__main__':
    APITool.download_yzm()
