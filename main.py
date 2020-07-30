from mainGUI import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
import sys

import re
import csv
import glob
import pandas as pd

class MyWin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.ErrorLabel.hide()
		self.ui.VersionLabel.hide()

		self.ErrorFlag = False
		self.InData = None
		self.InDataPath = None
		self.OutDataPath = None
		self.InState = False
		self.OutState = False

		self.ui.InputDataPushButton.clicked.connect(self.GetInDataPath)
		self.ui.OutputDatasetPushButton.clicked.connect(self.GetOutDatasetPath)
		self.ui.SubmitPushButton.clicked.connect(self.Continue)

	def GetInDataPath(self):
		'''
		:
		'''
		self.InDataPath = QFileDialog.getExistingDirectory(self, "Select Directory", 'C:\\')
		print(self.InDataPath)
		if self.InDataPath[0]:
			self.InState = True
		else:
			self.InState = False

	def GetOutDatasetPath(self):
		'''
		:
		'''
		self.OutDataPath = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', "Data files (*.csv)")
		if self.OutDataPath[0]:
			self.OutState = True
		else:
			self.OutState = False

	def Continue(self):
		'''
		:
		'''
		label = self.ui.LabelLineEdit.text()
		kword = self.ui.KWordLineEdit.text()

		if self.InState and self.OutState and label and kword:
			self.ui.ErrorLabel.setStyleSheet('color: black')
			self.ui.ErrorLabel.setText("Processing...")
			self.ui.ErrorLabel.show()

			QApplication.processEvents()

			corpusPath = glob.glob(self.InDataPath+"/*.txt")
			for c_path in corpusPath:
				corpus = open(c_path, encoding="utf-8").read()
				for k in re.split('\W+', kword):
					toWrite = [[s.strip(), label, k] for s in re.split(r'\.|\?|\!', corpus) if k in re.split(r'\s|\,|\, ' , s.lower().strip())]
					with open(self.OutDataPath[0], "a", newline='', encoding='utf-8') as f:
					    writer = csv.writer(f)
					    writer.writerows(toWrite)
			self.ui.ErrorLabel.setText("Done")
		else:
			self.ui.ErrorLabel.setStyleSheet('color: red')
			self.ui.ErrorLabel.setText("Error")
			self.ui.ErrorLabel.show()

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()
	myapp.show()
	sys.exit(app.exec_())