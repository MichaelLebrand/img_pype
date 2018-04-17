
from PyQt4 import QtCore, QtGui
import os
import pydicom

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(363, 244)
        MainWindow.move(500,400)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 10, 301, 151))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setToolTip(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.subjIDBox = QtGui.QLineEdit(self.formLayoutWidget)
        self.subjIDBox.setAlignment(QtCore.Qt.AlignCenter)
        self.subjIDBox.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.subjIDBox)
        self.selectT1Btn = QtGui.QPushButton(self.formLayoutWidget)
        self.selectT1Btn.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.selectT1Btn)
        self.T1Folder = QtGui.QLineEdit(self.formLayoutWidget)
        self.T1Folder.setAlignment(QtCore.Qt.AlignCenter)
        self.T1Folder.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.T1Folder)
        self.selectCTBtn = QtGui.QPushButton(self.formLayoutWidget)
        self.selectCTBtn.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.selectCTBtn)
        self.CTFolder = QtGui.QLineEdit(self.formLayoutWidget)
        self.CTFolder.setAlignment(QtCore.Qt.AlignCenter)
        self.CTFolder.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.CTFolder)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(990, 610, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.okBtn = QtGui.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(140, 210, 81, 27))
        self.okBtn.setObjectName(_fromUtf8("pushButton_3"))
        self.cancelBtn = QtGui.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(230, 210, 81, 27))
        self.cancelBtn.setObjectName(_fromUtf8("pushButton_4"))
        self.flagUseGPU = QtGui.QCheckBox(self.centralwidget)
        self.flagUseGPU.setGeometry(QtCore.QRect(180, 160, 121, 22))
        self.flagUseGPU.setObjectName(_fromUtf8("checkBox_2"))
        self.formLayoutWidget.raise_()
        self.buttonBox.raise_()
        self.okBtn.raise_()
        self.cancelBtn.raise_()
        self.flagUseGPU.raise_()
        self.flagUseGPU.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Initialize patient parameters
        self.subjID  = []
        self.T1DICOM = []
        self.CTDICOM = []
        self.hemi    = []
        self.use3T   = []
        self.useGPU  = []

        # Set button effects
        self.selectT1Btn.clicked.connect(self.selectFileT1)    # open filedialog for T1 DICOM
        self.selectCTBtn.clicked.connect(self.selectFileCT)    # open filedialog for CT DICOM
        self.okBtn.clicked.connect(self.startPipeline)         # Start pipeline
        self.cancelBtn.clicked.connect(MainWindow.close)       # close window, exit initialization

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Initialize img_pipe patient", None))
        self.label.setText(_translate("MainWindow", " SubjectID:", None))
        self.subjIDBox.setPlaceholderText(_translate("MainWindow", "Set Subject ID", None))
        self.selectT1Btn.setText(_translate("MainWindow", "Select T1", None))
        self.T1Folder.setPlaceholderText(_translate("MainWindow", "DICOM Folder", None))
        self.selectCTBtn.setText(_translate("MainWindow", "Select CT", None))
        self.CTFolder.setPlaceholderText(_translate("MainWindow", "DICOM Folder", None))
        self.okBtn.setText(_translate("MainWindow", "Ok", None))
        self.cancelBtn.setText(_translate("MainWindow", "Cancel", None))
        self.flagUseGPU.setText(_translate("MainWindow", "Use GPU", None))

    # Functions for the file selection
    def selectFileT1(self):
        self.fileT1 = str(QtGui.QFileDialog.getOpenFileName())

        if len(self.fileT1):
            self.T1Folder.setText(self.fileT1)
            self.T1DICOM = os.path.dirname(self.fileT1)

    def selectFileCT(self):
        fileCT = str(QtGui.QFileDialog.getOpenFileName())

        if len(fileCT):
            self.CTFolder.setText(fileCT)
            self.CTDICOM = os.path.dirname(fileCT)


    def startPipeline(self):
        # self.noErrors = 1
        # set string parameters
        self.subjID = self.subjIDBox.text()

        # set default hemisphere for pipeline (doesn't matter now anyways)
        self.hemi = 'rh'

        # read dicom and check fieldstrength, set var accordingly
        ds = pydicom.dcmread(self.fileT1)

        if ds.MagneticFieldStrength > 1.5:
            self.use3T = '1'
        else:
            self.use3T = '0'

        del ds

        # checkstate GPU flag
        self.useGPU = self.flagUseGPU.checkState()

        MainWindow.close()
        print self.T1Folder

        print ('**************************************************************************** \n'
               'Creating folder structure and running FreeSurfer segmentation for subject %s \n '
               '****************************************************************************' % self.subjID)

        # running python script to prepare and initialize the recon-all via the edited img_pipe distro.
        exec_img_pipe = os.path.join(os.path.dirname(os.path.realpath(__file__)),'exec_img_pipe.py')
        print ('python %s %s %s %s %s %s %s'%(exec_img_pipe, self.subjID, self.hemi, self.T1DICOM, self.CTDICOM, self.use3T, self.useGPU))
        os.system('python %s %s %s "%s" "%s" %s %s'%(exec_img_pipe, self.subjID, self.hemi, self.T1DICOM, self.CTDICOM, self.use3T, self.useGPU))


    # TODO: fix warning dialog that responds to incorrect inputs (subject already exists / wrong file / no hemi selected)




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

