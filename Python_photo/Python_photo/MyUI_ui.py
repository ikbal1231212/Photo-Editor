# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\basha\OneDrive\Desktop\FSM education\FSM education\Thired Year\sixth sem\Python\finalProject_Group10\Python_photo\MyUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 874)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(790, 0, 281, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.cropbutton = QtWidgets.QPushButton(self.tab_3)
        self.cropbutton.setGeometry(QtCore.QRect(80, 70, 101, 31))
        self.cropbutton.setObjectName("cropbutton")
        self.addtxtButton = QtWidgets.QPushButton(self.tab_3)
        self.addtxtButton.setGeometry(QtCore.QRect(80, 130, 101, 31))
        self.addtxtButton.setObjectName("addtxtButton")
        self.drawButton = QtWidgets.QPushButton(self.tab_3)
        self.drawButton.setGeometry(QtCore.QRect(80, 190, 101, 31))
        self.drawButton.setObjectName("drawButton")
        self.rightbtn = QtWidgets.QPushButton(self.tab_3)
        self.rightbtn.setGeometry(QtCore.QRect(140, 250, 61, 31))
        self.rightbtn.setObjectName("rightbtn")
        self.leftbtn = QtWidgets.QPushButton(self.tab_3)
        self.leftbtn.setGeometry(QtCore.QRect(70, 250, 61, 31))
        self.leftbtn.setObjectName("leftbtn")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 0, 276, 341))
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_15 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_15.setFont(font)
        self.radioButton_15.setObjectName("radioButton_15")
        self.gridLayout_3.addWidget(self.radioButton_15, 3, 0, 1, 1)
        self.radioButton_13 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_13.setFont(font)
        self.radioButton_13.setObjectName("radioButton_13")
        self.gridLayout_3.addWidget(self.radioButton_13, 2, 0, 1, 1)
        self.radioButton_14 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_14.setFont(font)
        self.radioButton_14.setChecked(False)
        self.radioButton_14.setObjectName("radioButton_14")
        self.gridLayout_3.addWidget(self.radioButton_14, 0, 0, 1, 1)
        self.radioButton_17 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_17.setFont(font)
        self.radioButton_17.setObjectName("radioButton_17")
        self.gridLayout_3.addWidget(self.radioButton_17, 2, 1, 1, 1)
        self.radioButton_16 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_16.setFont(font)
        self.radioButton_16.setObjectName("radioButton_16")
        self.gridLayout_3.addWidget(self.radioButton_16, 3, 1, 1, 1)
        self.radioButton_18 = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_18.setFont(font)
        self.radioButton_18.setChecked(True)
        self.radioButton_18.setObjectName("radioButton_18")
        self.gridLayout_3.addWidget(self.radioButton_18, 1, 0, 1, 1)
        self.noFilterRadio = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.noFilterRadio.setFont(font)
        self.noFilterRadio.setObjectName("noFilterRadio")
        self.gridLayout_3.addWidget(self.noFilterRadio, 1, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_3)
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_7.addWidget(self.line_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.filterPropDisp1_label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.filterPropDisp1_label_2.setObjectName("filterPropDisp1_label_2")
        self.horizontalLayout_7.addWidget(self.filterPropDisp1_label_2)
        self.filterProp1_label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.filterProp1_label_2.setText("")
        self.filterProp1_label_2.setObjectName("filterProp1_label_2")
        self.horizontalLayout_7.addWidget(self.filterProp1_label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.filterProp1_slider_2 = QtWidgets.QSlider(self.groupBox_2)
        self.filterProp1_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.filterProp1_slider_2.setObjectName("filterProp1_slider_2")
        self.verticalLayout_7.addWidget(self.filterProp1_slider_2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 340, 271, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.tab_4)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(0, 440, 251, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 470, 271, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalSlider = QtWidgets.QSlider(self.tab_4)
        self.horizontalSlider.setGeometry(QtCore.QRect(0, 580, 261, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 30, 665, 789))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(17, 388, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.original_label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.original_label.sizePolicy().hasHeightForWidth())
        self.original_label.setSizePolicy(sizePolicy)
        self.original_label.setFrameShape(QtWidgets.QFrame.Box)
        self.original_label.setAlignment(QtCore.Qt.AlignCenter)
        self.original_label.setObjectName("original_label")
        self.gridLayout.addWidget(self.original_label, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 338, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 3, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1076, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuResize = QtWidgets.QMenu(self.menubar)
        self.menuResize.setObjectName("menuResize")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Image = QtWidgets.QAction(MainWindow)
        self.actionLoad_Image.setObjectName("actionLoad_Image")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionload_image = QtWidgets.QAction(MainWindow)
        self.actionload_image.setObjectName("actionload_image")
        self.actionSave_ = QtWidgets.QAction(MainWindow)
        self.actionSave_.setObjectName("actionSave_")
        self.actionUndu = QtWidgets.QAction(MainWindow)
        self.actionUndu.setObjectName("actionUndu")
        self.actionRezise_image = QtWidgets.QAction(MainWindow)
        self.actionRezise_image.setObjectName("actionRezise_image")
        self.menuFile.addAction(self.actionload_image)
        self.menuFile.addAction(self.actionSave_)
        self.menuEdit.addAction(self.actionUndu)
        self.menuResize.addAction(self.actionRezise_image)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuResize.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cropbutton.setText(_translate("MainWindow", "Crop"))
        self.addtxtButton.setText(_translate("MainWindow", "add text"))
        self.drawButton.setText(_translate("MainWindow", "draw"))
        self.rightbtn.setText(_translate("MainWindow", "trun Right"))
        self.leftbtn.setText(_translate("MainWindow", "trun left"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Edit"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Filter"))
        self.radioButton_15.setText(_translate("MainWindow", "laplacian"))
        self.radioButton_13.setText(_translate("MainWindow", "Cold"))
        self.radioButton_14.setText(_translate("MainWindow", "Median"))
        self.radioButton_17.setText(_translate("MainWindow", "warm"))
        self.radioButton_16.setText(_translate("MainWindow", "Sobal"))
        self.radioButton_18.setText(_translate("MainWindow", "Dark"))
        self.noFilterRadio.setText(_translate("MainWindow", "no Filter"))
        self.filterPropDisp1_label_2.setText(_translate("MainWindow", "Strength"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Brightness:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">blur:</span></p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Filters"))
        self.original_label.setText(_translate("MainWindow", "Original"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuResize.setTitle(_translate("MainWindow", "Resize"))
        self.actionLoad_Image.setText(_translate("MainWindow", "Load Image"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionload_image.setText(_translate("MainWindow", "load image"))
        self.actionSave_.setText(_translate("MainWindow", "Save"))
        self.actionUndu.setText(_translate("MainWindow", "Undu"))
        self.actionRezise_image.setText(_translate("MainWindow", "Rezise image"))
