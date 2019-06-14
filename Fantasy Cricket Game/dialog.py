# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(512, 476)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("AR BLANCA")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        import sqlite3
        conn=sqlite3.connect('database.db')
        self.horizontalLayout.addWidget(self.comboBox)
        sql='SELECT name FROM teams'
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            self.comboBox.addItem(row[0])
        conn.close()
        
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("AR BLANCA")
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_5.addWidget(self.frame)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.calculate)
        
        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def calculate(self):
        try:
            import sqlite3
            conn = sqlite3.connect('database.db')
            team=self.comboBox.currentText()
            self.listWidget.clear()
            sql1="SELECT players, value FROM teams WHERE name='"+team+"';"
            cur=conn.execute(sql1)
            row=cur.fetchone()
            selected=row[0].split(',')
            self.listWidget.addItems(selected)
            teamttl=0
            self.listWidget_2.clear()
            match=self.comboBox_2.currentText()
            for i in range(self.listWidget.count()):
                ttl=0
                batscore=0
                bowlscore=0
                fieldscore=0
                nm=self.listWidget.item(i).text()
                cursor=conn.execute("SELECT * FROM "+match+" WHERE player='"+nm+"'")
                row=cursor.fetchone()
                batscore=int(row[1]/2)
                if batscore>=50: batscore+=5
                if batscore>=100: batscore+=10
                if row[1]>0:
                    sr=row[1]/row[2]
                    if sr>=80 and sr<100: batscore+=2
                    if sr>=100:batscore+=4
                batscore=batscore+row[3]
                batscore=batscore+2*row[4]
                bowlscore=row[8]*10
                if row[8]>=3: bowlscore=bowlscore+5
                if row[8]>=5: bowlscore=bowlscore=bowlscore+10
                if row[7]>0:
                    er=6*row[7]/row[5]
                    if er<=2: bowlscore=bowlscore+10
                    if er>2 and er<=3.5: bowlscore=bowlscore+7
                    if er>3.5 and er<=4.5: bowlscore=bowlscore+4
                fieldscore=(row[9]+row[10]+row[11])*10
                ttl=batscore+bowlscore+fieldscore
                self.listWidget_2.addItem(str(ttl))
                teamttl=teamttl+ttl
                self.lineEdit.setText(str(teamttl))
        except:
            print("Fantasy Cricket Game")
    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Evaluate the Performance of your Fantasy Team"))
        self.label_2.setText(_translate("Dialog", "Select Team: "))
        self.label_3.setText(_translate("Dialog", "Select Match: "))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Match1"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Match2"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Match3"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Match4"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "Match5"))
        self.label_4.setText(_translate("Dialog", "Players"))
        self.label_5.setText(_translate("Dialog", "Points: "))
        self.pushButton.setText(_translate("Dialog", "Calculate Score"))
        self.lineEdit.setText(_translate("Dialog", "00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
