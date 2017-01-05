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
    def __init__(self,cooler,exposure):
        cam.QCam_LoadDriver()
        self.camId = uint32(0) 
        llen = ct.c_byte(0)    
        self.myHandle = uint32(0)
        cam.QCam_ListCameras(self.camId,byref(llen))
        cam.QCam_OpenCamera(self.camId,byref(self.myHandle))

        self.c = cooler
        self.exp = exposure
        ccdType = QCam_Info.qinfCcd.value
         

        #Initialize Camera settings
        settings = QCam_SettingsEx
        self.imgformat = QCam_ImageFormat.qfmtMono16.value

        # Get CCD type
        cam.QCam_GetInfo(self.myHandle,qinfCcd,byref(ccdType))


        #Read Default Settings
        #Settings: exposure, Cooling,image format
        
        cam.QCam_CreateSettingsStruct(byref(settings))
        cam.QCam_InitializeCameraSettings(self.myHandle, byref(settings));
        cam.QCam_ReadDefaultSettings(self.myHandle, byref(settings))
        
    def __del__(self):
        cam.QCam_CloseCamera(self.myHandle)
        cam.QCam_ReleaseDriver()
        
    def setQCam(self):
        


        # Set 16 Bit Mono
        
        cam.QCam_SetParam(byref(),)
        cam.QCam_SendSettingsToCam(self.myHandle,byref(settings))
        ## Not sure how to handle pointer to QCam_Settings struct
        ##QCam_SendSettingsToCam(handle, (QCam_Settings*)&settings);
        
        #Settings structure
        
    def snapMono(self):
        self.frame = QCam_Frame
        
        qimgSize = QCam_Info.qinfImageSize.value
        #Get Image Size in bytes
        cam.QCam_GetInfo(self.myHandle,qimgSize,byref(imageSize))
        
        cam.QCam_GrabFrame(self.myHandle, byref(self.frame))
