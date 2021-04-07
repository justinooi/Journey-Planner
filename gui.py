from PyQt5.QtCore import QStringListModel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter
import pandas as pd


class Ui_JourneyPlannerGUI(object):
    def setupUi(self, JourneyPlannerGUI):
        JourneyPlannerGUI.setObjectName("JourneyPlannerGUI")
        JourneyPlannerGUI.resize(492, 450)
        JourneyPlannerGUI.setMinimumSize(QtCore.QSize(492, 450))
        JourneyPlannerGUI.setMaximumSize(QtCore.QSize(492, 450))
        self.centralwidget = QtWidgets.QWidget(JourneyPlannerGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.findRouteButton = QtWidgets.QPushButton(self.centralwidget)
        self.findRouteButton.setGeometry(QtCore.QRect(390, 10, 91, 51))
        self.findRouteButton.setObjectName("findRouteButton")
        self.startLocationTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.startLocationTextBox.setGeometry(QtCore.QRect(10, 10, 371, 20))
        self.startLocationTextBox.setText("")
        self.startLocationTextBox.setObjectName("startLocationTextBox")
        self.endLocationTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.endLocationTextBox.setGeometry(QtCore.QRect(10, 40, 371, 20))
        self.endLocationTextBox.setText("")
        self.endLocationTextBox.setObjectName("endLocationTextBox")
        self.transportGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.transportGroupBox.setGeometry(QtCore.QRect(10, 70, 471, 51))
        self.transportGroupBox.setObjectName("transportGroupBox")
        self.mrtRadioButton = QtWidgets.QRadioButton(self.transportGroupBox)
        self.mrtRadioButton.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.mrtRadioButton.setObjectName("mrtRadioButton")
        self.radioButton = QtWidgets.QRadioButton(self.transportGroupBox)
        self.radioButton.setGeometry(QtCore.QRect(200, 20, 61, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.transportGroupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(380, 20, 71, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.routeSelectionGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.routeSelectionGroupBox.setGeometry(QtCore.QRect(10, 130, 471, 301))
        self.routeSelectionGroupBox.setObjectName("routeSelectionGroupBox")
        self.listView = QtWidgets.QListView(self.routeSelectionGroupBox)
        self.listView.setGeometry(QtCore.QRect(10, 20, 301, 131))
        self.listView.setObjectName("listView")
        self.djisktraStopsLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.djisktraStopsLabel.setGeometry(QtCore.QRect(320, 20, 141, 16))
        self.djisktraStopsLabel.setObjectName("djisktraStopsLabel")
        self.djisktraDistLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.djisktraDistLabel.setGeometry(QtCore.QRect(320, 40, 141, 16))
        self.djisktraDistLabel.setObjectName("djisktraDistLabel")
        self.djisktraTimeLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.djisktraTimeLabel.setGeometry(QtCore.QRect(320, 60, 141, 16))
        self.djisktraTimeLabel.setObjectName("djisktraTimeLabel")
        self.djisktraTransferLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.djisktraTransferLabel.setGeometry(QtCore.QRect(320, 80, 141, 16))
        self.djisktraTransferLabel.setObjectName("djisktraTransferLabel")
        self.djisktraPlotButton = QtWidgets.QPushButton(self.routeSelectionGroupBox)
        self.djisktraPlotButton.setGeometry(QtCore.QRect(320, 100, 141, 51))
        self.djisktraPlotButton.setObjectName("djisktraPlotButton")
        self.bfsStopsLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.bfsStopsLabel.setGeometry(QtCore.QRect(320, 160, 141, 16))
        self.bfsStopsLabel.setObjectName("bfsStopsLabel")
        self.bfsDistLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.bfsDistLabel.setGeometry(QtCore.QRect(320, 180, 141, 16))
        self.bfsDistLabel.setObjectName("bfsDistLabel")
        self.listView_2 = QtWidgets.QListView(self.routeSelectionGroupBox)
        self.listView_2.setGeometry(QtCore.QRect(10, 160, 301, 131))
        self.listView_2.setObjectName("listView_2")
        self.bfsPlotButton = QtWidgets.QPushButton(self.routeSelectionGroupBox)
        self.bfsPlotButton.setGeometry(QtCore.QRect(320, 240, 141, 51))
        self.bfsPlotButton.setObjectName("bfsPlotButton")
        self.bfsTimeLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.bfsTimeLabel.setGeometry(QtCore.QRect(320, 200, 141, 16))
        self.bfsTimeLabel.setObjectName("bfsTimeLabel")
        self.bfsTransferLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.bfsTransferLabel.setGeometry(QtCore.QRect(320, 220, 141, 16))
        self.bfsTransferLabel.setObjectName("bfsTransferLabel")
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
        self.routeSelectionGroupBox.setTitle(_translate("JourneyPlannerGUI", "Route Selection"))
        self.djisktraStopsLabel.setText(_translate("JourneyPlannerGUI", "djisktraStopsLabel"))
        self.djisktraDistLabel.setText(_translate("JourneyPlannerGUI", "djisktraDistLabel"))
        self.djisktraTimeLabel.setText(_translate("JourneyPlannerGUI", "djisktraTimeLabel"))
        self.djisktraTransferLabel.setText(_translate("JourneyPlannerGUI", "djisktraTransferLabel"))
        self.djisktraPlotButton.setText(_translate("JourneyPlannerGUI", "Plot"))
        self.bfsStopsLabel.setText(_translate("JourneyPlannerGUI", "bfsStopsLabel"))
        self.bfsDistLabel.setText(_translate("JourneyPlannerGUI", "bfsDistLabel"))
        self.bfsPlotButton.setText(_translate("JourneyPlannerGUI", "Plot"))
        self.bfsTimeLabel.setText(_translate("JourneyPlannerGUI", "bfsTimeLabel"))
        self.bfsTransferLabel.setText(_translate("JourneyPlannerGUI", "bfsTransferLabel"))

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
