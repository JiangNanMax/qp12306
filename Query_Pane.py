from PyQt5.Qt import *

from resource.query_pane_ui import Ui_Form
from API.API_Tool import APITool

class QueryPane(QWidget, Ui_Form):
    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.setupData()

    def setupData(self):
        station_dic = APITool.get_all_stations()
        self.from_station_cb.addItems(station_dic.keys())
        self.to_station_cb.addItems(station_dic.keys())

        from_completer = QCompleter(station_dic.keys())
        self.from_station_cb.setCompleter(from_completer)

        def check_data(cb):
            current_station = cb.currentText()
            result = station_dic.keys().__contains__(current_station)
            #print(result)
            if not result:
                cb.clearEditText()

        self.from_station_cb.lineEdit().editingFinished.connect(lambda : check_data(self.from_station_cb))

        to_completer = QCompleter(station_dic.keys())
        self.to_station_cb.setCompleter(to_completer)

        self.to_station_cb.lineEdit().editingFinished.connect(lambda : check_data(self.to_station_cb))


        self.start_date_edit.setDate(QDate.currentDate())
        self.start_date_edit.setMinimumDate(QDate.currentDate())

    def query_tickets(self):
        print("查询票")

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = QueryPane()
    window.show()

    sys.exit(app.exec())