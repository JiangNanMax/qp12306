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

        start_date = self.start_date_edit.text()
        print(start_date)

        station_dic = APITool.get_all_stations()
        from_station_code = station_dic[self.from_station_cb.currentText()]
        to_station_code = station_dic[self.to_station_cb.currentText()]
        print(from_station_code, to_station_code)

        purpose_codes = self.buttonGroup.checkedButton().property("q_value")
        print(purpose_codes)

        APITool.query_tickts(start_date, from_station_code, to_station_code, purpose_codes)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = QueryPane()
    window.show()

    sys.exit(app.exec())