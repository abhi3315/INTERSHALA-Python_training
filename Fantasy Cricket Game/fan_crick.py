# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_FILE.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1003, 600)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("AR DESTINE")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(3)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("AR BLANCA")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("AR BLANCA")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("AR BLANCA")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("AR BLANCA")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.frame)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_3.addWidget(self.lineEdit_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_2.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_6.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_4.addWidget(self.lineEdit_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_5.addWidget(self.lineEdit_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.horizontalLayout_6.addWidget(self.frame_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1003, 25))
        self.menubar.setObjectName("menubar")
        self.menuMANAGE_TEAMS = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        self.menuMANAGE_TEAMS.setFont(font)
        self.menuMANAGE_TEAMS.setObjectName("menuMANAGE_TEAMS")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuMANAGE_TEAMS.addAction(self.actionNEW_Team)
        self.menuMANAGE_TEAMS.addAction(self.actionOPEN_Team)
        self.menuMANAGE_TEAMS.addAction(self.actionSAVE_Team)
        self.menuMANAGE_TEAMS.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuMANAGE_TEAMS.menuAction())

        #######adding logic#########
        self.listWidget.itemDoubleClicked.connect(self.removelist1)
        self.listWidget_2.itemDoubleClicked.connect(self.removelist2)

        self.radioButton.toggled.connect(self.ctg)
        self.radioButton_2.toggled.connect(self.ctg)
        self.radioButton_3.toggled.connect(self.ctg)
        self.radioButton_4.toggled.connect(self.ctg)

        self.menuMANAGE_TEAMS.triggered[QtWidgets.QAction].connect(self.menu)

        self.bat=0
        self.bwl=0
        self.ar=0
        self.wk=0
        self.avl=1000
        self.used=0
    ##############################

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selections:"))
        self.label_2.setText(_translate("MainWindow", "Batsmen (BAT):"))
        self.label_3.setText(_translate("MainWindow", "Bowlers (BOW):"))
        self.label_4.setText(_translate("MainWindow", "Allrounders (AR):"))
        self.label_5.setText(_translate("MainWindow", "Wicket-keeper (WK):"))
        self.label_6.setText(_translate("MainWindow", "Points Available:"))
        self.radioButton.setText(_translate("MainWindow", "BAT"))
        self.radioButton_2.setText(_translate("MainWindow", "BOW"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.label_7.setText(_translate("MainWindow", "Points Used:"))
        self.label_8.setText(_translate("MainWindow", "Team Name:"))
        self.menuMANAGE_TEAMS.setTitle(_translate("MainWindow", "MANAGE TEAMS"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionNEW_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionOPEN_Team.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionEVALUATE_Team.setShortcut(_translate("MainWindow", "Ctrl+E"))

    ############defining Functions###########

    def menu(self,action):
        txt=(action.text())

        if txt=='NEW Team':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.listWidget.clear()
            self.listWidget_2.clear()

            text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter name of team:")
            if ok:
                self.lineEdit_7.setText(str(text))
            self.show()

        if txt=="SAVE Team":
            count=self.listWidget_2.count()
            selected=""
            for i in range(count):
                selected+=self.listWidget_2.item(i).text()
                if i<count:
                    selected+=","
            self.saveteam(self.lineEdit_7.text(),selected,self.used)

        if txt=='OPEN Team':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.avl=1000
            self.used=0
            self.listWidget.clear()
            self.listWidget_2.clear()
            self.show()
            self.openteam()

        if txt=='EVALUATE Team':
            from dialog import Ui_Dialog
            Dialog = QtWidgets.QDialog()
            ui=Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()

    def show(self):
        self.lineEdit.setText(str(self.bat))
        self.lineEdit_2.setText(str(self.bwl))
        self.lineEdit_3.setText(str(self.ar))
        self.lineEdit_4.setText(str(self.wk))
        self.lineEdit_5.setText(str(self.avl))
        self.lineEdit_6.setText(str(self.used))

    def criteria(self,ctgr,item):
        msg=''
        if ctgr=="BAT" and self.bat>=5:msg="Batsmen not more than 5."
        if ctgr=="BWL" and self.bwl>=5:msg="bowlers not more than 5."
        if ctgr=="AR" and self.ar>=3:msg="Allrounders not more than 3."
        if ctgr=="WK" and self.wk>=1:msg="Wicketkeeper not more than 1."
        if msg!='':
            self.showdlg(msg)
            return False

        if self.avl<0:
            msg="You have exhausted your points!"
            self.showdlg(msg)
            return False
        
        if ctgr=="BAT":self.bat+=1
        if ctgr=="BWL":self.bwl+=1
        if ctgr=="AR":self.ar+=1
        if ctgr=="WK":self.wk+=1

        sql="SELECT value from stats WHERE player='"+item.text()+"';"
        cur=conn.execute(sql)
        row=cur.fetchone()
        self.avl-=int(row[0])
        self.used+=int(row[0])
        return True


    def removelist1(self,item):

        ctgr=''
        if self.radioButton.isChecked()==True:ctgr='BAT'
        if self.radioButton_2.isChecked()==True:ctgr='BWL'
        if self.radioButton_3.isChecked()==True:ctgr='AR'
        if self.radioButton_4.isChecked()==True:ctgr='WK'
        ret=self.criteria(ctgr,item)

        if ret==True:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            self.show()

    def ctg(self):
        ctgr=''
        if self.radioButton.isChecked()==True:ctgr='BAT'
        if self.radioButton_2.isChecked()==True:ctgr='BWL'
        if self.radioButton_3.isChecked()==True:ctgr='AR'
        if self.radioButton_4.isChecked()==True:ctgr='WK'

        self.fillList(ctgr)

    def removelist2(self,item):
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        cursor=conn.execute("SELECT player,value,ctg FROM stats WHERE player='"+item.text()+"';")
        row=cursor.fetchone()
        self.avl=self.avl+int(row[1])
        self.used=self.used-int(row[1])
        ctgr=row[2]
        if ctgr=="BAT":
            self.bat-=1
            if self.radioButton.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="BWL":
            self.bwl-=1
            if self.radioButton_2.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="AR":
            self.ar-=1
            if self.radioButton_3.isChecked()==True:self.listWidget.addItem(item.text())
        if ctgr=="WK":
            self.wk-=1
            if self.radioButton_4.isChecked()==True:self.listWidget.addItem(item.text())
        self.show()

    def fillList(self,ctgr):
        if self.lineEdit_7.text()=='':
            self.showdlg("Create a new team.")
            return
        self.listWidget.clear()
        sql="SELECT player FROM players WHERE ctg='"+ctgr+"';"
        cur=conn.execute(sql)
        for row in cur:
            selected=[]
            for i in range(self.listWidget_2.count()):
                selected.append(self.listWidget_2.item(i).text())
            if row[0] not in selected:
                self.listWidget.addItem(row[0])

    def openteam(self):
        sql="SELECT name FROM teams;"
        cur=conn.execute(sql)
        teams=[]
        for row in cur:
            teams.append(row[0])
        team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Dream","Choose A Team",teams,0,False)
        if ok and team:
            self.lineEdit_7.setText(team)

        sqll="SELECT players,value FROM teams WHERE name='"+team+"';"
        cur=conn.execute(sqll)
        row=cur.fetchone()
        selected=row[0].split(',')
        self.listWidget_2.addItems(selected)
        self.used=row[1]
        self.avl=1000-row[1]
        count=self.listWidget_2.count()

        for i in range(count-1):
            ply=self.listWidget_2.item(i).text()
            sql="SELECT ctg FROM stats WHERE player='"+ply+"';"
            cur=conn.execute(sql)
            row=cur.fetchone()
            ctgr=row[0]
            if ctgr=="BAT":self.bat+=1
            if ctgr=="BWL":self.bwl+=1
            if ctgr=="AR":self.ar+=1
            if ctgr=="WK":self.wk+=1

        self.show()

    def saveteam(self,nm,ply,val):
        if self.bat+self.bwl+self.ar+self.wk!=11:
            self.showdlg("Select 11 Players.")
            return
        
        sql="INSERT INTO teams (name,players,value) VALUES('"+nm+"','"+ply+"','"+str(val)+"');"
        try:
            cur=conn.execute(sql)
            self.showdlg("Team Saved Successfully!")
            conn.commit()
        except:
            self.showdlg("Error in operation!")
            conn.rollback()
            
    def showdlg(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Dream Team selector")
        ret=Dialog.exec()
    
if __name__ == "__main__":
    import sqlite3
    conn=sqlite3.connect('database.db')
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
