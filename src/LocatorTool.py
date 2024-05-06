import os
from maya import OpenMayaUI
import maya.cmds as cmds
from PySide2.QtCore import Signal
from PySide2.QtGui import QIntValidator, QRegExpValidator 
from PySide2.QtWidgets import QCheckBox, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QListWidget, QMessageBox, QPushButton, QVBoxLayout, QWidget, QAbstractItemView


class LocatorToolWidget(QWidget):
    def __init__(self):
        super(LocatorToolWidget, self).__init__()

        self.setWindowTitle("Create Locator")
        self.setMinimumWidth(500)

        layout = QVBoxLayout()
        self.create_button = QPushButton("Create Locator")
        self.create_button.clicked.connect(self.zeroandgroup)

        layout.addWidget(self.create_button)

        self.setLayout(layout)

        
    def zeroandgroup(self):
        selected_objects = cmds.ls(selection=True)

        if not selected_objects:
            cmds.warning("Please select one mesh or control.")
            return
        
        for obj in selected_objects:
            # Capture the original translation of the object
            original_position = cmds.xform(obj, query=True, worldSpace=True, translation=True)

            # Zero out the transformations
            cmds.setAttr(f"{obj}.translateX", 0)
            cmds.setAttr(f"{obj}.translateY", 0)
            cmds.setAttr(f"{obj}.translateZ", 0)
            cmds.setAttr(f"{obj}.rotateX", 0)
            cmds.setAttr(f"{obj}.rotateY", 0)
            cmds.setAttr(f"{obj}.rotateZ", 0)
            cmds.setAttr(f"{obj}.scaleX", 1)
            cmds.setAttr(f"{obj}.scaleY", 1)
            cmds.setAttr(f"{obj}.scaleZ", 1)


            # Create a locator
            locator = cmds.spaceLocator(name=f"{obj}_locator")[0]

            # Group the object and the locator
            group = cmds.group(obj, locator, name=f"{obj}_group")

            # Move the group to the original position of the object
            cmds.xform(group, worldSpace=True, translation=original_position)

            print(f"Group created with the object and locator: {group}")
        


        



    ##git add -A
    ##git commit -m "new stuff"
    ##git push

    ##to push and save changes