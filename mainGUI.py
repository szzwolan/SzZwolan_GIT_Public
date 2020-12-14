from PyQt5 import QtCore, QtGui, QtWidgets
import pdfBrowser
import pdfReader
import msgGenerate
import excelReader
from tkinter import messagebox as tkMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, n, m):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 801)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(30, 30, 471, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 61, 16))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 70, 491, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 100, 71, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 100, 81, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 100, 191, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 150, 471, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 80, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 80, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 55, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(400, 100, 101, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 80, 55, 16))
        self.label_6.setObjectName("label_6")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 363, 491, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 383, 51, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setCurrentIndex(m - 1)
        self.comboBox.currentIndexChanged[int].connect(lambda: self.comboBoxChanged())



        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 383, 81, 21))
        self.label_7.setObjectName("label_7")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 180, 111, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(30, 270, 141, 16))
        self.label_16.setObjectName("label_15")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 200, 471, 61))
        self.textEdit_3.setObjectName("textEdit_PerformedAction")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(30, 290, 471, 61))
        self.textEdit_4.setObjectName("textEdit_Verification")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 410, 491, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 380, 311, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: reportGenerate(self,m) )
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 430, 471, 321))
        self.tabWidget.setObjectName("tabWidget")

        listGenerator(self, n, m)
        tabGen(self, n, m)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBrowser = QtWidgets.QAction(MainWindow)
        self.actionBrowser.setObjectName("action")
        #self.actionBrowser.triggered.connect(lambda: pdfReader.pdfReader())
        self.actionBrowser.triggered.connect(lambda: fillFields(self))


        self.actionEdit_probe_list = QtWidgets.QAction(MainWindow)
        self.actionEdit_probe_list.setObjectName("actionEdit_probe_list")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(lambda: close_application(self))

        self.actionTabWidgetNo = QtWidgets.QAction(MainWindow)
        self.actionTabWidgetNo.setObjectName("actionTabWidgetNo")
        self.menuFile.addAction(self.actionBrowser)
        self.menuFile.addAction(self.actionEdit_probe_list)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        print("Click")

    def comboBoxChanged(self):
        a = self.comboBox.currentIndex()
        self.comboBox.setCurrentIndex(a)
        print("selected index = " + str(a))
        tabCount = self.tabWidget.count()
        print("liczba tabów: " + str(tabCount))
        if a + 1 > tabCount:
            listGenerator(self, tabCount, a + 1)
            tabGen(self, tabCount, a + 1)
        elif a + 1 < tabCount:
            for i in range((a + 1), tabCount):
                self.tabWidget.removeTab(self.tabWidget.count() - 1)
        else:
            print("nic")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ULS Report generator"))
        self.label.setText(_translate("MainWindow", "Report file"))
        self.label_2.setText(_translate("MainWindow", "Dispatch"))
        self.label_3.setText(_translate("MainWindow", "SystemID"))
        self.label_4.setText(_translate("MainWindow", "System"))
        self.label_5.setText(_translate("MainWindow", "Customer"))
        self.label_6.setText(_translate("MainWindow", "S/N"))
        self.comboBox.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "9"))
        self.comboBox.setItemText(9, _translate("MainWindow", "10"))
        self.comboBox.setItemText(10, _translate("MainWindow", "New Item"))
        self.label_7.setText(_translate("MainWindow", "No. of issues"))
        self.label_15.setText(_translate("MainWindow", "Performed action"))
        self.label_16.setText(_translate("MainWindow", "Verification / Test done"))
        self.pushButton.setText(_translate("MainWindow", "Generate report message"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionBrowser.setText(_translate("MainWindow", "Load PDF report"))
        self.actionEdit_probe_list.setText(_translate("MainWindow", "Edit probe list"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionTabWidgetNo.setText(_translate("MainWindow", "TabWidgetNo"))
        print("Click")

    def aaa(self):
        print()


def radioButtonChecked(self, n):
    for i in range(0, n):
        if self.radioButton[i].isChecked():
            print("Radiobutton " + str(i) + " checked!")
            self.frame[i].setVisible(True)
            self.lineEdit_7[i].setVisible(False)
            self.label_9[i].setVisible(False)
            self.label_10[i].setVisible(True)
            self.label_11[i].setVisible(True)
            self.label_12[i].setVisible(True)
            self.textEditDescription[i].setVisible(True)
            self.lineEdit_6[i].setVisible(True)
            self.lineEdit_9[i].setVisible(True)
            self.comboBox_2[i].setVisible(True)
            self.label_11[i].setText("Probe name")
        else:
            print("Radiobutton " + str(i) + " unchecked!")
            self.frame[i].setVisible(False)
            self.lineEdit_7[i].setVisible(True)
            self.label_9[i].setVisible(True)
            self.label_11[i].setVisible(True)
            self.label_12[i].setVisible(True)
            self.textEditDescription[i].setVisible(True)
            self.lineEdit_6[i].setVisible(True)
            self.lineEdit_7[i].setVisible(True)
            self.lineEdit_9[i].setVisible(True)
            self.comboBox_2[i].setVisible(True)
            self.label_11[i].setText("Part name")


def listGenerator(self, n, m):
    if n == 0:
        self.frame = [None] * m
        self.radioButton = [None] * m
        self.radioButton_2 = [None] * m
        self.comboBox_2 = [None] * m
        self.tab = [None] * m
        self.label_8 = [None] * m
        self.label_9 = [None] * m
        self.label_10 = [None] * m
        self.label_11 = [None] * m
        self.label_12 = [None] * m
        self.lineEdit_6 = [None] * m
        self.lineEdit_7 = [None] * m
        self.lineEdit_8 = [None] * m
        self.lineEdit_9 = [None] * m
        self.lineEdit_10 = [None] * m
        self.lineEdit_11 = [None] * m
        self.textEditDescription = [None] * m

    else:
        for i in range(n, m):
            self.frame.append(None)
            self.radioButton.append(None)
            self.radioButton_2.append(None)
            self.tab.append(None)
            self.label_8.append(None)
            self.label_9.append(None)
            self.label_10.append(None)
            self.label_11.append(None)
            self.label_12.append(None)
            self.lineEdit_6.append(None)
            self.lineEdit_7.append(None)
            self.lineEdit_8.append(None)
            self.lineEdit_9.append(None)
            self.lineEdit_10.append(None)
            self.lineEdit_11.append(None)
            self.textEditDescription.append(None)


def tabGen(self, n, m):
    _translate = QtCore.QCoreApplication.translate
    print(m)

    for i in range(n, m):
        self.tab[i] = QtWidgets.QWidget()
        self.tab[i].setObjectName("Tab" + str(i + 1))

        self.frame[i] = QtWidgets.QFrame(self.tab[i])
        self.frame[i].setGeometry(QtCore.QRect(0, 220, 451, 71))
        self.frame[i].setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame[i].setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame[i].setObjectName("frame")

        self.textEditDescription[i] = QtWidgets.QTextEdit(self.tab[i])
        self.textEditDescription[i].setGeometry(QtCore.QRect(10, 60, 441, 111))
        self.textEditDescription[i].setObjectName("lineEditDescription")
        self.radioButton[i] = QtWidgets.QRadioButton(self.tab[i])
        self.radioButton[i].setGeometry(QtCore.QRect(20, 10, 81, 20))
        self.radioButton[i].setObjectName("radioButton")
        self.radioButton[i].toggled.connect(lambda: radioButtonChecked(self, m))

        self.radioButton_2[i] = QtWidgets.QRadioButton(self.tab[i])
        self.radioButton_2[i].setGeometry(QtCore.QRect(100, 10, 81, 20))
        self.radioButton_2[i].setObjectName("radioButton_2")
        self.lineEdit_6[i] = QtWidgets.QLineEdit(self.tab[i])
        self.lineEdit_6[i].setGeometry(QtCore.QRect(10, 200, 271, 22))
        self.lineEdit_6[i].setObjectName("lineEdit_6")
        self.lineEdit_7[i] = QtWidgets.QLineEdit(self.tab[i])
        self.lineEdit_7[i].setGeometry(QtCore.QRect(370, 200, 81, 22))
        self.lineEdit_7[i].setObjectName("lineEdit_7")
        self.lineEdit_8[i] = QtWidgets.QLineEdit(self.frame[i])
        self.lineEdit_8[i].setGeometry(QtCore.QRect(40, 10, 31, 22))
        self.lineEdit_8[i].setObjectName("lineEdit_8")
        self.lineEdit_10[i] = QtWidgets.QLineEdit(self.frame[i])
        self.lineEdit_10[i].setGeometry(QtCore.QRect(120, 10, 31, 22))
        self.lineEdit_10[i].setObjectName("lineEdit_10")


        self.label_8[i] = QtWidgets.QLabel(self.frame[i])
        self.label_8[i].setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label_8[i].setObjectName("label_8")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8[i].setFont(font)

        self.lineEdit_9[i] = QtWidgets.QLineEdit(self.tab[i])
        self.lineEdit_9[i].setGeometry(QtCore.QRect(290, 200, 71, 22))
        self.lineEdit_9[i].setObjectName("lineEdit_9")
        self.label_9[i] = QtWidgets.QLabel(self.tab[i])
        self.label_9[i].setGeometry(QtCore.QRect(370, 180, 71, 16))
        self.label_9[i].setObjectName("label_9")
        self.label_10[i] = QtWidgets.QLabel(self.tab[i])
        self.label_10[i].setGeometry(QtCore.QRect(290, 180, 21, 16))
        self.label_10[i].setObjectName("label_10")
        self.label_11[i] = QtWidgets.QLabel(self.tab[i])
        self.label_11[i].setGeometry(QtCore.QRect(10, 180, 71, 16))
        self.label_11[i].setObjectName("label_11" + str(i))
        self.label_12[i] = QtWidgets.QLabel(self.tab[i])
        self.label_12[i].setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.label_12[i].setObjectName("label_12" + str(i))

        self.lineEdit_11[i] = QtWidgets.QLineEdit(self.frame[i])
        self.lineEdit_11[i].setGeometry(QtCore.QRect(60, 40, 301, 22))
        self.lineEdit_11[i].setObjectName("lineEdit_11")
        self.label_13 = QtWidgets.QLabel(self.frame[i])
        self.label_13.setGeometry(QtCore.QRect(10, 10, 51, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame[i])
        self.label_14.setGeometry(QtCore.QRect(10, 40, 51, 20))
        self.label_14.setObjectName("label_14")
        self.label_17 = QtWidgets.QLabel(self.frame[i])
        self.label_17.setGeometry(QtCore.QRect(80, 10, 51, 20))
        self.label_17.setObjectName("label_15")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame[i])
        self.pushButton_2.setGeometry(QtCore.QRect(370, 10, 81, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: unisynCheck(self, self.tabWidget.currentIndex()))
        #3self.pushButton_2.clicked.connect(lambda: unisynCheck(self, i))
        self.comboBox_2[i] = QtWidgets.QComboBox(self.frame[i])
        self.comboBox_2[i].setGeometry(QtCore.QRect(160, 10, 201, 22))
        self.comboBox_2[i].setObjectName("comboBox_2")


        self.tabWidget.addTab(self.tab[i], "")

        tabName = str(i + 1)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab[i]), _translate("MainWindow", tabName))

        self.radioButton[i].setText(_translate("MainWindow", "Probe"))
        self.radioButton_2[i].setText(_translate("MainWindow", "Other"))
        #self.label_8[i].setText(_translate("MainWindow", "UNISYN"))
        self.label_9[i].setText(_translate("MainWindow", "Labour time"))
        self.label_10[i].setText(_translate("MainWindow", "PN"))
        self.label_11[i].setText(_translate("MainWindow", "Part name"))
        self.label_12[i].setText(_translate("MainWindow", "Problem descryption"))
        self.label_13.setText(_translate("MainWindow", "Test"))
        self.label_14.setText(_translate("MainWindow", "Console"))
        self.label_17.setText(_translate("MainWindow", "Repair"))
        self.pushButton_2.setText(_translate("MainWindow", "Check"))

        self.frame[i].setVisible(False)
        self.label_9[i].setVisible(False)
        self.label_10[i].setVisible(False)
        self.label_11[i].setVisible(False)
        self.label_12[i].setVisible(False)
        self.textEditDescription[i].setVisible(False)
        self.lineEdit_6[i].setVisible(False)

        self.lineEdit_7[i].setVisible(False)
        self.lineEdit_9[i].setVisible(False)

def fillFields(self):
    print("Report filling")
    report = pdfReader.pdfReader()
    self.textEdit.setText(report[0])
    self.lineEdit.setText(report[1])
    self.lineEdit_2.setText(report[2])
    self.lineEdit_3.setText(report[3])
    self.lineEdit_5.setText(report[4])
    self.lineEdit_4.setText(report[5])
    self.textEdit_3.setText(report[6])
    self.textEdit_4.setText(report[7])
    #self.

def unisynCheck(self,i):
    print("Unisyn CHECK")

    # for n in range(0,i):
    probeName = self.lineEdit_6[i].text()
    if(probeName != ""):
        probeCapa, unisynStatus, console = excelReader.excelReader(probeName)

        if unisynStatus[5] == "Y":
            testStatus = "YES"
            bg1 = 'green'
            if unisynStatus[16] == "Y":
                repairStatus = "YES"
                bg2 = 'green'
            else:
                repairStatus = "NO"
                bg2 = 'red'
        else:
            testStatus = "NO"
            bg1 = 'red'
            if unisynStatus[15] == "Y":
                repairStatus = "YES"
                bg2 = 'green'
            else:
                repairStatus = "NO"
                bg2 = 'red'

        self.lineEdit_8[i].setText(testStatus)
        self.lineEdit_8[i].setStyleSheet('background-color: ' + bg1 + ';color: yellow')
        self.lineEdit_10[i].setText(repairStatus)
        self.lineEdit_10[i].setStyleSheet('background-color: ' + bg2 + ';color: yellow')
        self.lineEdit_11[i].setText(console)
        if len(probeCapa) != 0:
            self.comboBox_2[i].clear()
            for n in range(0, len(probeCapa)):
                self.comboBox_2[i].addItem(probeCapa[n])
                # else:
                #     self.comboBox_2[i].clear()
                #     self.comboBox_2[i].addItem(probeCapa)




def reportGenerate(self,m):
    print("Report generate!")

    m = self.tabWidget.count()

    report = [],[]
    issues = [0] * m
    comboBoxValue = self.comboBox.currentIndex()
    #If no issues selected then fill just customer&device data
    if comboBoxValue!=-1:
    # If tab issue is about probe then write 1 into array
        for i in range(0,m):
            report[i].append(self.lineEdit.text())
            report[i].append(self.lineEdit_2.text())
            report[i].append(self.lineEdit_3.text())
            report[i].append(self.lineEdit_4.text())
            report[i].append(self.lineEdit_5.text())
            report[i].append(self.textEditDescription[i].toPlainText())
            report[i].append(self.lineEdit_6[i].text())
            report[i].append(self.lineEdit_7[i].text())
            report[i].append(self.lineEdit_9[i].text())


        if self.radioButton[i].isChecked():
            issues[i] = 1

        if len(self.textEdit.toPlainText()) == 0:
            print("Brak danych")
            tkMessageBox.showinfo(title="Error", message="Missing iDebrief report!")
        else:
            msgGenerate.msgGenerate(report, issues)

    else:
        tkMessageBox.showinfo(title="Error", message="No issues filled!")

    # report.append(self.lineEdit.text())
    # report.append(self.lineEdit_2.text())
    # report.append(self.lineEdit_3.text())
    # report.append(self.lineEdit_4.text())
    # report.append(self.lineEdit_5.text())


    # report.append(self.textEdit_2.text())
    # report.append(self.lineEdit_6.text())
    # report.append(self.lineEdit_7.text())
    # report.append(self.lineEdit_9.text())




def close_application(self):
    print("Quit app")
    sys.exit()




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, 0, 0)
    MainWindow.show()

    sys.exit(app.exec_())
