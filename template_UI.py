from shiboken2 import wrapInstance

import os
import maya.cmds as cm
# import pymel.core as pm
import maya.OpenMaya as om
import maya.OpenMayaUI as omui

from PySide2 import QtWidgets, QtCore, QtGui
from maya.mel import eval


# import sys

# noinspection PyAttributeOutsideInit
class ToolName(QtWidgets.QWidget):

    def __init__(self):
        super(ToolName, self).__init__()

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        pass

    def create_layouts(self):
        first_layout = QtWidgets.QHBoxLayout()

        second_layout = QtWidgets.QHBoxLayout()

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(first_layout)
        main_layout.addLayout(second_layout)

    def create_connections(self):
        pass


# noinspection PyMethodMayBeStatic,PyAttributeOutsideInit,PyMethodOverriding
class MainWindow(QtWidgets.QDialog):
    WINDOW_TITLE = "Name Show On Maya"

    dlg_instance = None

    @classmethod
    def display(cls):
        if not cls.dlg_instance:
            cls.dlg_instance = MainWindow()

        if cls.dlg_instance.isHidden():
            cls.dlg_instance.show()

        else:
            cls.dlg_instance.raise_()
            cls.dlg_instance.activateWindow()

    @classmethod
    def maya_main_window(cls):
        """

        Returns: The Maya main window widget as a Python object

        """
        main_window_ptr = omui.MQtUtil.mainWindow()
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

    def __init__(self):
        super(MainWindow, self).__init__(self.maya_main_window())

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.geometry = None

        self.setMinimumSize(400, 100)
        self.setMaximumSize(400, 100)
        self.create_widget()
        self.create_layouts()
        self.create_connections()

    def create_widget(self):
        self.content_layout = QtWidgets.QHBoxLayout()
        self.content_layout.addWidget(ToolName())

        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layouts(self):

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(self.content_layout)

    def create_connections(self):
        self.close_btn.clicked.connect(self.close)

    def showEvent(self, e):
        super(MainWindow, self).showEvent(e)

        if self.geometry:
            self.restoreGeometry(self.geometry)

    def closeEvent(self, e):
        super(MainWindow, self).closeEvent(e)

        self.geometry = self.saveGeometry()

MainWindow().show()