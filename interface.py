# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(898, 518)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet("background-color:rgb(250, 243, 223)")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leaf_frame_container = QtWidgets.QFrame(Form)
        self.leaf_frame_container.setMinimumSize(QtCore.QSize(0, 0))
        self.leaf_frame_container.setMaximumSize(QtCore.QSize(200, 16777215))
        self.leaf_frame_container.setStyleSheet("background-color:rgb(212, 197, 138)")
        self.leaf_frame_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leaf_frame_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leaf_frame_container.setObjectName("leaf_frame_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leaf_frame_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.leaf_frame = QtWidgets.QFrame(self.leaf_frame_container)
        self.leaf_frame.setMinimumSize(QtCore.QSize(198, 0))
        self.leaf_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leaf_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leaf_frame.setObjectName("leaf_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.leaf_frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.spisok_knig = QtWidgets.QListWidget(self.leaf_frame)
        self.spisok_knig.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.spisok_knig.setObjectName("spisok_knig")
        self.horizontalLayout_6.addWidget(self.spisok_knig)
        self.verticalLayout_2.addWidget(self.leaf_frame)
        self.horizontalLayout.addWidget(self.leaf_frame_container, 0, QtCore.Qt.AlignLeft)
        self.main_frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.main_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tool_frame = QtWidgets.QFrame(self.main_frame)
        self.tool_frame.setStyleSheet("background-color:rgb(212, 197, 138)")
        self.tool_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tool_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tool_frame.setObjectName("tool_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tool_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tools_frame = QtWidgets.QFrame(self.tool_frame)
        self.tools_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tools_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tools_frame.setObjectName("tools_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tools_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listclose_but = QtWidgets.QPushButton(self.tools_frame)
        self.listclose_but.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-font-arrow-left-3916840.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.listclose_but.setIcon(icon)
        self.listclose_but.setObjectName("listclose_but")
        self.horizontalLayout_5.addWidget(self.listclose_but, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.remove_but = QtWidgets.QPushButton(self.tools_frame)
        self.remove_but.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-font-minus-3917755.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_but.setIcon(icon1)
        self.remove_but.setObjectName("remove_but")
        self.horizontalLayout_5.addWidget(self.remove_but)
        self.add_but = QtWidgets.QPushButton(self.tools_frame)
        self.add_but.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-font-plus-3917757.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_but.setIcon(icon2)
        self.add_but.setObjectName("add_but")
        self.horizontalLayout_5.addWidget(self.add_but)
        self.fav_but = QtWidgets.QPushButton(self.tools_frame)
        self.fav_but.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-font-bookmark-3916594.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fav_but.setIcon(icon3)
        self.fav_but.setObjectName("fav_but")
        self.horizontalLayout_5.addWidget(self.fav_but, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.tools_frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.window_tools_frame = QtWidgets.QFrame(self.tool_frame)
        self.window_tools_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.window_tools_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.window_tools_frame.setObjectName("window_tools_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.window_tools_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.roll_up_but = QtWidgets.QPushButton(self.window_tools_frame)
        self.roll_up_but.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-font-arrow-up-left-8540384.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.roll_up_but.setIcon(icon4)
        self.roll_up_but.setObjectName("roll_up_but")
        self.horizontalLayout_4.addWidget(self.roll_up_but, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.size_but = QtWidgets.QPushButton(self.window_tools_frame)
        self.size_but.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-font-arrow-up-right-and-arrow-down-left-from-center-8540385.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.size_but.setIcon(icon5)
        self.size_but.setObjectName("size_but")
        self.horizontalLayout_4.addWidget(self.size_but, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.close_but = QtWidgets.QPushButton(self.window_tools_frame)
        self.close_but.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-font-cross-3917759.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_but.setIcon(icon6)
        self.close_but.setObjectName("close_but")
        self.horizontalLayout_4.addWidget(self.close_but, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.window_tools_frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.tool_frame)
        self.main_page_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_page_frame.sizePolicy().hasHeightForWidth())
        self.main_page_frame.setSizePolicy(sizePolicy)
        self.main_page_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_page_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_page_frame.setObjectName("main_page_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.main_page_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.leftslide_frame = QtWidgets.QFrame(self.main_page_frame)
        self.leftslide_frame.setStyleSheet("background-color:rgb(212, 197, 138)")
        self.leftslide_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftslide_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftslide_frame.setObjectName("leftslide_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.leftslide_frame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.leftslide = QtWidgets.QPushButton(self.leftslide_frame)
        self.leftslide.setMinimumSize(QtCore.QSize(0, 0))
        self.leftslide.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-font-angle-left-3916931.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftslide.setIcon(icon7)
        self.leftslide.setObjectName("leftslide")
        self.horizontalLayout_10.addWidget(self.leftslide)
        self.horizontalLayout_8.addWidget(self.leftslide_frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.page_frame = QtWidgets.QFrame(self.main_page_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_frame.sizePolicy().hasHeightForWidth())
        self.page_frame.setSizePolicy(sizePolicy)
        self.page_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_frame.setObjectName("page_frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.page_frame)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.scrollArea = QtWidgets.QScrollArea(self.page_frame)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 632, 458))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.page_pixmap = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.page_pixmap.setMinimumSize(QtCore.QSize(0, 0))
        self.page_pixmap.setText("")
        self.page_pixmap.setScaledContents(False)
        self.page_pixmap.setAlignment(QtCore.Qt.AlignCenter)
        self.page_pixmap.setObjectName("page_pixmap")
        self.verticalLayout_3.addWidget(self.page_pixmap)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.addWidget(self.scrollArea)
        self.horizontalLayout_8.addWidget(self.page_frame)
        self.rightslide_frame = QtWidgets.QFrame(self.main_page_frame)
        self.rightslide_frame.setStyleSheet("background-color:rgb(212, 197, 138)")
        self.rightslide_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightslide_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightslide_frame.setObjectName("rightslide_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.rightslide_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.rightslide = QtWidgets.QPushButton(self.rightslide_frame)
        self.rightslide.setMinimumSize(QtCore.QSize(0, 0))
        self.rightslide.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-font-angle-right-3916925.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightslide.setIcon(icon8)
        self.rightslide.setObjectName("rightslide")
        self.horizontalLayout_9.addWidget(self.rightslide)
        self.horizontalLayout_8.addWidget(self.rightslide_frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.main_page_frame)
        self.page_number_frame = QtWidgets.QFrame(self.main_frame)
        self.page_number_frame.setStyleSheet("background-color:rgb(212, 197, 138)")
        self.page_number_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_number_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_number_frame.setObjectName("page_number_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_number_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.page_number_label = QtWidgets.QLabel(self.page_number_frame)
        self.page_number_label.setMaximumSize(QtCore.QSize(50, 30))
        self.page_number_label.setObjectName("page_number_label")
        self.horizontalLayout_7.addWidget(self.page_number_label)
        self.page_number_LineEdit = QtWidgets.QLineEdit(self.page_number_frame)
        self.page_number_LineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.page_number_LineEdit.setObjectName("page_number_LineEdit")
        self.horizontalLayout_7.addWidget(self.page_number_LineEdit)
        self.page_number_but = QtWidgets.QPushButton(self.page_number_frame)
        self.page_number_but.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/free-icon-font-check-3917749.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.page_number_but.setIcon(icon9)
        self.page_number_but.setObjectName("page_number_but")
        self.horizontalLayout_7.addWidget(self.page_number_but, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.size_grip = QtWidgets.QFrame(self.page_number_frame)
        self.size_grip.setMaximumSize(QtCore.QSize(20, 20))
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_7.addWidget(self.size_grip, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.page_number_frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.main_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.page_number_label.setText(_translate("Form", "Page: "))
import icons_rc