import sys
import urllib.request
from PyQt4 import QtGui, QtCore
from bs4 import BeautifulSoup

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Fucking Shit!")
        self.setWindowIcon(QtGui.QIcon("favicon.png"))
        
        #MenuBar
        extractAction = QtGui.QAction("&Close", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the App")
        extractAction.triggered.connect(self.close_app)
        
        extractAction2 = QtGui.QAction("&Update", self)
        extractAction2.setShortcut("Ctrl+U")
        extractAction2.setStatusTip("Connect to Update Server")
        extractAction2.triggered.connect(self.connecting)
        
        self.statusBar()
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
        
        fileMenu2 = mainMenu.addMenu("&Help")
        fileMenu2.addAction(extractAction2)
        
        self.home()
        
    def home(self):
        #Button
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_app)
        btn.resize(btn.minimumSizeHint())
        btn.move(200, 250)
        
        #ToolBar
        extractAction = QtGui.QAction(QtGui.QIcon("favicon00.png"), "Leave that Shit", self)
        extractAction.setStatusTip("I'm Quit !!")
        extractAction.triggered.connect(self.close_app)
        
        self.statusBar()
        
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)
        
        #CheckBox to enlagrge the window
        checkBox = QtGui.QCheckBox("Enlarge Window", self)
        checkBox.move(6, 50)
        checkBox.stateChanged.connect(self.enlarge_window)

        #ProgressBar
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(150, 100, 250, 20)
        #Button to make the progressBar working
        self.btn = QtGui.QPushButton("Download", self)
        self.btn.move(200, 135)
        self.btn.clicked.connect(self.download)
        

        self.show()


    #func for updating in the help menu button update
    def connecting(self):
        wh = urllib.request.urlopen("http://nullege.com/codes/search/PyQt4.QtGui.QLineEdit.setEchoMode").read()
        soup = BeautifulSoup(wh, "html.parser")
        print(soup)
        
    #func to enlarge window using checkBox
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
    
    #Func to connect the button with the progressBar and make it working
    def download(self):
        self.completed = 0
        
        while self.completed < 100:
            self.completed += 0.001
            self.progress.setValue(self.completed)
            
                          
    #func for closing any window, but with asking yes or no
    def close_app(self):
        choice = QtGui.QMessageBox.Question(self, "Quitting !!",
                                            "Are You Sure you wanna leave that shit ?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Bye Bye")
            sys.exit()
        else:
            pass
    
"""  
    #func for closing any window, without any asking
    def close_app(self):
        print("Bye Bye!!")
        sys.exit()
"""
        
#running the whole program       
def run():        
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()