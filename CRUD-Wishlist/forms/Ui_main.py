# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Boruto\Desktop\Chio\github\CRUD-Wishlist\CRUD-Wishlist\forms\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(750, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(750, 600))
        MainWindow.setBaseSize(QtCore.QSize(700, 450))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(129, 129, 129))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/icon_window"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setToolTipDuration(0)
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(129, 129, 129);")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        MainWindow.setWindowFilePath("")
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-image: none;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.HeaderLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HeaderLabel.sizePolicy().hasHeightForWidth())
        self.HeaderLabel.setSizePolicy(sizePolicy)
        self.HeaderLabel.setMinimumSize(QtCore.QSize(761, 101))
        self.HeaderLabel.setMaximumSize(QtCore.QSize(16777215, 101))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.HeaderLabel.setFont(font)
        self.HeaderLabel.setAutoFillBackground(False)
        self.HeaderLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.715909, y1:0.744, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.517045 rgba(129, 129, 129, 255), stop:0.846591 rgba(129, 129, 129, 255));\n"
"font: 50pt \"Impact\";\n"
"color: qlineargradient(spread:pad, x1:0.715909, y1:0.744, x2:1, y2:0, stop:0 rgba(223, 223, 223, 255), stop:0.517045 rgba(189, 189, 189, 255), stop:0.846591 rgba(212, 212, 212, 255));\n"
"border-bottom: 1px solid black;")
        self.HeaderLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.HeaderLabel.setTextFormat(QtCore.Qt.PlainText)
        self.HeaderLabel.setScaledContents(False)
        self.HeaderLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HeaderLabel.setIndent(0)
        self.HeaderLabel.setObjectName("HeaderLabel")
        self.verticalLayout_3.addWidget(self.HeaderLabel)
        self.FrameMenus = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrameMenus.sizePolicy().hasHeightForWidth())
        self.FrameMenus.setSizePolicy(sizePolicy)
        self.FrameMenus.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.FrameMenus.setObjectName("FrameMenus")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.FrameMenus)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(20, 0, 20, 20)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PanelElements = QtWidgets.QFrame(self.FrameMenus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PanelElements.sizePolicy().hasHeightForWidth())
        self.PanelElements.setSizePolicy(sizePolicy)
        self.PanelElements.setMinimumSize(QtCore.QSize(211, 400))
        self.PanelElements.setMaximumSize(QtCore.QSize(211, 16777215))
        self.PanelElements.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.PanelElements.setStyleSheet("*{background-color: rgb(225, 225, 225);}\n"
"#PanelElements {border: 1px solid black;}")
        self.PanelElements.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PanelElements.setFrameShadow(QtWidgets.QFrame.Plain)
        self.PanelElements.setObjectName("PanelElements")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PanelElements)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 3, -1, -1)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.PanelElements)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(170, 20))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ButtonsFrame = QtWidgets.QFrame(self.PanelElements)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonsFrame.sizePolicy().hasHeightForWidth())
        self.ButtonsFrame.setSizePolicy(sizePolicy)
        self.ButtonsFrame.setMinimumSize(QtCore.QSize(193, 0))
        self.ButtonsFrame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ButtonsFrame.setTabletTracking(False)
        self.ButtonsFrame.setStyleSheet("\n"
"color: rgb(1, 175, 223);\n"
"background-color: rgb(250, 250, 250);")
        self.ButtonsFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.ButtonsFrame.setObjectName("ButtonsFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ButtonsFrame)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(19)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.AddButton = QtWidgets.QPushButton(self.ButtonsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/icon_add"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddButton.setIcon(icon1)
        self.AddButton.setIconSize(QtCore.QSize(32, 32))
        self.AddButton.setAutoDefault(False)
        self.AddButton.setDefault(True)
        self.AddButton.setFlat(False)
        self.AddButton.setObjectName("AddButton")
        self.horizontalLayout.addWidget(self.AddButton)
        self.EditButton = QtWidgets.QPushButton(self.ButtonsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EditButton.sizePolicy().hasHeightForWidth())
        self.EditButton.setSizePolicy(sizePolicy)
        self.EditButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/icon_edit"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EditButton.setIcon(icon2)
        self.EditButton.setIconSize(QtCore.QSize(32, 32))
        self.EditButton.setAutoDefault(False)
        self.EditButton.setDefault(True)
        self.EditButton.setFlat(False)
        self.EditButton.setObjectName("EditButton")
        self.horizontalLayout.addWidget(self.EditButton)
        self.DeleteButton = QtWidgets.QPushButton(self.ButtonsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DeleteButton.sizePolicy().hasHeightForWidth())
        self.DeleteButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        self.DeleteButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/icon_remove"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteButton.setIcon(icon3)
        self.DeleteButton.setIconSize(QtCore.QSize(32, 32))
        self.DeleteButton.setAutoRepeatInterval(100)
        self.DeleteButton.setAutoDefault(True)
        self.DeleteButton.setDefault(True)
        self.DeleteButton.setFlat(False)
        self.DeleteButton.setObjectName("DeleteButton")
        self.horizontalLayout.addWidget(self.DeleteButton)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 4)
        self.verticalLayout.addWidget(self.ButtonsFrame)
        self.listView = QtWidgets.QListView(self.PanelElements)
        self.listView.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setMinimumSize(QtCore.QSize(170, 0))
        self.listView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listView.setAutoFillBackground(False)
        self.listView.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.listView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setDragEnabled(True)
        self.listView.setDragDropOverwriteMode(False)
        self.listView.setAlternatingRowColors(True)
        self.listView.setTextElideMode(QtCore.Qt.ElideNone)
        self.listView.setMovement(QtWidgets.QListView.Free)
        self.listView.setFlow(QtWidgets.QListView.TopToBottom)
        self.listView.setResizeMode(QtWidgets.QListView.Adjust)
        self.listView.setModelColumn(0)
        self.listView.setUniformItemSizes(False)
        self.listView.setBatchSize(99)
        self.listView.setWordWrap(False)
        self.listView.setSelectionRectVisible(False)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.horizontalLayout_4.addWidget(self.PanelElements)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.InformationBox = QtWidgets.QFrame(self.FrameMenus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InformationBox.sizePolicy().hasHeightForWidth())
        self.InformationBox.setSizePolicy(sizePolicy)
        self.InformationBox.setMinimumSize(QtCore.QSize(500, 400))
        font = QtGui.QFont()
        font.setKerning(True)
        self.InformationBox.setFont(font)
        self.InformationBox.setToolTip("")
        self.InformationBox.setStyleSheet("#InformationBox {border: 1px solid black; border-right: 1px solid transparent;}")
        self.InformationBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InformationBox.setFrameShadow(QtWidgets.QFrame.Plain)
        self.InformationBox.setObjectName("InformationBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.InformationBox)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ImageLayots = QtWidgets.QWidget(self.InformationBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ImageLayots.sizePolicy().hasHeightForWidth())
        self.ImageLayots.setSizePolicy(sizePolicy)
        self.ImageLayots.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ImageLayots.setStyleSheet("* {background-color: rgb(225, 225, 225);}\n"
"#ImageLayouts {border: 0px solid transparent; \n"
"border-top:0px solid transparent;}")
        self.ImageLayots.setObjectName("ImageLayots")
        self.ImageLayout = QtWidgets.QHBoxLayout(self.ImageLayots)
        self.ImageLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ImageLayout.setContentsMargins(0, 0, 0, 0)
        self.ImageLayout.setSpacing(8)
        self.ImageLayout.setObjectName("ImageLayout")
        self.ImageName = QtWidgets.QLabel(self.ImageLayots)
        self.ImageName.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageName.sizePolicy().hasHeightForWidth())
        self.ImageName.setSizePolicy(sizePolicy)
        self.ImageName.setMinimumSize(QtCore.QSize(150, 150))
        self.ImageName.setMaximumSize(QtCore.QSize(150, 123123))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.ImageName.setFont(font)
        self.ImageName.setTabletTracking(False)
        self.ImageName.setAcceptDrops(False)
        self.ImageName.setStatusTip("")
        self.ImageName.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ImageName.setAutoFillBackground(False)
        self.ImageName.setStyleSheet("text-decoration: underline;\n"
"border: 1px solid transparent;\n"
"border-top: 0px solid black;")
        self.ImageName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ImageName.setLineWidth(1)
        self.ImageName.setMidLineWidth(0)
        self.ImageName.setScaledContents(False)
        self.ImageName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImageName.setWordWrap(True)
        self.ImageName.setIndent(-1)
        self.ImageName.setOpenExternalLinks(False)
        self.ImageName.setObjectName("ImageName")
        self.ImageLayout.addWidget(self.ImageName)
        self.PhotoFrame = QtWidgets.QFrame(self.ImageLayots)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PhotoFrame.sizePolicy().hasHeightForWidth())
        self.PhotoFrame.setSizePolicy(sizePolicy)
        self.PhotoFrame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.PhotoFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PhotoFrame.setStyleSheet("#PhotoFrame{border: 1px solid black;\n"
"border-bottom: 1px solid transparent;\n"
"border-top: 0px solid transparent;}")
        self.PhotoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PhotoFrame.setMidLineWidth(0)
        self.PhotoFrame.setObjectName("PhotoFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.PhotoFrame)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.PhotoLabel = QtWidgets.QLabel(self.PhotoFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PhotoLabel.sizePolicy().hasHeightForWidth())
        self.PhotoLabel.setSizePolicy(sizePolicy)
        self.PhotoLabel.setMinimumSize(QtCore.QSize(100, 100))
        self.PhotoLabel.setMaximumSize(QtCore.QSize(1000, 1000))
        self.PhotoLabel.setAutoFillBackground(False)
        self.PhotoLabel.setStyleSheet("color: rgb(229, 229, 229);\n"
"background-color: rgb(62, 62, 62);")
        self.PhotoLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.PhotoLabel.setLineWidth(2)
        self.PhotoLabel.setTextFormat(QtCore.Qt.AutoText)
        self.PhotoLabel.setScaledContents(True)
        self.PhotoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PhotoLabel.setWordWrap(False)
        self.PhotoLabel.setIndent(1)
        self.PhotoLabel.setObjectName("PhotoLabel")
        self.gridLayout.addWidget(self.PhotoLabel, 0, 0, 1, 1)
        self.ImageLayout.addWidget(self.PhotoFrame)
        self.verticalLayout_2.addWidget(self.ImageLayots)
        self.NameWidget = QtWidgets.QWidget(self.InformationBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameWidget.sizePolicy().hasHeightForWidth())
        self.NameWidget.setSizePolicy(sizePolicy)
        self.NameWidget.setMinimumSize(QtCore.QSize(0, 62))
        self.NameWidget.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.NameWidget.setObjectName("NameWidget")
        self.NameLayout = QtWidgets.QHBoxLayout(self.NameWidget)
        self.NameLayout.setContentsMargins(0, 0, 0, 0)
        self.NameLayout.setSpacing(8)
        self.NameLayout.setObjectName("NameLayout")
        self.PreNameLabel = QtWidgets.QLabel(self.NameWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PreNameLabel.sizePolicy().hasHeightForWidth())
        self.PreNameLabel.setSizePolicy(sizePolicy)
        self.PreNameLabel.setMinimumSize(QtCore.QSize(150, 63))
        self.PreNameLabel.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.PreNameLabel.setFont(font)
        self.PreNameLabel.setAcceptDrops(False)
        self.PreNameLabel.setAutoFillBackground(False)
        self.PreNameLabel.setStyleSheet("text-decoration: underline;\n"
"border: 1px solid transparent;")
        self.PreNameLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PreNameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PreNameLabel.setWordWrap(True)
        self.PreNameLabel.setObjectName("PreNameLabel")
        self.NameLayout.addWidget(self.PreNameLabel)
        self.NameLabel = QtWidgets.QLabel(self.NameWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameLabel.sizePolicy().hasHeightForWidth())
        self.NameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(29)
        font.setBold(False)
        font.setWeight(50)
        self.NameLabel.setFont(font)
        self.NameLabel.setAutoFillBackground(False)
        self.NameLabel.setStyleSheet("border: 1px solid black;\n"
"border-bottom: 1px solid transparent;")
        self.NameLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NameLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.NameLabel.setTextFormat(QtCore.Qt.AutoText)
        self.NameLabel.setScaledContents(False)
        self.NameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NameLabel.setWordWrap(True)
        self.NameLabel.setIndent(5)
        self.NameLabel.setObjectName("NameLabel")
        self.NameLayout.addWidget(self.NameLabel)
        self.verticalLayout_2.addWidget(self.NameWidget)
        self.PriceWidget = QtWidgets.QWidget(self.InformationBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PriceWidget.sizePolicy().hasHeightForWidth())
        self.PriceWidget.setSizePolicy(sizePolicy)
        self.PriceWidget.setMinimumSize(QtCore.QSize(0, 62))
        self.PriceWidget.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.PriceWidget.setObjectName("PriceWidget")
        self.PriceLayout = QtWidgets.QHBoxLayout(self.PriceWidget)
        self.PriceLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.PriceLayout.setContentsMargins(0, 0, 0, 0)
        self.PriceLayout.setSpacing(8)
        self.PriceLayout.setObjectName("PriceLayout")
        self.PriceLabel = QtWidgets.QLabel(self.PriceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PriceLabel.sizePolicy().hasHeightForWidth())
        self.PriceLabel.setSizePolicy(sizePolicy)
        self.PriceLabel.setMinimumSize(QtCore.QSize(150, 62))
        self.PriceLabel.setMaximumSize(QtCore.QSize(150, 435345))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.PriceLabel.setFont(font)
        self.PriceLabel.setAcceptDrops(False)
        self.PriceLabel.setAutoFillBackground(False)
        self.PriceLabel.setStyleSheet("text-decoration: underline;\n"
"border: 1px solid transparent;")
        self.PriceLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PriceLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PriceLabel.setWordWrap(True)
        self.PriceLabel.setObjectName("PriceLabel")
        self.PriceLayout.addWidget(self.PriceLabel)
        self.frame = QtWidgets.QFrame(self.PriceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("#frame {border: 1px solid black;\n"
"border-bottom: 1px solid transparent;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(-25, 1, 255, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMinimumSize(QtCore.QSize(255, 60))
        self.lcdNumber.setMaximumSize(QtCore.QSize(255, 60))
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setStyleSheet("background-color: transparent;")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(7)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 8236.12)
        self.lcdNumber.setObjectName("lcdNumber")
        self.PriceLayout.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.PriceWidget)
        self.LinkWidget = QtWidgets.QWidget(self.InformationBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LinkWidget.sizePolicy().hasHeightForWidth())
        self.LinkWidget.setSizePolicy(sizePolicy)
        self.LinkWidget.setMinimumSize(QtCore.QSize(0, 62))
        self.LinkWidget.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.LinkWidget.setObjectName("LinkWidget")
        self.NameLayout_2 = QtWidgets.QHBoxLayout(self.LinkWidget)
        self.NameLayout_2.setContentsMargins(0, 0, 0, 0)
        self.NameLayout_2.setSpacing(8)
        self.NameLayout_2.setObjectName("NameLayout_2")
        self.PreNameLabel_2 = QtWidgets.QLabel(self.LinkWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PreNameLabel_2.sizePolicy().hasHeightForWidth())
        self.PreNameLabel_2.setSizePolicy(sizePolicy)
        self.PreNameLabel_2.setMinimumSize(QtCore.QSize(150, 62))
        self.PreNameLabel_2.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.PreNameLabel_2.setFont(font)
        self.PreNameLabel_2.setAcceptDrops(False)
        self.PreNameLabel_2.setAutoFillBackground(False)
        self.PreNameLabel_2.setStyleSheet("text-decoration: underline;\n"
"border: 1px solid transparent;")
        self.PreNameLabel_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PreNameLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PreNameLabel_2.setWordWrap(True)
        self.PreNameLabel_2.setObjectName("PreNameLabel_2")
        self.NameLayout_2.addWidget(self.PreNameLabel_2)
        self.NameLabel_2 = QtWidgets.QLabel(self.LinkWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NameLabel_2.sizePolicy().hasHeightForWidth())
        self.NameLabel_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.NameLabel_2.setFont(font)
        self.NameLabel_2.setAutoFillBackground(False)
        self.NameLabel_2.setStyleSheet("border: 1px solid black;\n"
"border-bottom: 1px solid transparent;")
        self.NameLabel_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NameLabel_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.NameLabel_2.setLineWidth(1)
        self.NameLabel_2.setWordWrap(True)
        self.NameLabel_2.setIndent(5)
        self.NameLabel_2.setOpenExternalLinks(True)
        self.NameLabel_2.setObjectName("NameLabel_2")
        self.NameLayout_2.addWidget(self.NameLabel_2)
        self.verticalLayout_2.addWidget(self.LinkWidget)
        self.EntryLabel = QtWidgets.QWidget(self.InformationBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EntryLabel.sizePolicy().hasHeightForWidth())
        self.EntryLabel.setSizePolicy(sizePolicy)
        self.EntryLabel.setMinimumSize(QtCore.QSize(0, 62))
        self.EntryLabel.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-bottom: 0px solid transparent;")
        self.EntryLabel.setObjectName("EntryLabel")
        self.NoteLayout = QtWidgets.QHBoxLayout(self.EntryLabel)
        self.NoteLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.NoteLayout.setContentsMargins(0, 0, 0, 0)
        self.NoteLayout.setSpacing(8)
        self.NoteLayout.setObjectName("NoteLayout")
        self.NoteText = QtWidgets.QLabel(self.EntryLabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoteText.sizePolicy().hasHeightForWidth())
        self.NoteText.setSizePolicy(sizePolicy)
        self.NoteText.setMinimumSize(QtCore.QSize(150, 62))
        self.NoteText.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.NoteText.setFont(font)
        self.NoteText.setAcceptDrops(False)
        self.NoteText.setAutoFillBackground(False)
        self.NoteText.setStyleSheet("text-decoration: underline;\n"
"border: 1px solid transparent;\n"
"border-bottom: 1px solid transparent;")
        self.NoteText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NoteText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.NoteText.setWordWrap(True)
        self.NoteText.setObjectName("NoteText")
        self.NoteLayout.addWidget(self.NoteText)
        self.textBrowser = QtWidgets.QTextBrowser(self.EntryLabel)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet("border: 1px solid black;\n"
"border-bottom: 1px solid transparent;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.textBrowser.setPlaceholderText("")
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.NoteLayout.addWidget(self.textBrowser)
        self.verticalLayout_2.addWidget(self.EntryLabel)
        self.horizontalLayout_4.addWidget(self.InformationBox)
        self.verticalLayout_3.addWidget(self.FrameMenus)
        self.FrameMenus.raise_()
        self.HeaderLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.EditButton, self.DeleteButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список желаний"))
        self.HeaderLabel.setText(_translate("MainWindow", "С П И С О К      Ж Е Л А Н И Й"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Элементы управления</span></p></body></html>"))
        self.AddButton.setToolTip(_translate("MainWindow", "Добавить новый элемент"))
        self.EditButton.setToolTip(_translate("MainWindow", "Редактировать элемент (ВНИМАНИЕ: Должна быть выбрана строка для редактирования)"))
        self.DeleteButton.setToolTip(_translate("MainWindow", "Удалить элемент (ВНИМАНИЕ: должна быть выбрана строка для удаления)"))
        self.listView.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ваш список желаний. Щелкните по пункту, чтобы узнать подробнее.</p></body></html>"))
        self.ImageName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Изображение:</span></p></body></html>"))
        self.PhotoLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">НЕТ ФОТО</span></p></body></html>"))
        self.PreNameLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Наименование:</span></p></body></html>"))
        self.NameLabel.setText(_translate("MainWindow", "Банка огурцов"))
        self.PriceLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Цена:</span></p></body></html>"))
        self.PreNameLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Ссылка:</span></p></body></html>"))
        self.NameLabel_2.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.farpost.ru/vladivostok/food/organic/ogurcy-malosolnye-57356470.html\"><span style=\" text-decoration: underline; color:#0000ff;\">https://www.farpost.ru/vladivostok/food/organic/ogurcy-malosolnye-57356470.html</span></a></p></body></html>"))
        self.NoteText.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Примечание:</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diem nonummy nibh euismod tincidunt ut lacreet dolore magna aliguam erat volutpat.</span></p></body></html>"))

import resources_rc
