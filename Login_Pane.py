from PyQt5.Qt import *
from resource.login_ui import Ui_Form

from API.API_Tool import APITool
from API.YDMHTTP import YDMHttp

class LoginPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.refresh_yzm()

    def refresh_yzm(self):
        print("刷新验证码")
        url = APITool.download_yzm()
        self.current_yzm_url = url
        print(url)

        self.yzm_label.clear_points()

        pixmap = QPixmap(url)
        self.yzm_label.setPixmap(pixmap)

    def auto_dm(self):
        print("自动识别")
        dm = YDMHttp()
        result = dm.get_yzm_result(self.current_yzm_url)
        #print(result)
        self.yzm_label.auto_add_point(result)

    def check_login(self):
        print("验证登录")

        result = self.yzm_label.get_result()
        print(result)

        if APITool.check_yzm(result):
            print("验证码正确")
        else:
            print("验证码错误")
            self.yzm_label.clear_points()
            self.refresh_yzm()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    login = LoginPane()
    login.show()

    sys.exit(app.exec())