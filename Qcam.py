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
        cam.QCam_CloseCamera(self.myHandle)
        cam.QCam_ReleaseDriver()
        
    def setQCam(self):
        settings = QCam_SettingsEx()
       # imgForm = QCam_ImageFormat()
        imgForm = qfmtMono16
        cooler = 0 
        cam.QCam_GetInfo(self.myHandle,qinfCcd, byref(ccdType))
        cam.QCam_CreateCameraSettingsStruct(byref(settings))
        cam.QCam_InitializeCameraSettings(self.myHandle,byref(settings))
        cam.QCam_ReadDefaultSettings(self.myHandle,byref(settings))
        cam.QCam_GetParamMin(byref(settings),qprmExposure,expMin)
        cam.QCam_GetParamMax(byref(settings,qprmExposure,expMax)
        cam.QCam_SetParam(byref(settings),qprmCoolerActive,cooler)
        cam.QCam_SetParam(byref(settings),qprmExposure,exposure)
        cam.QCam_SetParam(byref(settings),qprmImageFormat,imgForm)
        if exposure < expMin:
             exposure = expMin
             
        if exposure > expMax:
             exposure = expMax
             
        cam.QCam_SendSettingstoCam(self.myHandle,byref(settings))
    
      
         
        
         
        
#
    def snapMono(self):
        frame = QCam_Frame()
        
        cam.QCam_Getinfo(self.myHandle,qinfImageSize,byref(imgSize))
        cam.QCam_GrabFrame(self.myHandle,byref(frame))
        
        del frame.pbuffer
        
        
