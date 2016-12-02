# -*- coding: utf-8 -*-
"""
Created on Wed May 25 12:29:46 2016

@author: kayvanf
"""
import ctypes as ct
cam = ct.windll.QCamDriver
uint32 = ct.c_uint32
byref = ct.byref
from QCam_vars import *


class Qcam(object):
    def __init__(self):
        cam.QCam_LoadDriver()
        self.camId = uint32(0) 
        llen = ct.c_byte(0)    
        self.myHandle = uint32(0)
        cam.QCam_ListCameras(self.camId,byref(llen))
        cam.QCam_OpenCamera(self.camId,byref(self.myHandle))

    def __del__(self):
        cam.killQCam(self.myHandle)
        cam.QCam_ReleaseDriver()
        
    def setQCam(self):
        cam.QCam_SetParam(byref(),)
        

        return 0
#
    def snapMono(self):
       # cam.QCam_GrabFrame(self.myHandle, byref(Qcam_Frame))
        cam.QCam_GrabFrame(self.myHandle)