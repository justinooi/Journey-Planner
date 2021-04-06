from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Ui_JourneyPlannerGUI(object):
    def setupUi(self, JourneyPlannerGUI):
        JourneyPlannerGUI.setObjectName("JourneyPlannerGUI")
        JourneyPlannerGUI.resize(492, 525)
        JourneyPlannerGUI.setMinimumSize(QtCore.QSize(492, 525))
        JourneyPlannerGUI.setMaximumSize(QtCore.QSize(492, 525))
        self.centralwidget = QtWidgets.QWidget(JourneyPlannerGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.findRouteButton = QtWidgets.QPushButton(self.centralwidget)
        self.findRouteButton.setGeometry(QtCore.QRect(390, 10, 91, 51))
        self.findRouteButton.setObjectName("findRouteButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 371, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 40, 371, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.widget = QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 70, 471, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        JourneyPlannerGUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(JourneyPlannerGUI)
        self.statusbar.setObjectName("statusbar")
        JourneyPlannerGUI.setStatusBar(self.statusbar)

        self.retranslateUi(JourneyPlannerGUI)
        QtCore.QMetaObject.connectSlotsByName(JourneyPlannerGUI)

    def retranslateUi(self, JourneyPlannerGUI):
        _translate = QtCore.QCoreApplication.translate
        JourneyPlannerGUI.setWindowTitle(_translate("JourneyPlannerGUI", "Journey Planner"))
        self.findRouteButton.setText(_translate("JourneyPlannerGUI", "Find Route"))
        self.lineEdit.setText(_translate("JourneyPlannerGUI", "Enter Start Location"))
        self.lineEdit_2.setText(_translate("JourneyPlannerGUI", "Enter End Location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JourneyPlannerGUI = QtWidgets.QMainWindow()
    ui = Ui_JourneyPlannerGUI()
    ui.setupUi(JourneyPlannerGUI)
    JourneyPlannerGUI.show()
    sys.exit(app.exec_())
