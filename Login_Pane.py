from PyQt5.Qt import *
from resource.login_ui import Ui_Form

class LoginPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def refresh_yzm(self):
        print("刷新验证码")

    def auto_dm(self):
        print("自动识别")

    def check_login(self):
        print("验证登录")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    login = LoginPane()
    login.show()

    sys.exit(app.exec())