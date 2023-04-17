# This Python file uses the following encoding: utf-8
import sys
import threading

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QInputDialog, QLineEdit,QListWidgetItem
from PySide6.QtCore import Qt
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

from pynput.mouse import Button, Controller
import pynput

# from pynput import mouse

def thread_mousetrack(widget):
    with pynput.mouse.Events() as event:

        for i in event:
        #迭代用法。
            if widget.Add_btn_Status == 'White':
                continue
            if isinstance(i, pynput.mouse.Events.Click) and i.pressed:
                #鼠标点击事件。
                widget.ui.Record_List.addItem(QListWidgetItem(f'{i.x},{i.y}'))
#                print(i.x, i.y, i.button, i.pressed)
                # return i.x,i.y
                #这个i.button就是上文所说的“鼠标按键”中的一个，用is语句判断即可。
        i = event.get(1)

class Widget(QWidget):
    mouse = Controller()
    Add_btn_Status = 'White'
    t = None
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True) #Pin
        # self.setWindowFlag(Qt.FramelessWindowHint, True)

#        self.ui.Right_Btn.setStyleSheet(f"background-color: {self.Add_btn_Status};border:2px solid;border-radius:2px")
#        self.ui.Add_btn.setStyleSheet(f"background-color: {self.Add_btn_Status};border:2px solid;border-radius:2px")

        self.ui.Add_btn.clicked.connect(self.add_position)
        self.ui.Right_Btn.clicked.connect(self.right_down)
        self.t = threading.Thread(target=thread_mousetrack, args = (self,))  #建立執行緒

    def add_position(self):
        if self.Add_btn_Status == 'White':
            self.Add_btn_Status = 'Red'
#            self.ui.Add_btn.setStyleSheet(f"background-color: {self.Add_btn_Status};border:2px solid;border-radius:2px")
            self.ui.Right_Btn.setDisabled(1)

            self.t.start()  #執行
            # X,Y = thread_mousetrack()
            # self.ui.Record_List.addItem(QListWidgetItem(f'{X},{Y}'))

        else:
            self.Add_btn_Status = 'White'
#            self.ui.Add_btn.setStyleSheet(f"background-color: {self.Add_btn_Status};border:2px solid;border-radius:2px")
            self.ui.Right_Btn.setDisabled(0)

        # X, okX = QInputDialog.getText(self, "Input Location."," X軸", QLineEdit.Normal)
        # Y, okY = QInputDialog.getText(self, "Input Location."," Y軸", QLineEdit.Normal)

        # if okX and X and okY and Y:
        #         self.ui.Record_List.addItem(QListWidgetItem(f'({X},{Y})'))
        print("Clicked!")

    def right_down(self):
        pos = self.ui.Record_List.currentItem().text().split(',')
        self.mouse.position = (int(pos[0]), int(pos[1]))
        print(pos)
        self.mouse.press(Button.right)
        self.mouse.release(Button.right)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()

    sys.exit(app.exec())
