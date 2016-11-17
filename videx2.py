# -*- coding: utf-8 -*-
"""
Created on Mon Sep 03 15:00:33 2012

@author: kner
"""

import sys, os, random
from PyQt4 import QtGui, QtCore


from PyQt4.QtCore import *
from PyQt4.QtGui import *

from scipy import signal as sg
#import tiffile as tf
import numpy as N
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import cm
import matplotlib as mpl

#import serial
import time


app = QtGui.QApplication(sys.argv)

#import DVI

class vid(QtCore.QObject):
    
    def __init__(self, parent=None):
        super(vid, self).__init__(parent)
        self.data = N.random.rand(512, 512)
        self.timer = QtCore.QTimer(self)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.vtest)
        self.timer.start(30)
    
    def vtest(self):
        self.data = N.random.rand(512,512)
        self.emit(QtCore.SIGNAL("newdata"))

class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        self.axes.hold(False)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def sizeHint(self):
        w, h = self.get_width_height()
        return QtCore.QSize(w, h)

    def minimumSizeHint(self):
        return QtCore.QSize(10, 10)


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, data=None, parent=None, dpi=100):
        if data==None:
            self.nx = 512
            self.ny = 512
            self.data = N.zeros((self.nx, self.ny))            
        else:
            self.data = data
            nx,ny = data.shape
            self.nx = nx
            self.ny = ny
        W = N.round(self.nx)
        H = N.round(self.ny)
        MyMplCanvas.__init__(self, parent=None, width=W, height=H, dpi=100)
        
    
        
            
        
    def compute_initial_figure(self):
        self.imgh = self.axes.imshow(self.data,interpolation="nearest", cmap=cm.bone)

    def update_figure(self, datanew):
        #self.axes.imshow(self.data[slice],interpolation='nearest',cmap=cm.winter)
        self.data = datanew
        nx,ny = self.data.shape
        self.nx = nx
        self.ny = ny
        self.imgh.set_data(self.data)
        self.imgh.set_clim(datanew.min(), datanew.max())
        self.draw()
        
           
class viewerWindow(QtGui.QDialog):
    def __init__(self, data=None, parent=None):
        super(viewerWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
#        self.ser = serial.Serial('COM3',9600)
#        self.ser.write('1')
        
        self.main_widget = QtGui.QWidget(self)
        
        self.dc = MyDynamicMplCanvas(data, parent=self.main_widget)
        
        self.ks=5
        self.msk = self.discarr2(self.ks)
        self.slider1 = QtGui.QSlider(Qt.Horizontal)
        self.slider1.setMinimum(1)
        self.slider1.setMaximum(20)
        self.slider1.setValue(self.ks)
        self.slider1.setTickPosition(QSlider.TicksBothSides)
        self.slider1.setTickInterval(5)
        
        self.slider2 = QtGui.QSlider(Qt.Horizontal)
        self.slider2.setMinimum(1)
        self.slider2.setMaximum(193)
        self.slider2.setValue(0)
        self.slider2.setTickPosition(QSlider.TicksBothSides)
        self.slider2.setTickInterval(4.25)
        
#        self.n = 100
#        self.slider3 = QtGui.QSlider(Qt.Horizontal)
#        self.slider3.setMinimum(10)
#        self.slider3.setMaximum(150)
#        self.slider3.setValue(self.n)
#        self.slider3.setTickPosition(QSlider.TicksBothSides)
#        self.slider3.setTickInterval(10)
        
        
        
        self.button2 = QtGui.QPushButton("Save Image")
        
        self.button1 = QtGui.QPushButton("Close")
        
        self.vs = vid()
        self.connect(self.vs,QtCore.SIGNAL("newdata"),self.update)
        #self.connect(self.vm,QtCore.SIGNAL("newdata1"),self.update)
        
        # Layout
        lyt = QtGui.QVBoxLayout(self.main_widget)
        lyt.addWidget(self.dc)
        lyt.addWidget(self.slider1)
        lyt.addWidget(self.slider2)
#        lyt.addWidget(self.slider3)
        
        lyt.addWidget(self.button1)
        lyt.addWidget(self.button2)
        lyt.addStretch()
        self.setLayout(lyt)
        
        self.clicked =False
        
        self.slider1.valueChanged.connect(self.valuechange)        
        self.slider2.valueChanged.connect(self.valuechange2)
#        self.slider3.valueChanged.connect(self.valuechange3)
        
        self.connect(self.button1, QtCore.SIGNAL("clicked()"), self.fileQuit)
        self.connect(self.button2, QtCore.SIGNAL("clicked()"), self.saveImage)
        
        
        self.setWindowTitle("Local STD")
        self.show()
        self.raise_()
        self.activateWindow()
    
    def __del__(self):
#        self.ser.write('1')
#        self.ser.close()
        
    def update(self):
        data = self.vs.data
#        self.data = self.discarr(self.ks, 512)
        self.data = self.lstd(data)
        self.dc.update_figure(self.data)        
        
    def fileQuit(self):
        self.close()
        self.__del__()

    def closeEvent(self, ce):
        self.fileQuit()
        
    def valuechange(self):
        self.ks = self.slider1.value()
        msk = self.discarr2(self.ks)
        self.msk = msk/msk.sum()
        print("Disc Radius: %i" %(self.ks))
    
    def valuechange2(self):
        sv = self.slider2.value()
        self.ser.write(str(sv))
        print str(sv)
        
    def discarr(self, r, nx):
        x = N.linspace(-nx/2,nx/2,nx)
        X,Y = N.meshgrid(x,x)
        rho = N.hypot(X,Y)
        return rho <= r
        
    def lstd(self,arr):
        msk = self.msk
        ar2 = sg.fftconvolve(arr,msk)**2
        ar3 = sg.fftconvolve(arr**2,msk)
        return N.sqrt(N.abs(ar3-ar2))
        
    def discarr2(self, r):
        x = N.arange(-r,r,1)
        X,Y = N.meshgrid(x,x)
        rho = N.hypot(X,Y)
        return (rho <= r).astype(N.float)
        
    def saveImage(self, msk):
        rnd = []
        for i in range(100):
            a = N.random.exponential(N.ones((512,512))).astype(float)
            b = N.random.rand(512,512).astype(float)
            rnd.append(a*msk + b*(1-msk))
            N.save(rnd)
            print(rnd)
        
        savedimg = T.imsave(self.data) 
    
    def binMask(self):
        self.nx = 512
        n = 100
        arr = N.array([[j for j in range(self.nx)] for i in range(self.nx)])
        lowerlim = (nx - n)/2
        upperlim = (nx + n)/2
        msk = (a>lowerlim) & (a<upperlim)
        
        
       
       
       
            
    
        
    
        

        
        
