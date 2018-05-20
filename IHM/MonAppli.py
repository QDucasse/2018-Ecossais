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
        
        palette = QtGui.QPalette()
        pixmap = QtGui.QPixmap("")
        palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        self.ui.Principale_ihm.setPalette(palette)
        
        self.ui.bouton_pas.clicked.connect(self.un_pas)
        
#    def un_pas(self):
#        # print("un pas')
#        self.ecosys.unTour()
#        self.ui.centralwidget.update()  # nécessaire pour la MAJ de l'IHM
#        
#        
#    def paintEvent(self, e):
#        qp = QtGui.QPainter()
#        qp.begin(self)
#        self.drawecosysteme(qp) # une méthode à définir
#        qp.end()    
#    
#    def drawecosysteme(self):
#        qp = QtGui.QPainter()
#        qp.setPen(QtCore.Qt.red)
#        qp.drawEllipse(x,y, r_x, r_y)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    