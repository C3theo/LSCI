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

        ccdType = QCam_Info.qinfCcd.value
         
        #Initialize Cam to Mono
        settings = QCam_SettingsEx
        self.imgformat = QCam_ImageFormat.qfmtMono16.value

        # Get CCD type
        cam.QCam_GetInfo(self.myHandle,qinfCcd,byref(ccdType))

        #Read Default Settings
        cam.QCam_CreateSettingsStruct(byref(settings))
        cam.QCam_InitializeCameraSettings(self.myHandle, byref(settings));
        cam.QCam_ReadDefaultSettings(self.myHandle, byref(settings))
        
    def __del__(self,cooler,exposure):
        
        cam.QCam_CloseCamera(self.myHandle)
        cam.QCam_ReleaseDriver()
        
    def setQCam(self):

        self.c = cool
        self.exp = exposure

        qexp ,= QCam_Param.qprmExposure.value

        #Min/Max exposure
        QCam_GetParamMin(byref(settings), qexp, byref(expMin))
        QCam_ParamMax(byuref(settings),qexp, byref(expMax))
        

        # Set 16 Bit Mono This could be initialized
        
        cam.QCam_SetParam(byref(settings),qprmImageFormat,format)
        cam.QCam_SendSettingsToCam(self.myHandle,byref(settings))
        
        ## Not sure how to handle pointer to QCam_Settings struct
        ##QCam_SendSettingsToCam(handle, (QCam_Settings*)&settings);
        
        
    def snapMono(self):
        
        self.frame = QCam_Frame
        qimgSize = QCam_Info.qinfImageSize.value
        
        #Get Image Size in bytes
        cam.QCam_GetInfo(self.myHandle,qimgSize,byref(imageSize))

        # frame buffer. Need this in Python?
        frame.pBuffer = []
        frameInterp.bufferSize = imageSize
        
        cam.QCam_GrabFrame(self.myHandle, byref(self.frame))
        del frame.pBuffer
