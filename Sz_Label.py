from PyQt5.Qt import *

class SzLabel(QLabel):

    def auto_add_point(self, result):

        w = self.width() / 4
        h = (self.height() - 30) / 2

        for idx_c in result:
            idx_i = int(idx_c)

            row = (idx_i - 1) / 4
            col = (idx_i - 1) % 4

            center_x = col * w + w * 0.5
            center_y = row * h + h * 0.5 + 30

            self.create_point_btn(QPoint(center_x, center_y))



    def clear_points(self):
        [child.deleteLater() for child in self.children() if child.inherits("QPushButton")]

    def get_result(self):
        result  = ",".join(["{},{}".format(child.x() + 10, child.y() - 20) for child in self.children() if child.inherits("QPushButton")])
        #for child in self.children():
        #    if child.inherits("QPushButton"):
        #        print(child.pos())
        return result

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        #print(evt.pos())

        self.create_point_btn(evt.pos() - QPoint(10, 10))

    def create_point_btn(self, pt):
        point = QPushButton(self)
        point.resize(20, 20)
        point.move(pt)
        point.setStyleSheet("background-color: red; border-radius: 10px;")
        point.show()

        point.clicked.connect(lambda _, btn=point: btn.deleteLater())

        