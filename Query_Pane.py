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

        # 设置表格的头部数据
        model = QStandardItemModel(self.tickets_tv)
        # 设置模型的头部数据
        headers = ["车次", "出发站->到达站", "出发时间->到达时间", "历时", "商务座-特等座",
                   "一等座","二等座", "高级软卧", "软卧-一等卧", "动卧","硬卧-二等卧",
                    "硬座", "无座", "其他"]
        model.setColumnCount(len(headers))
        for idx, header in enumerate(headers):
            model.setHeaderData(idx, Qt.Horizontal, header)

        self.tickets_tv.setModel(model)

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

        result, result_len = APITool.query_tickts(start_date, from_station_code, to_station_code, purpose_codes)
        #print(result_len)
        #for i in result:
        #    print(i)

        model = self.tickets_tv.model()
        model.setRowCount(result_len)

        cols = ["train_name",("from_station_name","to_station_name"),("start_time","arrive_time"),"total_time","business_seat","first_seat",
         "second_seat", "vip_soft_bed", "soft_bed", "move_bed", "hard_bed", "hard_seat", "no_seat", "other_seat"]

        for row, train_dic in enumerate(result):
            #print(train_dic)
            for col, col_name in enumerate(cols):
                if type(col_name) == str:
                    model.setItem(row, col, QStandardItem(train_dic[col_name]))
                else:
                    tmp = "->".join([train_dic[key] for key in col_name])
                    model.setItem(row, col, QStandardItem(tmp))

        self.tickets_tv.setModel(model)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = QueryPane()
    window.show()

    sys.exit(app.exec())