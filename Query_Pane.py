from PyQt5.Qt import *

from resource.query_pane_ui import Ui_Form

class QueryPane(QWidget, Ui_Form):
    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)



if __name__ == '__main__':
    pass