
from encryption import Enc
from receiving import Rcv
import rsa
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
from chat import Chat
from receiving import Rcv
from encryption import Enc
import socket
class Ui_MainWindow(object):

    def __init__(self):
        (pub_key, priv_key) = rsa.newkeys(512)
        self.enc = Enc(pub_key, priv_key)
        self.rcv = Rcv(pub_key, priv_key)
        self.file = None
        self.rcv.set_message = self.set_message
        self.cht = Chat(rcv=self.rcv, enc=self.enc)
        self.cht.set_status = self.set_status
        self.cht.set_peer_ip = self.set_peer_ip
        self.cht.set_port = self.set_port

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 20, 131, 41))
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 290, 171, 301))
        self.groupBox.setStyleSheet("background-color:#0A2647;\n"
                                    "  border: 1px solid #222222;\n"
                                    "  border-radius: 8px;\n"
                                    "  box-sizing: border-box;\n"
                                    "  color: white;\n"
                                    "  cursor: pointer;\n"
                                    "  display: inline-block;\n"
                                    "  font-size: 10px;\n"
                                    "  font-weight: 600;\n"
                                    "  line-height: 20px;\n"
                                    "  margin: 0;\n"
                                    "  outline: none;\n"
                                    "  padding: 3px 8px;\n"
                                    "  position: relative;\n"
                                    "  text-decoration: none;\n"
                                    "  touch-action: manipulation;\n"
                                    "  transition: box-shadow .2s,-ms-transform .1s,-webkit-transform .1s,transform .1s;\n"
                                    "  user-select: none;\n"
                                    "  -webkit-user-select: none;\n"
                                    "  width: auto;\n"
                                    "")
        self.groupBox.setObjectName("groupBox")

        self.label_status = QtWidgets.QLabel(self.groupBox)
        self.label_status.setGeometry(QtCore.QRect(10, 20, 149, 41))
        self.label_status.setStyleSheet("background-color:#1B2430;\n"
                                        "color: white;")
        self.label_status.setObjectName("label_status")


        self.label_peerip = QtWidgets.QLabel(self.groupBox)
        self.label_peerip.setGeometry(QtCore.QRect(10, 120, 149, 41))
        self.label_peerip.setStyleSheet("background-color:#1B2430;\n"
                                        "color: white;")
        self.label_peerip.setObjectName("label_peerip")


        self.label_name = QtWidgets.QLabel(self.groupBox)
        self.label_name.setGeometry(QtCore.QRect(10, 70, 149, 41))
        self.label_name.setStyleSheet("background-color:#1B2430;\n"
                                      "color: white;")
        self.label_name.setObjectName("label_name")


        self.label_port = QtWidgets.QLabel(self.groupBox)
        self.label_port.setGeometry(QtCore.QRect(10, 170, 149, 41))
        self.label_port.setStyleSheet("background-color:#1B2430;\n"
                                      "color: white;")
        self.label_port.setObjectName("label_port")


        self.label_key = QtWidgets.QLabel(self.groupBox)
        self.label_key.setGeometry(QtCore.QRect(10, 220, 149, 41))
        self.label_key.setStyleSheet("background-color:#1B2430;\n"
                                     "color: white;")
        self.label_key.setObjectName("label_key")


        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 171, 201))
        self.groupBox_2.setStyleSheet("background-color:#0A2647;\n"
                                        "  border: 1px solid #222222;\n"
                                        "  border-radius: 8px;\n"
                                        "  box-sizing: border-box;\n"
                                        "  color: white;\n"
                                        "  cursor: pointer;\n"
                                        "  display: inline-block;\n"
                                        "  font-size: 10px;\n"
                                        "  font-weight: 600;\n"
                                        "  line-height: 20px;\n"
                                        "  margin: 0;\n"
                                        "  outline: none;\n"
                                        "  padding: 3px 8px;\n"
                                        "  position: relative;\n"
                                        "  text-decoration: none;\n"
                                        "  touch-action: manipulation;\n"
                                        "  transition: box-shadow .2s,-ms-transform .1s,-webkit-transform .1s,transform .1s;\n"
                                        "  user-select: none;\n"
                                        "  -webkit-user-select: none;\n"
                                        "  width: auto;\n"
                                        "")
        self.groupBox_2.setObjectName("groupBox_2")
        #await
        self.await_button = QtWidgets.QPushButton(self.groupBox_2)
        self.await_button.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.await_button.setStyleSheet("background-color: #FF0000")
        self.await_button.setObjectName("await_button")
        self.await_button.clicked.connect(self.cht.start_chat_await)

        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 151, 31))
        self.label_4.setStyleSheet("background-color:#1B2430;\n"
                                    "color: white;")
        self.label_4.setObjectName("label_4")

        #connect
        self.connect_button = QtWidgets.QPushButton(self.groupBox_2)
        self.connect_button.setGeometry(QtCore.QRect(10, 140, 151, 18))
        self.connect_button.setStyleSheet("background-color: #FF0000")
        self.connect_button.setObjectName("connect_button")
        self.connect_button.clicked.connect(self.get_ip)

        self.disconnect_button = QtWidgets.QPushButton(self.groupBox_2)
        self.disconnect_button.setGeometry(QtCore.QRect(10, 165, 151, 18))
        self.disconnect_button.setStyleSheet("background-color: #FF0000")
        self.disconnect_button.setObjectName("disconnect_button")
        self.disconnect_button.clicked.connect(self.cht.disconnect)


        self.lineEdit_ip = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_ip.setGeometry(QtCore.QRect(10, 100, 151, 31))
        self.lineEdit_ip.setStyleSheet("background-color: white;\n"
                                       "color: black;")
        self.lineEdit_ip.setText("")
        self.lineEdit_ip.setObjectName("lineEdit")


        self.label_4.raise_()
        self.connect_button.raise_()
        self.lineEdit_ip.raise_()
        self.await_button.raise_()
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(200, 80, 551, 511))
        self.groupBox_3.setStyleSheet("background-color:#0A2647;\n"
                                        "  border: 1px solid #222222;\n"
                                        "  border-radius: 8px;\n"
                                        "  box-sizing: border-box;\n"
                                        "  color: white;\n"
                                        "  cursor: pointer;\n"
                                        "  display: inline-block;\n"
                                        "  font-size: 14px;\n"
                                        "  font-weight: 600;\n"
                                        "  line-height: 20px;\n"
                                        "  margin: 0;\n"
                                        "  outline: none;\n"
                                        "  padding: 13px 23px;\n"
                                        "  position: relative;\n"
                                        "  text-decoration: none;\n"
                                        "  touch-action: manipulation;\n"
                                        "  transition: box-shadow .2s,-ms-transform .1s,-webkit-transform .1s,transform .1s;\n"
                                        "  user-select: none;\n"
                                        "  -webkit-user-select: none;\n"
                                        "  width: auto;")
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.input_line = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_line.setGeometry(QtCore.QRect(20, 460, 361, 41))
        self.input_line.setStyleSheet("QLineEdit { \n"
                                      "  background-color: #FFFFFF;\n"
                                      "  border: 1px solid #222222;\n"
                                      "  border-radius: 8px;\n"
                                      "  box-sizing: border-box;\n"
                                      "  color: #222222;\n"
                                      "  cursor: pointer;\n"
                                      "  display: inline-block;\n"
                                      "  font-family: Circular,-apple-system,BlinkMacSystemFont,Roboto,\"Helvetica Neue\",sans-serif;\n"
                                      "  font-size: 14px;\n"
                                      "  font-weight: 600;\n"
                                      "  line-height: 20px;\n"
                                      "  margin: 0;\n"
                                      "  outline: none;\n"
                                      "  padding: 3px 8px;\n"
                                      "  position: relative;\n"
                                      "  text-decoration: none;\n"
                                      "  touch-action: manipulation;\n"
                                      "  transition: box-shadow .2s,-ms-transform .1s,-webkit-transform .1s,transform .1s;\n"
                                      "  user-select: none;\n"
                                      "  -webkit-user-select: none;\n"
                                      "  width: auto;\n"
                                      "}")
        self.input_line.setText("")
        self.input_line.setObjectName("input_line")


        self.send_button = QtWidgets.QPushButton(self.groupBox_3)
        self.send_button.setGeometry(QtCore.QRect(440, 460, 91, 41))
        self.send_button.setStyleSheet("background-color: #FF0000;\n"
                                        "  border: 1px solid #222222;\n"
                                        "  border-radius: 8px;\n"
                                        "  box-sizing: border-box;\n"
                                        "  color: white;\n"
                                        "  cursor: pointer;\n"
                                        "  display: inline-block;\n"
                                        "  font-size: 14px;\n"
                                        "  font-weight: 600;\n"
                                        "  line-height: 20px;\n"
                                        "  margin: 0;\n"
                                        "  outline: none;\n"
                                        "  padding: 13px 23px;\n"
                                        "  position: relative;\n"
                                        "  text-align: center;\n"
                                        "  text-decoration: none;\n"
                                        "  touch-action: manipulation;\n"
                                        "  transition: box-shadow .2s,-ms-transform .1s,-webkit-transform .1s,transform .1s;\n"
                                        "  user-select: none;\n"
                                        "  -webkit-user-select: none;\n"
                                        "  width: auto;\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "")
        self.send_button.setAutoDefault(False)
        self.send_button.setObjectName("send_button")
        self.send_button.clicked.connect(self.message)

        self.chat_text = QtWidgets.QTextEdit(self.groupBox_3)
        self.chat_text.setReadOnly(True)
        self.chat_text.setGeometry(QtCore.QRect(20, 30, 511, 421))
        self.chat_text.setStyleSheet("  background-color: white;\n"
                                        "  border: 1px solid #222222;\n"
                                        "  border-radius: 8px;\n"
                                        "  box-sizing: border-box;\n"
                                        "  color: #222222;\n"
                                        "  cursor: pointer;\n"
                                        "  display: inline-block;\n"
                                        "  font-family: Circular,-apple-system,BlinkMacSystemFont,Roboto,\"Helvetica Neue\",sans-serif;\n"
                                        "  font-size: 14px;\n"
                                        "  font-weight: 600;\n"
                                        "  line-height: 20px;\n"
                                        "  margin: 0;\n"
                                        "  outline: none;\n"
                                        "  padding: 13px 23px;\n"
                                        "  position: relative;\n"
                                        "  text-decoration: none;\n"
                                        "  touch-action: manipulation;\n"
                                        "  transition: box-shadow .2s,-ms-transform .1s,-webkit-transform .1s,transform .1s;\n"
                                        "  user-select: none;\n"
                                        "  -webkit-user-select: none;\n"
                                        "  width: auto;")
        self.chat_text.setObjectName("chat_text")
        self.send_button_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.send_button_2.setGeometry(QtCore.QRect(390, 460, 41, 41))
        self.send_button_2.setStyleSheet("background-color: white;\n"
                                         "  border: 1px solid #222222;\n"
                                         "  border-radius: 8px;\n"
                                         "  box-sizing: border-box;\n"
                                         "  color: white;\n"
                                         "  cursor: pointer;\n"
                                         "  display: inline-block;\n"
                                         "  font-size: 14px;\n"
                                         "  font-weight: 600;\n"
                                         "  line-height: 20px;\n"
                                         "  margin: 0;\n"
                                         "  outline: none;\n"
                                         "  padding: 3px 8px;\n"
                                         "  position: relative;\n"
                                         "  text-align: center;\n"
                                         "  text-decoration: none;\n"
                                         "  touch-action: manipulation;\n"
                                         "  transition: box-shadow .2s,-ms-transform .1s,-webkit-transform .1s,transform .1s;\n"
                                         "  user-select: none;\n"
                                         "  -webkit-user-select: none;\n"
                                         "  width: auto;\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "")
        self.send_button_2.setText("")
        self.send_button_2.setAutoDefault(False)
        self.send_button_2.setObjectName("send_button_2")
        self.send_button_2.clicked.connect(self.open_file_system)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(-4, -8, 771, 651))
        self.label_10.setStyleSheet("background-color:#1B2430")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_10.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Chat P2P"))
        hostname = socket.gethostname()
        self.label_2.setText(_translate("MainWindow", "Your IP: "+socket.gethostbyname(hostname)))
        self.groupBox.setTitle(_translate("MainWindow", "Info"))
        self.label_status.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:8pt;\">Status: </span></p></body></html>"))
        self.label_peerip.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:8pt;\">Peer IP: </span></p></body></html>"))
        self.label_name.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:8pt;\"> Name: </span></p></body></html>"))
        self.label_port.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:8pt;\">Port: </span></p></body></html>"))
        self.label_key.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:8pt;\">Key:  </span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Mode"))
        self.await_button.setText(_translate("MainWindow", "Await Connection"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Enter IP address:</span></p></body></html>"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.disconnect_button.setText(_translate("MainWindow", "Disconnect"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Chat"))
        self.send_button.setText(_translate("MainWindow", "Send"))
        self.send_button_2.setIcon(QIcon('ico.png'))

    def open_file_system(self):
        filename, ok = QFileDialog.getOpenFileName(None, "Select a File","","All Files (*)")
        self.rcv.file = filename
        self.input_line.setText("File Selected")

    def get_ip(self):
        ip = self.lineEdit_ip.text()
        self.cht.target_ip = ip
        self.cht.start_chat_connect()
    def set_status(self, msg):
        self.label_status.setText("Status: " + msg)

    def set_peer_ip(self, msg):
        self.label_peerip.setText("Peer IP: " + msg)

    def set_port(self, msg):
        self.label_port.setText("Port: " + msg)

    def set_message(self, msg):
        self.chat_text.append(msg)

    def message(self):
        if not "Connected" in self.label_status.text():
            return
        msg = self.input_line.text()
        self.rcv.send_messages(msg)
        self.input_line.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
