from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QCompleter, QListWidgetItem
from dijkstra_bus import dijkstra_bus
from dijkstra_mrt import dijkstra_mrt
from bfs_bus import bfs_bus
from bfs_mrt import bfs_mrt
from graph_plot import plot_graph
import pandas as pd


# Class for GUI object running PyQt
class Ui_JourneyPlannerGUI(object):

    # Function to setup UI objects.
    def setupUi(self, JourneyPlannerGUI):

        # UI Objects & Properties

        # Window Size
        JourneyPlannerGUI.setObjectName("JourneyPlannerGUI")
        JourneyPlannerGUI.resize(992, 450)
        JourneyPlannerGUI.setMinimumSize(QtCore.QSize(992, 450))
        JourneyPlannerGUI.setMaximumSize(QtCore.QSize(992, 450))

        # Create central widget to hold other widgets.
        self.centralwidget = QtWidgets.QWidget(JourneyPlannerGUI)
        self.centralwidget.setObjectName("centralwidget")

        # GUI for user input and find route button
        self.findRouteButton = QtWidgets.QPushButton(self.centralwidget)
        self.findRouteButton.setGeometry(QtCore.QRect(390, 10, 91, 51))
        self.findRouteButton.setObjectName("findRouteButton")
        self.findRouteButton.setStyleSheet("background-color:#44c767;\n"
                                           "	                                            border-radius:6px;\n"
                                           "	                                            border:1px solid #18ab29;\n"
                                           "	                                            display:inline-block;\n"
                                           "                                                cursor:pointer;\n"
                                           "                                                color:#000000;\n"
                                           "                                                font-family:Arial;\n"
                                           "                                                font-size:10px;\n"
                                           "                                                font-weight:bold;\n"
                                           "                                                text-decoration:none;\n"
                                           "text-shadow:0px 1px 0px #2f6627;")
        self.startLocationTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.startLocationTextBox.setGeometry(QtCore.QRect(10, 10, 371, 20))
        self.startLocationTextBox.setText("")
        self.startLocationTextBox.setObjectName("startLocationTextBox")
        self.endLocationTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.endLocationTextBox.setGeometry(QtCore.QRect(10, 40, 371, 20))
        self.endLocationTextBox.setText("")
        self.endLocationTextBox.setObjectName("endLocationTextBox")

        # Group Box to choose transport mode elements
        self.transportGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.transportGroupBox.setGeometry(QtCore.QRect(10, 70, 471, 51))
        self.transportGroupBox.setObjectName("transportGroupBox")
        self.mrtRadioButton = QtWidgets.QRadioButton(self.transportGroupBox)
        self.mrtRadioButton.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.mrtRadioButton.setObjectName("mrtRadioButton")
        self.busRadioButton = QtWidgets.QRadioButton(self.transportGroupBox)
        self.busRadioButton.setGeometry(QtCore.QRect(200, 20, 61, 17))
        self.busRadioButton.setObjectName("busRadioButton")

        # Group Box for route selection elements
        self.routeSelectionGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.routeSelectionGroupBox.setGeometry(QtCore.QRect(10, 130, 471, 301))
        self.routeSelectionGroupBox.setObjectName("routeSelectionGroupBox")
        self.listView = QtWidgets.QListWidget(self.routeSelectionGroupBox)
        self.listView.setGeometry(QtCore.QRect(10, 20, 301, 131))
        self.listView.setObjectName("listView")
        self.dijkstraStopsLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.dijkstraStopsLabel.setGeometry(QtCore.QRect(320, 20, 141, 16))
        self.dijkstraStopsLabel.setObjectName("dijkstraStopsLabel")
        self.dijkstraDistLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.dijkstraDistLabel.setGeometry(QtCore.QRect(320, 40, 141, 16))
        self.dijkstraDistLabel.setObjectName("dijkstraDistLabel")
        self.dijkstraTimeLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.dijkstraTimeLabel.setGeometry(QtCore.QRect(320, 60, 141, 16))
        self.dijkstraTimeLabel.setObjectName("dijkstraTimeLabel")
        self.dijkstraTransferLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.dijkstraTransferLabel.setGeometry(QtCore.QRect(320, 80, 141, 16))
        self.dijkstraTransferLabel.setObjectName("dijkstraTransferLabel")
        self.dijkstraPlotButton = QtWidgets.QPushButton(self.routeSelectionGroupBox)
        self.dijkstraPlotButton.setGeometry(QtCore.QRect(320, 100, 141, 51))
        self.dijkstraPlotButton.setObjectName("dijkstraPlotButton")
        self.dijkstraPlotButton.setStyleSheet("background-color:#FE1F16;\n"
                                              "	                                            border-radius:6px;\n"
                                              "	                                            border:1px solid #800000;\n"
                                              "	                                            display:inline-block;\n"
                                              "                                                cursor:pointer;\n"
                                              "                                                color:#000000;\n"
                                              "                                                font-family:Arial;\n"
                                              "                                                font-size:10px;\n"
                                              "                                                font-weight:bold;\n"
                                              "                                                text-decoration:none;\n"
                                              "text-shadow:0px 1px 0px #2f6627;")
        self.bfsStopsLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.bfsStopsLabel.setGeometry(QtCore.QRect(320, 160, 141, 16))
        self.bfsStopsLabel.setObjectName("bfsStopsLabel")
        self.listView_2 = QtWidgets.QListWidget(self.routeSelectionGroupBox)
        self.listView_2.setGeometry(QtCore.QRect(10, 160, 301, 131))
        self.listView_2.setObjectName("listView_2")
        self.bfsPlotButton = QtWidgets.QPushButton(self.routeSelectionGroupBox)
        self.bfsPlotButton.setGeometry(QtCore.QRect(320, 240, 141, 51))
        self.bfsPlotButton.setObjectName("bfsPlotButton")
        self.bfsPlotButton.setStyleSheet("background-color:#0066ff;\n"
                                         "	                                            border-radius:6px;\n"
                                         "	                                            border:1px solid #000099;\n"
                                         "	                                            display:inline-block;\n"
                                         "                                                cursor:pointer;\n"
                                         "                                                color:#000000;\n"
                                         "                                                font-family:Arial;\n"
                                         "                                                font-size:10px;\n"
                                         "                                                font-weight:bold;\n"
                                         "                                                text-decoration:none;\n"
                                         "text-shadow:0px 1px 0px #2f6627;")
        self.bfsTransferLabel = QtWidgets.QLabel(self.routeSelectionGroupBox)
        self.bfsTransferLabel.setGeometry(QtCore.QRect(320, 180, 141, 16))
        self.bfsTransferLabel.setObjectName("bfsTransferLabel")

        # Web HTML View widget set up
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(490, 10, 491, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.htmlView = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.htmlView.setContentsMargins(0, 0, 0, 0)
        self.htmlView.setObjectName("htmlView")
        self.webEngineView = QWebEngineView()
        self.htmlView.addWidget(self.webEngineView)

        with open('default.html', 'r') as f:
            html = f.read()
            self.webEngineView.setHtml(html)

        JourneyPlannerGUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(JourneyPlannerGUI)
        self.statusbar.setObjectName("statusbar")
        JourneyPlannerGUI.setStatusBar(self.statusbar)

        # On Click Events for buttons.

        # On click, find route.
        self.findRouteButton.clicked.connect(lambda: self.findRoute())

        # On click, plot dijkstra graph.
        self.dijkstraPlotButton.clicked.connect(lambda: self.loadPage('dijkstra'))

        # On click, plot BFS graph.
        self.bfsPlotButton.clicked.connect(lambda: self.loadPage('bfs'))

        self.retranslateUi(JourneyPlannerGUI)
        QtCore.QMetaObject.connectSlotsByName(JourneyPlannerGUI)

    # Function to set text for elements of GUI.
    def retranslateUi(self, JourneyPlannerGUI):
        _translate = QtCore.QCoreApplication.translate
        JourneyPlannerGUI.setWindowTitle(_translate("JourneyPlannerGUI", "Journey Planner"))
        self.findRouteButton.setText(_translate("JourneyPlannerGUI", "Find Route"))
        self.startLocationTextBox.setPlaceholderText(_translate("JourneyPlannerGUI", "Enter Start Location"))
        self.endLocationTextBox.setPlaceholderText(_translate("JourneyPlannerGUI", "Enter End Location"))
        self.transportGroupBox.setTitle(_translate("JourneyPlannerGUI", "Mode of Transport"))
        self.mrtRadioButton.setText(_translate("JourneyPlannerGUI", "MRT Only"))
        self.busRadioButton.setText(_translate("JourneyPlannerGUI", "Bus Only"))
        self.routeSelectionGroupBox.setTitle(_translate("JourneyPlannerGUI", "Route Selection"))
        self.dijkstraStopsLabel.setText(_translate("JourneyPlannerGUI", ""))
        self.dijkstraDistLabel.setText(_translate("JourneyPlannerGUI", ""))
        self.dijkstraTimeLabel.setText(_translate("JourneyPlannerGUI", ""))
        self.dijkstraTransferLabel.setText(_translate("JourneyPlannerGUI", ""))
        self.dijkstraPlotButton.setText(_translate("JourneyPlannerGUI", "Plot - Dijkstra"))
        self.bfsStopsLabel.setText(_translate("JourneyPlannerGUI", ""))
        self.bfsPlotButton.setText(_translate("JourneyPlannerGUI", "Plot - BFS"))
        self.bfsTransferLabel.setText(_translate("JourneyPlannerGUI", ""))

    # Auto complete function.
    def getAutoCompleteData(self):

        # Substrings to add to each stop / station to differentiate.
        mrt_string = " (MRT Station)"
        bus_string = " (Bus Stop)"

        # Read json into DataFrame.
        train_data = pd.read_json("mrtstops.json")

        # Convert DF to list.
        station_list = train_data['Description'].values.tolist()

        # List comprehension, add mrt string to all mrt stations.
        station_list = [s + mrt_string for s in station_list]

        # Read json into Data Frame
        bus_data = pd.read_json("busstops.json")

        # Convert DF to list.
        bus_list = bus_data['Description'].values.tolist()

        # List comprehension, add bus string to all bus stops.
        bus_list = [s + bus_string for s in bus_list]

        # Add both lists together.
        full_list = station_list + bus_list
        full_list = list(dict.fromkeys(full_list))

        # Return full list.
        return full_list

    def loadPage(self, algorithm):

        # Create new graph class.
        graph_object = plot_graph()

        # Check which algorithm is chosen and which mode of transportation is chosen.
        if self.mrtRadioButton.isChecked() and algorithm == "dijkstra":

            start_location = self.startLocationTextBox.text()
            start_location = start_location.replace(" (MRT Station)", "")
            end_location = self.endLocationTextBox.text()
            end_location = end_location.replace(" (MRT Station)", "")

            # Plot MRT using Dijkstra.
            graph_object.mrt_dijs(start_location, end_location)

            # Load plot into HTML view.
            with open('dij_mrt.html', 'r') as f:
                html = f.read()
                self.webEngineView.setHtml(html)

        # Dijkstra for bus.
        elif self.busRadioButton.isChecked() and algorithm == "dijkstra":

            start_location = self.startLocationTextBox.text()
            start_location = start_location.replace(" (Bus Stop)", "")
            end_location = self.endLocationTextBox.text()
            end_location = end_location.replace(" (Bus Stop)", "")

            # Plot Bus using Dijkstra
            graph_object.bus_dijs(start_location, end_location)

            # Load plot into HTML view.
            with open('dij_bus.html', 'r') as f:
                html = f.read()
                self.webEngineView.setHtml(html)

        # BFS For MRT
        elif self.mrtRadioButton.isChecked() and algorithm == "bfs":

            start_location = self.startLocationTextBox.text()
            start_location = start_location.replace(" (MRT Station)", "")
            end_location = self.endLocationTextBox.text()
            end_location = end_location.replace(" (MRT Station)", "")

            # Plot MRT using BFS
            graph_object.mrt_bfs(start_location, end_location)

            # Load HTML into view.
            with open('mrt_bfs.html', 'r') as f:
                html = f.read()
                self.webEngineView.setHtml(html)

        # BFS for Bus
        elif self.busRadioButton.isChecked() and algorithm == "bfs":

            start_location = self.startLocationTextBox.text()
            start_location = start_location.replace(" (Bus Stop)", "")
            end_location = self.endLocationTextBox.text()
            end_location = end_location.replace(" (Bus Stop)", "")

            # Plot Bus using BFS.
            graph_object.bus_bfs(start_location, end_location)

            # Load HTML into view.
            with open('bus_bfs.html', 'r') as f:
                html = f.read()
                self.webEngineView.setHtml(html)

    def findRoute(self):

        # Check which mode of transportation is done.
        if self.mrtRadioButton.isChecked():

            start_location = self.startLocationTextBox.text()
            start_location = start_location.replace(" (MRT Station)", "")
            end_location = self.endLocationTextBox.text()
            end_location = end_location.replace(" (MRT Station)", "")

            # Error checking.
            if "(Bus Stop)" in start_location or "(Bus Stop)" in end_location:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('You cannot choose bus stops for MRT route!')
                error_dialog.exec_()
                return None
            elif start_location == "" or end_location == "":
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('You cannot leave blanks in start or end location!')
                error_dialog.exec_()
                return None

            # Reset list view.
            self.listView.clear()
            self.listView_2.clear()

            # Load both dijkstra and bfs routes.
            results = dijkstra_mrt(start_location, end_location)
            results2 = bfs_mrt(start_location, end_location)

            self.bfsStopsLabel.setText("Stops: " + str(results2[1]))
            if results2[2] == 0:
                self.bfsTransferLabel.setText("Transfers Needed: 1")
            else:
                self.bfsTransferLabel.setText("Transfers Needed: " + str(results2[2]))

            # Update list view with route information - bfs
            for j in range(len(results2[0])):
                if results2[0][j][1] == 0:
                    results2[0][j] = (results2[0][j][0], results2[0][j + 1][1], results2[0][j][2])
                string_builder = str(results2[0][j][2]) + ' - ' + str(results2[0][j][1])
                item = QListWidgetItem(string_builder)
                self.listView_2.addItem(item)

            # Update display with route information - dijkstra
            self.dijkstraStopsLabel.setText("Stops: " + str(results[1]))
            self.dijkstraDistLabel.setText("Distance: ~" + str(round(results[2])) + "km")
            self.dijkstraTimeLabel.setText("Time Needed: ~" + str(round(results[3])) + "mins")
            self.dijkstraTransferLabel.setText("Transfers Needed: " + str(results[4]))

            # Update list view with route information - dijkstra
            for i in range(len(results[0])):
                if results[0][i][1] == 0:
                    results[0][i] = (results[0][i][0], results[0][i + 1][1], results[0][i][2])
                string_builder = str(results[0][i][2]) + ' - ' + str(results[0][i][1])
                item = QListWidgetItem(string_builder)
                self.listView.addItem(item)

        elif self.busRadioButton.isChecked():

            start_location = self.startLocationTextBox.text()
            start_location = start_location.replace(" (Bus Stop)", "")
            end_location = self.endLocationTextBox.text()
            end_location = end_location.replace(" (Bus Stop)", "")

            # Error checking.
            if "(MRT Station)" in start_location or "(MRT Station)" in end_location:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('You cannot choose MRT station for bus routes!')
                error_dialog.exec_()
                return None
            elif start_location == "" or end_location == "":
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('You cannot leave blanks in start or end location!')
                error_dialog.exec_()
                return None

            # Reset list view.
            self.listView.clear()
            self.listView_2.clear()

            # Call BFS & dijkstra for bus.
            results = dijkstra_bus(start_location, end_location)
            results2 = bfs_bus(start_location, end_location)

            # Update elements with route information.
            self.dijkstraStopsLabel.setText("Stops: " + str(results[1]))
            self.dijkstraDistLabel.setText("Distance: " + str(results[2]))
            self.dijkstraTimeLabel.setText("Time Needed: " + str(results[3]))
            self.dijkstraTransferLabel.setText("Transfers Needed: " + str(results[4]))

            for i in range(len(results[0])):
                if results[0][i][1] == 0:
                    results[0][i] = (results[0][i][0], results[0][i + 1][1], results[0][i][2])
                string_builder = str(results[0][i][2]) + ' - ' + str(results[0][i][1])
                item = QListWidgetItem(string_builder)
                self.listView.addItem(item)

            self.bfsStopsLabel.setText("Stops: " + str(results2[1]))
            self.bfsTransferLabel.setText("Transfers: " + str(results2[2]))

            for j in range(len(results2[0])):
                if results2[0][j][1] == 0:
                    results2[0][j] = (results2[0][j][0], results2[0][j + 1][1], results2[0][j][2])
                string_builder = str(results2[0][j][2]) + ' - ' + str(results2[0][j][1])
                item = QListWidgetItem(string_builder)
                self.listView_2.addItem(item)

        # Error catch - check if user chose a mode of transportation.
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Please select mode of transportation!')
            error_dialog.exec_()


# Main Driver
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
