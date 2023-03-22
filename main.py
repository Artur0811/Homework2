import csv
import matplotlib.pyplot as plt
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QTableWidget, \
    QTableWidgetItem, QAbstractItemView
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import sys
import pandas as pd
import os

def res_path(path):
    try:
        a = sys._MEIPASS
    except Exception:
        a = os.path.abspath(".")

    return os.path.join(a, path)

def make_grath():
    fig, ax = plt.subplots()
    name = []
    res = []
    with open("data_2022.csv") as f:
        a = csv.DictReader(f, delimiter = ";")
        for i in a:
            if i["Role"] == "worker":
                name.append(i["Name"] + " " + i['Last_name'])
                res.append(int(i['Result']))
    data = pd.DataFrame({"Name" : name, "Result": res})
    ax.bar(data["Name"], data["Result"])
    fig.set_figwidth(4)
    fig.set_figheight(4)
    plt.savefig("data.png")

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Logwin()
        self.last_id = ""

    def Logwin(self):
        self.last_id = ""
        self.logw = Login()
        self.logw.log_btn.clicked.connect(self.logw.Login_true)
        self.logw.log_btn.clicked.connect(self.ras)
        self.logw.show()

    def ras(self):
        if self.logw.rol == "worker":
            self.work()
            self.logw.close()
        elif self.logw.rol == "director":
            self.dir()
            self.logw.close()
        else:
            self.admin()
            self.logw.close()

    def admin(self):
        if self.last_id == "":
            self.last_id = self.logw.id
        self.admw = AdminWin(self.last_id)
        self.admw.beak_btn.clicked.connect(self.Logwin)
        self.admw.beak_btn.clicked.connect(self.admw.close)
        self.admw.add_btn.clicked.connect(self.addwin)
        self.admw.re_btn.clicked.connect(self.rewin)
        self.admw.show()

    def work(self):
        self.last_id = self.logw.id
        self.workw = workWin(self.logw.name, self.logw.user_kpd)
        self.workw.beak_btn.clicked.connect(self.Logwin)
        self.workw.beak_btn.clicked.connect(self.workw.close)
        self.workw.show()

    def dir(self):
        self.last_id = self.logw.id
        self.dirw = DirWin()
        self.dirw.beak_btn.clicked.connect(self.Logwin)
        self.dirw.beak_btn.clicked.connect(self.dirw.close)
        self.dirw.show()

    def addwin(self):
        self.add = reUser()
        self.admw.close()
        self.add.beak_btn.clicked.connect(self.admin)
        self.add.beak_btn.clicked.connect(self.add.close)
        self.add.res_btn.clicked.connect(self.saccess)
        self.add.show()

    def rewin(self):
        if self.admw.select != "":
            self.add = reUser(self.admw.table.item(self.admw.select, 0).text())
            self.add.beak_btn.clicked.connect(self.admin)
            self.add.beak_btn.clicked.connect(self.add.close)
            self.add.res_btn.clicked.connect(self.saccess)
            self.add.show()
            self.admw.close()

    def saccess(self):
        if self.add.add:
            self.add.close()
            self.admin()

class reUser(QWidget):
    def __init__(self, user_id = ""):
        super().__init__()
        self.id = user_id
        self.UI()
        self.add= False

    def UI(self):
        self.setGeometry(100, 100, 600, 600)

        self.log = QLabel(self)
        self.log.setText("Логин")
        self.log.move(200, 100)

        self.pas = QLabel(self)
        self.pas.move(200, 150)
        self.pas.setText("Пароль")

        self.log_in = QLineEdit(self)
        self.log_in.move(300, 100)

        self.pas_in = QLineEdit(self)
        self.pas_in.move(300, 150)

        self.name = QLabel(self)
        self.name.move(200, 200)
        self.name.setText("Имя")

        self.l_name = QLabel(self)
        self.l_name.move(200, 250)
        self.l_name.setText("Фамилия")

        self.role= QLabel(self)
        self.role.move(200, 300)
        self.role.setText("Роль")

        self.name_in = QLineEdit(self)
        self.name_in.move(300, 200)

        self.l_name_in = QLineEdit(self)
        self.l_name_in.move(300, 250)

        self.role_in = QLineEdit(self)
        self.role_in.move(300, 300)

        self.beak_btn = QPushButton(self)
        self.beak_btn.setText("Назад")
        self.beak_btn.move(100, 550)

        self.res_btn = QPushButton(self)
        self.res_btn.setText("Принять")
        self.res_btn.move(250, 400)
        self.res_btn.clicked.connect(self.err)

        if self.id != "":
            self.fil_lb()

    def fil_lb(self):
        with open("data_2022.csv") as f:
            data = csv.DictReader(f, delimiter = ";")
            for i in data:
                if i["Id"] == self.id:
                    self.log_in.setText(i["Login"])
                    self.pas_in.setText(i["Password"])
                    self.l_name_in.setText(i["Last_name"])
                    self.name_in.setText(i["Name"])
                    self.role_in.setText(i["Role"])

    def err(self):
        if self.log_in.text() != "" and self.pas_in.text() != "" and self.l_name_in.text() != "" and self.name_in != "" and self.role_in.text() != "":
            self.add = True
            last = -1
            s = []
            with open("data_2022.csv") as f:
                data = csv.DictReader(f, delimiter = ";")
                for i in data:
                    last = max(last, int(i["Id"]))
                    i = dict(i)
                    if i["Id"] == self.id:
                        i["Login"] = self.log_in.text()
                        i["Password"] = self.pas_in.text()
                        i["Last_name"] = self.l_name_in.text()
                        i["Name"] = self.name_in.text()
                        i["Role"] = self.role_in.text()
                    s.append(i)
            if self.id == "":
                s.append({"Id": last+1, "Last_name":self.l_name_in.text(),  "Name":self.name_in.text(),
                          "Login":self.log_in.text(), "Password":self.pas_in.text(), "Role":self.role_in.text(), "Result":0})

            with open("data_2022.csv", "w") as f:
                data = csv.DictWriter(f, fieldnames=['Id', 'Last_name', 'Name', 'Login', 'Password', 'Role', 'Result'], delimiter=";")
                data.writeheader()
                for i in s:
                    data.writerow(i)

class AdminWin(QWidget):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.UI()
        self.select = ""

    def UI(self):
        self.setGeometry(100, 100, 700, 600)
        self.cr_table()

        self.beak_btn = QPushButton(self)
        self.beak_btn.setText("Назад")
        self.beak_btn.move(100, 550)

        self.delete_btn = QPushButton(self)
        self.delete_btn.setText("Удалить")
        self.delete_btn.move(50, 500)
        self.delete_btn.clicked.connect(self.del_value)

        self.add_btn =QPushButton(self)
        self.add_btn.setText("Add")
        self.add_btn.move(200, 500)

        self.re_btn = QPushButton(self)
        self.re_btn.setText("reuser")
        self.re_btn.move(350, 500)

    def cr_table(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["номер", "логин", "пароль", "Роль", "Имя"])
        self.table.setGeometry(50, 50, 600, 400)
        self.table.verticalHeader().setVisible(False)
        self.table.clicked.connect(self.val)
        self.fill_t()

    def del_value(self):
        num = self.table.item(self.select, 0).text()
        self.table.removeRow(self.select)
        s = []
        with open("data_2022.csv") as f:
            data = csv.DictReader(f, delimiter = ";")
            fi = data.fieldnames
            for i in data:
                if i["Id"] != num:
                    s.append(i)

        with open("data_2022.csv", "w") as f:
            data = csv.DictWriter(f, fieldnames=fi, delimiter = ";")
            data.writeheader()
            for i in s:
                data.writerow(i)

    def val(self):
        self.select = self.table.currentRow()
        self.table.selectRow(self.select)

    def fill_t(self):
        with open("data_2022.csv") as f:
            data = csv.DictReader(f, delimiter = ";")
            m = 0
            for i in data:
                if i["Id"] != self.id:
                    self.table.insertRow(m)
                    self.table.setItem(m, 0, QTableWidgetItem(i["Id"]))
                    self.table.setItem(m, 1, QTableWidgetItem(i["Login"]))
                    self.table.setItem(m, 2, QTableWidgetItem(i["Password"]))
                    self.table.setItem(m, 3, QTableWidgetItem(i["Role"]))
                    self.table.setItem(m, 4, QTableWidgetItem(i["Name"]))

class DirWin(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        self.setGeometry(100, 100, 800, 600)

        self.grath = QLabel(self)
        self.grath.move(350, 100)
        make_grath()
        self.grath.setPixmap(QPixmap("data.png"))

        self.table = QTableWidget(self)
        self.table.setGeometry(50, 100, 250, 400)
        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 100)
        self.table.setHorizontalHeaderLabels(["номер", "имя", "результат"])
        self.fill_table()

        self.beak_btn = QPushButton(self)
        self.beak_btn.setText("Назад")
        self.beak_btn.move(100, 550)

    def fill_table(self):
        with open("data_2022.csv") as f:
            data = csv.DictReader(f, delimiter = ";")
            n = 0
            for i in data:
                if i["Role"] == "worker":
                    self.table.insertRow(n)
                    self.table.setItem(n, 0, QTableWidgetItem(i["Id"]))
                    self.table.setItem(n, 1, QTableWidgetItem(i["Name"]))
                    self.table.setItem(n, 2, QTableWidgetItem(i["Result"]))
                    self.table.verticalHeader().setVisible(False)
                    n+=1

class workWin(QWidget):
    def __init__(self, name, kpd):
        super().__init__()
        self.name = name
        self.kpd = kpd
        self.UI()

    def UI(self):
        self.setGeometry(100, 100, 600, 600)

        self.name_lb= QLabel(self)
        self.name_lb.setText("С возвращением: "+ self.name)
        self.name_lb.move(300, 100)

        self.klic_btn = QPushButton(self)
        self.klic_btn.setGeometry(50, 200, 200, 200)
        self.klic_btn.setText("Нажать")
        self.klic_btn.clicked.connect(self.add_num)

        self.result = QLabel(self)
        self.result.setGeometry(400, 300, 300, 50)
        self.result.setText("Ваш результат: " + str(self.kpd))

        self.beak_btn = QPushButton(self)
        self.beak_btn.setText("Назад")
        self.beak_btn.move(100, 500)

    def add_num(self):
        self.kpd+=1
        self.result.setText("Ваш результат: " + str(self.kpd))

    def closeEvent(self, event):
        s = []
        with open("data_2022.csv") as f:
            data = csv.DictReader(f, delimiter = ";")
            for i in data:
                a = dict(i)
                if a["Name"] == self.name:
                    a["Result"] = self.kpd
                s.append(a)
        with open("data_2022.csv", "w") as f:
            data = csv.DictWriter(f, fieldnames=['Id', 'Last_name', 'Name', 'Login', 'Password', 'Role', 'Result'], delimiter = ";")
            data.writeheader()
            for i in range(len(s)):
                data.writerow(s[i])

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
        self.login = False
        self.rol = ""
        self.user_kpd = 0
        self.name = ""
        self.id = ""

    def UI(self):
        self.setGeometry(100, 100, 600, 600)

        self.loglb = QLabel(self)
        self.loglb.setText("Login")
        self.loglb.move(200, 200)

        self.paslb = QLabel(self)
        self.paslb.setText("Password")
        self.paslb.move(200, 300)

        self.in_log = QLineEdit(self)
        self.in_log.move(300, 200)
        self.in_log.setMaxLength(30)
        self.in_log.setText("user1")

        self.in_pass =QLineEdit(self)
        self.in_pass.move(300, 300)
        self.in_pass.setMaxLength(30)
        self.in_pass.setText("54093")

        self.log_btn = QPushButton(self)
        self.log_btn.setText("Login")
        self.log_btn.move(275, 350)

        self.beak_btn = QPushButton(self)
        self.beak_btn.setText("Назад")
        self.beak_btn.move(100, 500)
        self.beak_btn.clicked.connect(self.close)

    def Login_true(self):
        with open("data_2022.csv") as f:
            data = csv.DictReader(f, delimiter = ";")
            lg = self.in_log.text()
            ps = self.in_pass.text()
            for i in data:
                if i["Login"] == lg and i["Password"] == ps:
                    self.login = True
                    self.user_kpd = int(i["Result"])
                    self.rol = i["Role"]
                    self.name = i["Name"]
                    self.id = i["Id"]
                    break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wi1= MainWin()
    sys.exit(app.exec_())