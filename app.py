from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
import sys

class Contact(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("สิ่งที่ได้จากการไปค่าย")
        self.setFixedSize(QSize(1270,720))
        #สร้าง layout และตั้งค่า
        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(hbox)

        img = QPixmap("img/5.png")
        label = QLabel()
        label.setPixmap(img.scaled(self.size()))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #widget
        #add widget to layout
        hbox.addWidget(label)

class Other(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Other")
        self.setFixedSize(QSize(1270,720))
        #สร้าง layout และตั้งค่า
        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(hbox)

        img = QPixmap("img/4.png")
        label = QLabel()
        label.setPixmap(img.scaled(self.size()))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #widget
        #add widget to layout
        hbox.addWidget(label)

class MINICAMP21(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("สิ่งที่ได้จากการไปค่าย")
        self.setFixedSize(QSize(1270,720))
        #สร้าง layout และตั้งค่า
        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(hbox)

        img = QPixmap("img/3.png")
        label = QLabel()
        label.setPixmap(img.scaled(self.size()))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #widget
        #add widget to layout
        hbox.addWidget(label)

class ITCAMP21(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("สิ่งที่ได้จากการไปค่าย")
        self.setFixedSize(QSize(1270,720))
        #สร้าง layout และตั้งค่า
        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(hbox)

        img = QPixmap("img/2.png")
        label = QLabel()
        label.setPixmap(img.scaled(self.size()))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #widget
        #add widget to layout
        hbox.addWidget(label)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("โปรแกรมของฉัน PyQt6 (นายกรินทร์ ชัยอมรวานิช)")
        self.setFixedSize(QSize(1270,720))
        #สร้าง layout และตั้งค่า
        hbox = QHBoxLayout()
        self.setLayout(hbox)
        hbox.setSpacing(20)
        hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.show_startup_notification()
        
        #widget

        self.ITCAMP21=None
        self.MINICAMP21=None
        self.Other=None
        self.Contact=None

        btn1=QPushButton("ITCAMP 21",self)
        btn1.clicked.connect(self.display)
        btn1.setObjectName("btn1")

        btn2=QPushButton("MINICAMP 21",self)
        btn2.clicked.connect(self.display)
        btn2.setObjectName("btn1")

        btn3=QPushButton("OTHER",self)
        btn3.clicked.connect(self.display)
        btn3.setObjectName("btn3")

        btn4=QPushButton("CONTACT",self)
        btn4.clicked.connect(self.display)
        btn4.setObjectName("btn4")
            

        # สร้าง layout ใหม่เฉพาะสำหรับปุ่ม
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(btn1)
        button_layout.addWidget(btn2)
        button_layout.addWidget(btn3)
        button_layout.addWidget(btn4)


        # container widget สำหรับ layout ปุ่ม
        button_container = QWidget(self)
        button_container.setLayout(button_layout)
        button_container.setGeometry(0, 350, 1270, 100)

    
        img = QPixmap("img/1.png")
        bg_label = QLabel(self)
        bg_label.setPixmap(img)
        bg_label.setFixedSize(QSize(1270,720))
        bg_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bg_label.lower()
        
        #add widget to layout
        hbox.addWidget(bg_label)

    def show_startup_notification(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("แจ้งเตือน")
        msg.setText("ยินดีต้อนรับเข้าสู่โปรแกรม! กรุณาเลือกจากซ้ายไปขวานะครับ ขอบคุณมากๆครับ TT")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()


    def display(self):
        if self.ITCAMP21 is None:
            self.ITCAMP21=ITCAMP21()
            self.ITCAMP21.show()
        elif self.MINICAMP21 is None:
            self.MINICAMP21=MINICAMP21()
            self.MINICAMP21.show()
        elif self.Other is None:
            self.Other=Other()
            self.Other.show()
        elif self.Contact is None:
            self.Contact=Contact()
            self.Contact.show()

#รันโปรแกรม
app=QCoreApplication.instance()
if app is None:
    app=QApplication([])
    with open('style.css','r') as style:
        app.setStyleSheet(style.read())

window = MainWindow()
window.show()
app.exec()