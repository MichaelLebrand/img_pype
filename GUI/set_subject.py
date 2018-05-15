# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_subject.ui'
#
# Created: Mon May 14 18:04:13 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import os
import pydicom

class Ui_setSubject(object):
    def setupUi(self, setSubject):
        setSubject.setObjectName("setSubject")
        setSubject.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(setSubject)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtGui.QWidget(setSubject)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 20, 301, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.SelectCT = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.SelectCT.setFont(font)
        self.SelectCT.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.SelectCT.setObjectName("SelectCT")
        self.gridLayout.addWidget(self.SelectCT, 2, 0, 1, 1)
        self.subjectID = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subjectID.setFont(font)
        self.subjectID.setAlignment(QtCore.Qt.AlignCenter)
        self.subjectID.setObjectName("subjectID")
        self.gridLayout.addWidget(self.subjectID, 0, 1, 1, 1)
        self.SelectT1 = QtGui.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.SelectT1.setFont(font)
        self.SelectT1.setObjectName("SelectT1")
        self.gridLayout.addWidget(self.SelectT1, 1, 0, 1, 1)
        self.subjectIDlabel = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.subjectIDlabel.setFont(font)
        self.subjectIDlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.subjectIDlabel.setObjectName("subjectIDlabel")
        self.gridLayout.addWidget(self.subjectIDlabel, 0, 0, 1, 1)
        self.CTDicomFolder = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CTDicomFolder.setFont(font)
        self.CTDicomFolder.setAlignment(QtCore.Qt.AlignCenter)
        self.CTDicomFolder.setObjectName("CTDicomFolder")
        self.gridLayout.addWidget(self.CTDicomFolder, 2, 1, 1, 1)
        self.T1DicomFolder = QtGui.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.T1DicomFolder.setFont(font)
        self.T1DicomFolder.setAlignment(QtCore.Qt.AlignCenter)
        self.T1DicomFolder.setObjectName("T1DicomFolder")
        self.gridLayout.addWidget(self.T1DicomFolder, 1, 1, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(setSubject)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(170, 160, 195, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setCursor(QtCore.Qt.ArrowCursor)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(4)
        self.spinBox.setSingleStep(3)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 1, 1, 1, 1)

        self.retranslateUi(setSubject)

        # Initialize patient parameters
        self.subjID = []
        self.T1DICOM = []
        self.CTDICOM = []
        self.hemi = []
        self.use3T = []
        self.useCPU = []
        self.origin = []

        # Set button effects
        self.SelectT1.clicked.connect(self.selectFileT1)  # open filedialog for T1 DICOM
        self.SelectCT.clicked.connect(self.selectFileCT)  # open filedialog for CT DICOM
        self.buttonBox.accepted.connect(self.startPipeline)  # Start pipeline
        self.buttonBox.rejected.connect(MainWindow.close)  # close window, exit initialization

    def retranslateUi(self, setSubject):
        setSubject.setWindowTitle(
            QtGui.QApplication.translate("setSubject", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.SelectCT.setText(
            QtGui.QApplication.translate("setSubject", "Select CT", None, QtGui.QApplication.UnicodeUTF8))
        self.subjectID.setPlaceholderText(
            QtGui.QApplication.translate("setSubject", "Set Subject ID", None, QtGui.QApplication.UnicodeUTF8))
        self.SelectT1.setText(
            QtGui.QApplication.translate("setSubject", "Select T1", None, QtGui.QApplication.UnicodeUTF8))
        self.subjectIDlabel.setText(
            QtGui.QApplication.translate("setSubject", "SubjectID:", None, QtGui.QApplication.UnicodeUTF8))
        self.CTDicomFolder.setPlaceholderText(
            QtGui.QApplication.translate("setSubject", "DICOM Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.T1DicomFolder.setPlaceholderText(
            QtGui.QApplication.translate("setSubject", "DICOM Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("setSubject", "Select origin:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("setSubject", "Midline AC-PC", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("setSubject", "Anterior Commisure", None,
                                                                  QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("setSubject", "# CPU Cores:", None, QtGui.QApplication.UnicodeUTF8))

        # Functions for the file selection

    def selectFileT1(self):
        fileT1 = QtGui.QFileDialog.getOpenFileName()
        self.fileT1 = [str(item) for item in fileT1]

        if len(self.fileT1):
            self.T1DicomFolder.setText(self.fileT1[0])
            self.T1DICOM = os.path.dirname(self.fileT1[0])

    def selectFileCT(self):
        fileCT = QtGui.QFileDialog.getOpenFileName()
        self.fileCT = [str(item) for item in fileCT]

        if len(fileCT):
            self.CTDicomFolder.setText(self.fileCT[0])
            self.CTDICOM = os.path.dirname(self.fileCT[0])

    def startPipeline(self):
        # self.noErrors = 1
        # set string parameters
        self.subjID = self.subjectID.text()
        # set default hemisphere for pipeline (doesn't matter now anyways)
        self.hemi = 'rh'

        # read dicom and check fieldstrength, set var accordingly
        ds = pydicom.dcmread(self.fileT1[0])

        if ds.MagneticFieldStrength > 1.5:
            self.use3T = '1'
        else:
            self.use3T = '0'

        del ds

        # checkstate GPU flag
        self.useCPU = self.spinBox.value()
        self.origin = self.comboBox.currentText()

        MainWindow.close()
        print self.T1DICOM

        print ('**************************************************************************** \n'
               'Creating folder structure and running FreeSurfer segmentation for subject %s \n '
               '****************************************************************************' % self.subjID)

        # running python script to prepare and initialize the recon-all via the edited img_pipe distro.
        exec_img_pipe = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'exec_img_pipe.py')
        print ('python %s %s %s %s %s %s %s %s' % (exec_img_pipe, self.subjID, self.hemi, self.T1DICOM,
                                                   self.CTDICOM, self.use3T, self.useCPU, self.origin))
        os.system('python %s %s %s "%s" "%s" %s %s %s' % (exec_img_pipe, self.subjID, self.hemi, self.T1DICOM,
                                                       self.CTDICOM, self.use3T, self.useCPU, self.origin))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_setSubject()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
