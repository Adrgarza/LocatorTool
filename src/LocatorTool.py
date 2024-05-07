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
            original_translation = cmds.xform(obj, query=True, worldSpace=True, translation=True)
            original_rotation = cmds.xform(obj, query=True, worldSpace=True, rotation=True)
            
            # Create a locator
            locator = cmds.spaceLocator(name=f"{obj}_locator")[0]



            # Group the object and the locator
            group = cmds.parent(locator, obj, name=f"{obj}_locator")

            # Move the group to the original position of the object
            cmds.xform(locator, worldSpace=True, translation=original_translation, rotation=original_rotation)

            print(f"Group created with the object and locator: {group}")
        


locatorToolWidget = LocatorToolWidget()
locatorToolWidget.show()




    ## copy and paste this below into your MEL code in maya
    ## commandPort -name "localhost:7001" -sourceType "mel";
    ##


    ##git add -A
    ##git commit -m "new stuff"
    ##git push

    ##to push and save changes