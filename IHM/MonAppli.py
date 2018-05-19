#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 14:33:50 2018

@author: quentin
"""

import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
# l'approche par héritage simple de la classe QMainWindow (même type de notre fenêtre 
# créée avec QT Designer. Nous configurons après l'interface utilisateur 
# dans le constructeur (la méthode init()) de notre classe

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(MyWindow,self).__init__()
        # Configuration de l'interface utilisateur.
        
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('interface.ui',self)
        # TO DO
        
        
        
        
        
        
        
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()