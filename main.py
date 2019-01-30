from PyQt5.Qt import *

from Login_Pane import LoginPane
from Query_Pane import QueryPane

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    login_pane = LoginPane()
    login_pane.show()

    query_pane = QueryPane()

    def success_login_slot(content):
        print(content)

        login_pane.hide()

        query_pane.setWindowTitle(content)
        query_pane.show()


    login_pane.success_login.connect(success_login_slot)

    sys.exit(app.exec())