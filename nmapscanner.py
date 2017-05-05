from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PySide.QTCore import *
from PySide.QtGui import *
import optparse
import nmap
import sys

import showGui


class UI_MainWindow(QDialog, showGui.Ui_mainDialog):
    # <editor-fold desc="Description">
    def __init__(self, parent=None):
        # </editor-fold>
        super(UI_MainWindow, self).__init__(parent)
        self.setupUi(self)


app = QApplication(sys.argv)
form = UI_MainWindow()
form.show()
app.exec_()


def nmapScan(tgtHost, tgtPort):
    nScan = nmap.PortScanner()
    nScan.scan(tgtHost, tgtPort)
    state = nScan[tgtHost]['tcp'][int(tgtPort)]['state']
    var = " [*] " + tgtHost + " tcp/ " + tgtPort + " " + state


def Main():
    parser = optparse.OptionParser('usage %prog -H <target host> ' + \
                                   '-p <target port')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',help='specify target port[s] seperated by comma')
    (options, args) = parser.parse_args()
    if (options.tgtHost == None) | (options.tgtPort == None):
        # print parser.usage
        exit(0)
    else:
        tgtHost = options.tgtHost
        if '-' in str(options.tgtPort):
            tgtPorts = str(options.tgtPort).split('-')
            tgtPorts = range(int(tgtPorts[0]), int(tgtPorts[1]))
        else:
            tgtPorts = str(options.tgtPort).split(',')

    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    Main()
