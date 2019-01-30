from PyQt5.Qt import *
from resource.login_ui import Ui_Form

from API.API_Tool import APITool
from API.YDMHTTP import YDMHttp

class DownLoadYZMThread(QThread):

    get_yzm_url_signal = pyqtSignal(str)

    def run(self):
        print("下载验证码")
        url = APITool.download_yzm()
        print("验证码下载成功")
        self.get_yzm_url_signal.emit(url)

class DMThread(QThread):

    def __init__(self, url, parent=None):
        super().__init__(parent)
        self.yzm_url = url

    get_yzm_result_signal = pyqtSignal(str)

    def run(self):
        print("开始进行识别")
        dm = YDMHttp()
        result = dm.get_yzm_result(self.yzm_url)
        print("识别完成")
        self.get_yzm_esult_signal.emit(result)

class LoginPane(QWidget, Ui_Form):

    success_login = pyqtSignal(str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.refresh_yzm()

    def refresh_yzm(self):
        print("刷新验证码")

        thread = DownLoadYZMThread(self)

        def parse_yzm_url(url):
            self.current_yzm_url = url
            #print(url)

            self.yzm_label.clear_points()
            pixmap = QPixmap(url)
            self.yzm_label.setPixmap(pixmap)

        thread.get_yzm_url_signal.connect(parse_yzm_url)
        thread.start()

        print("继续主线程任务")

    def auto_dm(self):
        print("自动识别")
        self.auto_dm_btn.setEnabled(False)

        thread = DMThread(self.current_yzm_url, self)

        def parse_yzm_result(result):
            # print(result)
            self.auto_dm_btn.setEnabled(True)
            if result != "0":
                self.yzm_label.auto_add_point(result)
            else:
                print("识别失败！")

        thread.get_yzm_url_signal.connect(parse_yzm_result)
        thread.start()


    def check_login(self):
        print("验证登录")

        result = self.yzm_label.get_result()
        print(result)

        if len(result) == 0:
            print("请填写验证码！")
            return None

        if APITool.check_yzm(result):
            print("验证码正确")

            # 拿到账号和密码
            account = self.account_le.text()
            pwd = self.pwd_le.text()

            #print(account, pwd)
            result_str = APITool.check_account_pwd(account, pwd)
            #print(result_str)

            self.success_login.emit(result_str)

        else:
            print("验证码错误")
            self.yzm_label.clear_points()
            self.refresh_yzm()

    def auto_enable_login_btn(self):
        print("设置登录按钮为有效")
        account = self.account_le.text()
        pwd = self.pwd_le.text()

        if len(account) == 0 or len(pwd) == 0:
            self.login_btn.setEnabled(False)
        else:
            self.login_btn.setEnabled(True)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    login = LoginPane()
    login.show()

    sys.exit(app.exec())