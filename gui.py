from PyQt5.QtCore import QStringListModel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PyQt5.QtWidgets import QCompleter


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
        self.startLocationTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.startLocationTextBox.setGeometry(QtCore.QRect(10, 10, 371, 20))
        self.startLocationTextBox.setObjectName("startLocationTextBox")
        self.endLocationTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.endLocationTextBox.setGeometry(QtCore.QRect(10, 40, 371, 20))
        self.endLocationTextBox.setObjectName("endLocationTextBox")
        self.widget = QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 130, 471, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.transportGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.transportGroupBox.setGeometry(QtCore.QRect(10, 70, 471, 51))
        self.transportGroupBox.setObjectName("transportGroupBox")
        self.mrtRadioButton = QtWidgets.QRadioButton(self.transportGroupBox)
        self.mrtRadioButton.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.mrtRadioButton.setObjectName("mrtRadioButton")
        self.radioButton = QtWidgets.QRadioButton(self.transportGroupBox)
        self.radioButton.setGeometry(QtCore.QRect(190, 20, 81, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.transportGroupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(380, 20, 71, 17))
        self.radioButton_2.setObjectName("radioButton_2")
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
        self.startLocationTextBox.setPlaceholderText(_translate("JourneyPlannerGUI", "Enter Start Location"))
        self.endLocationTextBox.setPlaceholderText(_translate("JourneyPlannerGUI", "Enter End Location"))
        self.transportGroupBox.setTitle(_translate("JourneyPlannerGUI", "Mode of Transport"))
        self.mrtRadioButton.setText(_translate("JourneyPlannerGUI", "MRT Only"))
        self.radioButton.setText(_translate("JourneyPlannerGUI", "Bus Only"))
        self.radioButton_2.setText(_translate("JourneyPlannerGUI", "MRT + Bus"))

    def getAutoCompleteData(self):

        mrt_string = " (MRT Station)"
        bus_string = " (Bus Stop)"

        train_data = pd.read_json("Algorithm & API calls\mrtstops.json")
        station_list = train_data['Description'].values.tolist()
        station_list = [s + mrt_string for s in station_list]

        bus_data = pd.read_json("Algorithm & API calls\\busstops.json")
        bus_list = bus_data['Description'].values.tolist()
        bus_list = [s + bus_string for s in bus_list]

        full_list = station_list + bus_list
        full_list = list(dict.fromkeys(full_list))

        return full_list

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    JourneyPlannerGUI = QtWidgets.QMainWindow()
    ui = Ui_JourneyPlannerGUI()
    ui.setupUi(JourneyPlannerGUI)

    mrt_list = ui.getAutoCompleteData()
    completer = QCompleter(mrt_list)
    ui.startLocationTextBox.setCompleter(completer)
    ui.endLocationTextBox.setCompleter(completer)

    JourneyPlannerGUI.show()
    sys.exit(app.exec_())
