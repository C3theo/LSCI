# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:16:14 2016

@author: kayvanf

Based on QCamApi.h
"""

from ctypes import *
from enum import Enum

class Settings(Structure):
    _fields_ = [("f1", c_uint32), 
                ("f2", c_uint16),
                ("f3", c_uint16), 
                ("f4", c_uint*8)]

class QCam_Settings(Structure):
    _fields_ = [("size", c_ulong), 
                ("_private_data",c_ulong*64)]

class QCam_SettingsEx(Structure):
    _fields_ = [("size", c_ulong),
                ("_pSettings_id",POINTER(Settings)),
                ("_private_data",POINTER(c_ulong))]

class QCam_CamListItem(Structure):
    _fields_ = [("cameraId", c_ulong),
                ("cameraType", c_ulong),
                ("uniqueId", c_ulong),
                ("isOpen", c_ulong),
                ("_reserved", c_ulong*10)]
    
class QCam_Frame(Structure):
    _fields_ = [("pBuffer", POINTER(c_ulong*4)),
                 ("bufferSize", c_ulong),
                 ("format", c_ulong),
                 ("width", c_ulong),
                 ("height", c_ulong),
                 ("size", c_ulong),
                 ("bits", c_ushort),
                 ("frameNumber", c_ushort),
                 ("bayerPattern", c_ulong),
                 ("errorCode", c_ulong),
                 ("timeStamp", c_ulong),
                 ("_reserved", c_ulong*8)]
                 
#QCam_Err =     {
#        'qerrSuccess'             : 0,        
#        'qerrNotSupported'        : 1,    # Function is not supported for this device
#        'qerrInvalidValue'        : 2,    # A parameter used was invalid
#        'qerrBadSettings'         : 3,    # The QCam_Settings structure is corrupted
#        'qerrNoUserDriver'        : 4,
#        'qerrNoFirewireDriver'    : 5,    # Firewire device driver is missing
#        'qerrDriverConnection'    : 6,
#        'qerrDriverAlreadyLoaded' : 7,    # The driver has already been loaded
#        'qerrDriverNotLoaded'     : 8,    # The driver has not been loaded.
#        'qerrInvalidHandle'       : 9,    # The QCam_Handle has been corrupted
#        'qerrUnknownCamera'       : 10,   # Camera model is unknown to this version of QCam
#        'qerrInvalidCameraId'     : 11,   # Camera id used in QCam_OpenCamera is invalid
#        'qerrNoMoreConnections'   : 12,   # Deprecated
#        'qerrHardwareFault'       : 13,
#        'qerrFirewireFault'       : 14,
#        'qerrCameraFault'         : 15,
#        'qerrDriverFault'         : 16,
#        'qerrInvalidFrameIndex'   : 17,
#        'qerrBufferTooSmall'      : 18,   # Frame buffer (pBuffer) is too small for image
#        'qerrOutOfMemory'         : 19,
#        'qerrOutOfSharedMemory'   : 20,
#        'qerrBusy'                : 21,   # The function used cannot be processed at this time
#        'qerrQueueFull'           : 22,   # The queue for frame and settings changes is full
#        'qerrCancelled'           : 23,
#        'qerrNotStreaming'        : 24,   # The function used requires that streaming be on
#        'qerrLostSync'            : 25,   # The host and the computer are out of sync, the frame returned is invalid
#        'qerrBlackFill'           : 26,   # Data is missing in the frame returned
#        'qerrFirewireOverflow'    : 27,   # The host has more data than it can process, restart streaming.
#        'qerrUnplugged'           : 28,   # The camera has been unplugged or turned off
#        'qerrAccessDenied'        : 29,   # The camera is already open
#        'qerrStreamFault'         : 30,   # Stream allocation failed, there may not be enough bandwidth
#        'qerrQCamUpdateNeeded'    : 31,   # QCam needs to be updated
#        'qerrRoiTooSmall'         : 32,   # The ROI used is too small
#        'qerr_last'               : 33,
#        '_qerr_force32'           : 0xFFFFFFFF
#    }
                 
class QCam_qcCameraType(Enum):
    qcCameraUnknown         = 0,
    qcCameraMi2             = 1,        # MicroImager II and Retiga 1300
    qcCameraPmi             = 2,
    qcCameraRet1350         = 3,        # Retiga EX
    qcCameraQICam           = 4,
    qcCameraRet1300B        = 5,
    qcCameraRet1350B        = 6,        # Retiga EXi
    qcCameraQICamB          = 7,        # QICam
    qcCameraMicroPub        = 8,        # Micropublisher
    qcCameraRetIT           = 9,
    qcCameraQICamIR         = 10,       # QICam IR
    qcCameraRochester       = 11,
    qcCameraRet4000R        = 12,       # Retiga 4000R
    qcCameraRet2000R        = 13,       # Retiga 2000R
    qcCameraRoleraXR        = 14,       # Rolera XR
    qcCameraRetigaSRV       = 15,       # Retiga SRV
    qcCameraOem3            = 16,
    qcCameraRoleraMGi       = 17,       # Rolera MGi
    qcCameraRet4000RV       = 18,       # Retiga 4000RV
    qcCameraRet2000RV       = 19,       # Retiga 2000RV
    qcCameraOem4            = 20,
    qcCameraGo1             = 21,       # USB CMOS camera
    qcCameraGo3             = 22,       # USB CMOS camera
    qcCameraGo5             = 23,       # USB CMOS camera
    qcCameraGo21            = 24,       # USB CMOS camera
    qcCameraRoleraEMC2      = 25,       
    qcCameraRetigaEXL       = 26,       
    qcCameraRoleraXRL       = 27,       
    qcCameraRetigaSRVL      = 28,
    qcCameraRetiga4000DC    = 29,
    qcCameraRetiga2000DC    = 30,
    qcCameraEXiBlue         = 31,
    qcCameraEXiAqua         = 32,
    qcCameraRetigaIndigo    = 33,
    qcCameraGoBolt          = 34,
    qcCameraX               = 1000,
    qcCameraOem1            = 1001,
    qcCameraOem2            = 1002

class QCam_qcCcdType(Enum):
    qcCcdMonochrome     = 0,
    qcCcdColorBayer     = 1,
    qctype_last         = 2


class QCam_qcCcd(Enum):
    qcCcdKAF1400        = 0,
    qcCcdKAF1600        = 1,
    qcCcdKAF1600L       = 2,
    qcCcdKAF4200        = 3,
    qcCcdICX085AL       = 4,
    qcCcdICX085AK       = 5,
    qcCcdICX285AL       = 6,
    qcCcdICX285AK       = 7,
    qcCcdICX205AL       = 8,
    qcCcdICX205AK       = 9,
    qcCcdICX252AQ       = 10,
    qcCcdS70311006      = 11,
    qcCcdICX282AQ       = 12,
    qcCcdICX407AL       = 13,
    qcCcdS70310908      = 14,
    qcCcdVQE3618L       = 15,
    qcCcdKAI2001gQ      = 16,
    qcCcdKAI2001gN      = 17,
    qcCcdKAI2001MgAR    = 18,
    qcCcdKAI2001CMgAR   = 19,
    qcCcdKAI4020gN      = 20,
    qcCcdKAI4020MgAR    = 21,
    qcCcdKAI4020MgN     = 22,
    qcCcdKAI4020CMgAR   = 23,
    qcCcdKAI1020gN      = 24,
    qcCcdKAI1020MgAR    = 25,
    qcCcdKAI1020MgC     = 26,
    qcCcdKAI1020CMgAR   = 27,
    qcCcdKAI2001MgC     = 28,
    qcCcdKAI2001gAR     = 29,
    qcCcdKAI2001gC      = 30,
    qcCcdKAI2001MgN     = 31,
    qcCcdKAI2001CMgC    = 32,
    qcCcdKAI2001CMgN    = 33,
    qcCcdKAI4020MgC     = 34,
    qcCcdKAI4020gAR     = 35,
    qcCcdKAI4020gQ      = 36,
    qcCcdKAI4020gC      = 37,
    qcCcdKAI4020CMgC    = 38,
    qcCcdKAI4020CMgN    = 39,
    qcCcdKAI1020gAR     = 40,
    qcCcdKAI1020gQ      = 41,
    qcCcdKAI1020gC      = 42,
    qcCcdKAI1020MgN     = 43,
    qcCcdKAI1020CMgC    = 44,
    qcCcdKAI1020CMgN    = 45,
    qcCcdKAI2020MgAR    = 46,
    qcCcdKAI2020MgC     = 47,
    qcCcdKAI2020gAR     = 48,
    qcCcdKAI2020gQ      = 49,
    qcCcdKAI2020gC      = 50,
    qcCcdKAI2020MgN     = 51,
    qcCcdKAI2020gN      = 52,
    qcCcdKAI2020CMgAR   = 53,
    qcCcdKAI2020CMgC    = 54,
    qcCcdKAI2020CMgN    = 55,
    qcCcdKAI2021MgC     = 56,
    qcCcdKAI2021CMgC    = 57,
    qcCcdKAI2021MgAR    = 58,
    qcCcdKAI2021CMgAR   = 59,
    qcCcdKAI2021gAR     = 60,
    qcCcdKAI2021gQ      = 61,
    qcCcdKAI2021gC      = 62,
    qcCcdKAI2021gN      = 63,
    qcCcdKAI2021MgN     = 64,
    qcCcdKAI2021CMgN    = 65,
    qcCcdKAI4021MgC     = 66,
    qcCcdKAI4021CMgC    = 67,
    qcCcdKAI4021MgAR    = 68,
    qcCcdKAI4021CMgAR   = 69,
    qcCcdKAI4021gAR     = 70,
    qcCcdKAI4021gQ      = 71,
    qcCcdKAI4021gC      = 72,
    qcCcdKAI4021gN      = 73,
    qcCcdKAI4021MgN     = 74,
    qcCcdKAI4021CMgN    = 75,
    qcCcdKAF3200M       = 76,
    qcCcdKAF3200ME      = 77,
    qcCcdE2v97B         = 78,
    qcCMOS              = 79,
    qcCcdTX285          = 80,
    qcCcdKAI04022MgC    = 81,
    qcCcdKAI04022CMgC   = 82,
    qcCcdKAI04022MgAR   = 83,
    qcCcdKAI04022CMgAR  = 83,
    qcCcdKAI04022gAR    = 85,
    qcCcdKAI04022gQ     = 86,
    qcCcdKAI04022gC     = 87,
    qcCcdKAI04022gN     = 88,
    qcCcdKAI04022MgN    = 89,
    qcCcdKAI04022CMgN   = 90,
    qcCcd_last          = 91,
    qcCcdX              = 255   # Reserved 

class QCam_qcIntensifierModel(Enum):
    qcItVsStdGenIIIA    = 0,
    qcItVsEbGenIIIA     = 1,
    qcIt_last           = 2

class QCam_qcBayerPattern(Enum):
    qcBayerRGGB         = 0,
    qcBayerGRBG         = 1,
    qcBayerGBRG         = 2,
    qcBayerBGGR         = 3,
    qcBayer_last        = 4

class QCam_qcTriggerType(Enum):
    qcTriggerNone       = 0,        # Depreciated

    # Freerun mode: expose images as fast as possible
    qcTriggerFreerun    = 0,

    # Hardware trigger modes
    qcTriggerEdgeHi     = 1,        # Edge triggers exposure start
    qcTriggerEdgeLow    = 2,
    qcTriggerPulseHi    = 3,        # Integrate over pulse
    qcTriggerPulseLow   = 4,

    # Software trigger (trigger through API call)
    qcTriggerSoftware   = 5,

    # New hardware trigger modes
    qcTriggerStrobeHi   = 6,        # Integrate over pulse without masking
    qcTriggerStrobeLow  = 7,
    qcTrigger_last      = 8

# RGB Filter Wheel Color
class QCam_qcWheelColor(Enum):
    qcWheelRed          = 0,
    qcWheelGreen        = 1,
    qcWheelBlack        = 2,
    qcWheelBlue         = 3,
    qcWheel_last        = 4

# Readout Speed
class QCam_qcReadoutSpeed(Enum):
    qcReadout20M        = 0,
    qcReadout10M        = 1,
    qcReadout5M         = 2,
    qcReadout2M5        = 3,
    qcReadout1M         = 4,
    qcReadout24M        = 5,
    qcReadout48M        = 6,
    qcReadout40M        = 7,
    qcReadout30M        = 8,
    qcReadout_last      = 9



# Readout port
class QCam_qcReadoutPort(Enum):
    qcPortNormal        = 0,
    qcPortEM            = 1,
    qcReadoutPort_last  = 2



# Shutter Control
class QCam_qcShutterControl(Enum):
    qcShutterAuto       = 0,
    qcShutterClose      = 1,
    qcShutterOpen       = 2,
    qcShutter_last      = 3



# Output on the SyncB Port
#
class QCam_qcSyncb(Enum):
    qcSyncbTrigmask     = 0,
    qcSyncbExpose       = 1,
    qcSyncbOem1         = 0,
    qcSyncbOem2         = 1,
    qcSyncb_last        = 2


# Callback Flags
class QCam_qcCallbackFlags(Enum):
    qcCallbackDone          = 1,    # Callback when QueueFrame (or QueueSettings) is done
    qcCallbackExposeDone    = 2     # Callback when exposure is done (readout starts)
                              # - For cameras manufactured after March 1, 2004 and all MicroPublishers
                              # - This callback is not guaranteed to occur



# RTV Mode
class QCam_Mode(Enum):
    qmdStandard             = 0,    # Default camera mode
    qmdRealTimeViewing      = 1,    # Real Time Viewing (RTV) mode, for MicroPublisher only
    qmdOverSample           = 2,    # A mode where you may snap Oversampled images from supported cameras
    qmd_last                = 3,
    _qmd_force32            = 0xFFFFFFFF



# CCD Clearing Mode
class  QCam_qcCCDClearingModes(Enum):
    qcPreFrameClearing      = 0,    # Default mode, clear CCD before next exposure starts 
    qcNonClearing           = 1     # Do not clear CCD before next exposure starts



# Fan Control Speed
class QCam_qcFanSpeed(Enum):
    qcFanSpeedLow           = 1,
    qcFanSpeedMedium        = 2,
    qcFanSpeedHigh          = 3,
    qcFanSpeedFull          = 4



# Image Format
#
# The name of the RGB format indicates how to interpret the data.
# Example: Xrgb32 means the following:
# Byte 1: Alpha (filled to be opaque, since it's not used)
# Byte 2: Red
# Byte 3: Green
# Byte 4: Blue
# The 32 corresponds to 32 bits (4 bytes)
#
# Note: The endianess of the data will be consistent with
# the processor used.
# x86/x64 = Little Endian
# PowerPC = Big Endian
# More information can be found at http:#en.wikipedia.org/wiki/Endianness 
#
# Note: - On color CCDs, 1x1 binning requires a bayer format (ex: qfmtBayer8)
#       - On color CCDs, binning higher than 1x1 requires a mono format (ex: qfmtMono8)
#       - Choosing a color format on a mono CCD will return a 3-shot RGB filter image
#
class QCam_ImageFormat(Enum):
    qfmtRaw8                = 0,    # Raw CCD output (this format is not supported)
    qfmtRaw16               = 1,    # Raw CCD output (this format is not supported)
    qfmtMono8               = 2,    # Data is bytes
    qfmtMono16              = 3,    # Data is shorts, LSB aligned
    qfmtBayer8              = 4,    # Bayer mosaic; data is bytes
    qfmtBayer16             = 5,    # Bayer mosaic; data is shorts, LSB aligned
    qfmtRgbPlane8           = 6,    # Separate color planes
    qfmtRgbPlane16          = 7,    # Separate color planes
    qfmtBgr24               = 8,    # Common Windows format
    qfmtXrgb32              = 9,    # Format of Mac pixelmap
    qfmtRgb48               = 10,
    qfmtBgrx32              = 11,   # Common Windows format
    qfmtRgb24               = 12,   # RGB with no alpha
    qfmt_last               = 13

# Camera Parameters - Unsigned 32 bit
#
# For use with QCam_GetParam, 
#				QCam_GetParamMin
#				QCam_GetParamMax
#				QCam_SetParam
#				QCam_GetParamSparseTable
#				QCam_IsSparseTable
#				QCam_IsRangeTable
#				QCam_IsParamSupported
#
# Note: Cameras produced after Mar 1, 2004 no longer support:
#       qprmGain
#       qprmOffset
#       qprmIntensifierGain
#
#       Please use the following:
#		 qprmNormalizedGain
#		 qprmS32AbsoluteOffset
#       qprm64NormIntensGain
#
# Note: Some parameters may not be supported on each camera.  Please check with QCam_IsParamSupported.
#       
class QCam_Param(Enum):
    qprmGain                        = 0,    # Deprecated
    qprmOffset                      = 1,    # Deprecated
    qprmExposure                    = 2,    # Exposure in microseconds
    qprmBinning                     = 3,    # Symmetrical binning	(ex: 1x1 or 4x4)
    qprmHorizontalBinning           = 4,    # Horizonal binning	(ex: 2x1)
    qprmVerticalBinning             = 5,    # Vertical binning		(ex: 1x4)
    qprmReadoutSpeed                = 6,    # Readout speed (see QCam_qcReadoutSpeed)
    qprmTriggerType                 = 7,    # Trigger type (see QCam_qcTriggerType)
    qprmColorWheel                  = 8,    # Manual control of current RGB filter wheel color
    qprmCoolerActive                = 9,    # 1 turns cooler on, 0 turns off
    qprmExposureRed                 = 10,   # For RGB filter mode, exposure (us) of red shot
    qprmExposureBlue                = 11,   # For RGB filter mode, exposure (us) of blue shot
    qprmImageFormat                 = 12,   # Image format (see QCam_ImageFormat)
    qprmRoiX                        = 13,   # Upper left X coordinate of the ROI
    qprmRoiY                        = 14,   # Upper left Y coordinate of the ROI
    qprmRoiWidth                    = 15,   # Width of ROI, in pixels
    qprmRoiHeight                   = 16,   # Height of ROI, in pixels
    qprmReserved1                   = 17,
    qprmShutterState                = 18,   # Shutter position
    qprmReserved2                   = 19,
    qprmSyncb                       = 20,   # Output type for SyncB port (see QCam_qcSyncb)
    qprmReserved3                   = 21,
    qprmIntensifierGain             = 22,   # Deprecated
    qprmTriggerDelay                = 23,   # Trigger delay in nanoseconds
    qprmCameraMode                  = 24,   # Camera mode (see QCam_Mode)
    qprmNormalizedGain              = 25,   # Normalized camera gain (micro units)
    qprmNormIntensGaindB            = 26,   # Normalized intensifier gain dB (micro units)
    qprmDoPostProcessing            = 27,   # Turns post processing on and off, 1 = On 0 = Off
    qprmPostProcessGainRed          = 28,   # Post processing red gain
    qprmPostProcessGainGreen        = 29,   # Post processing green gain
    qprmPostProcessGainBlue         = 30,   # Post processing blue gain
    qprmPostProcessBayerAlgorithm   = 31,   # Post processing bayer algorithm to use (see QCam_qcBayerInterp in QCamImgfnc.h)
    qprmPostProcessImageFormat      = 32,   # Post processing image format	
    qprmFan                         = 33,   # Fan speed (see QCam_qcFanSpeed)
    qprmBlackoutMode                = 34,   # Blackout mode, 1 turns all lights off, 0 turns them back on
    qprmHighSensitivityMode         = 35,   # High sensitivity mode, 1 turns high sensitivity mode on, 0 turns it off
    qprmReadoutPort                 = 36,   # The readout port (see QCam_qcReadoutPort)
    qprmEMGain                      = 37,   # EM (Electron Multiplication) Gain 
    qprmOpenDelay                   = 38,   # Open delay for the shutter.  Range is 0-419.43ms.  Must be smaller than expose time - 10us.  (micro units)
    qprmCloseDelay                  = 39,   # Close delay for the shutter.  Range is 0-419.43ms.  Must be smaller than expose time - 10us.  (micro units)
    qprmCCDClearingMode             = 40,   # CCD clearing mode (see QCam_qcCCDClearingModes)
    qprmOverSample                  = 41,   # set the oversample mode, only available on qcCameraGo21
    qprmReserved5                   = 42,   
    qprmReserved6                   = 43,   
    qprmReserved7                   = 44,   
    qprmReserved4                   = 45,   # QImaging OEM reserved parameter
    qprmReserved8                   = 46,   # QImaging OEM reserved parameter
    qprmEasyEmMode                  = 47,
    qprmLockedGainMode              = 48,
    qprmEasyEmGainValue10           = 49,
    qprmEasyEmGainValue20           = 50,
    qprmEasyEmGainValue40           = 51,
    qprmFrameBufferLength           = 52,
    qprm_last                       = 53,
    _qprm_force32                   = 0xFFFFFFFF

# Camera Parameters - Signed 32 bit
#
# For use with QCam_GetParamS32, 
#				QCam_GetParamS32Min
#				QCam_GetParamS32Max
#				QCam_SetParamS32
#				QCam_GetParamSparseTableS32
#				QCam_IsSparseTableS32
#				QCam_IsRangeTableS32
#				QCam_IsParamS32Supported
#
class QCam_ParamS32(Enum):
    qprmS32NormalizedGaindB     = 0,    # Normalized camera gain in dB (micro units)
    qprmS32AbsoluteOffset       = 1,    # Absolute camera offset
    qprmS32RegulatedCoolingTemp = 2,    # Regulated cooling temperature (C)
    qprmS32_last                = 3,
    _qprmS32_force32            = 0xFFFFFFFF

# Camera Parameters - Unsigned 64 bit
#
# For use with QCam_GetParam64, 
#				QCam_GetParam64Min
#				QCam_GetParam64Max
#				QCam_SetParam64
#				QCam_GetParamSparseTable64
#				QCam_IsSparseTable64
#				QCam_IsRangeTable64
#				QCam_IsParam64Supported
#
class QCam_Param64(Enum):
    qprm64Exposure          = 0,    # Exposure in nanoseconds
    qprm64ExposureRed       = 1,    # For RGB filter mode, exposure (nanoseconds) of red shot
    qprm64ExposureBlue      = 2,    # For RGB filter mode, exposure (nanoseconds) of blue shot
    qprm64NormIntensGain    = 3,    # Normalized intensifier gain (micro units)
    qprm64_last             = 4,

# Camera Info Parameters
#
# For use with QCam_GetInfo
#
class QCam_Info(Enum):
    qinfCameraType              = 0,    # Camera model (see QCam_qcCameraType)
    qinfSerialNumber            = 1,    # Deprecated
    qinfHardwareVersion         = 2,    # Hardware version
    qinfFirmwareVersion         = 3,    # Firmware version
    qinfCcd                     = 4,    # CCD model (see QCam_qcCcd)
    qinfBitDepth                = 5,    # Maximum bit depth
    qinfCooled                  = 6,    # Returns 1 if cooler is available, 0 if not
    qinfReserved1               = 7,    # Reserved
    qinfImageWidth              = 8,    # Width of the ROI (in pixels)
    qinfImageHeight             = 9,    # Height of the ROI (in pixels)
    qinfImageSize               = 10,   # Size of returned image (in bytes)
    qinfCcdType                 = 11,   # CDD type (see QCam_qcCcdType)
    qinfCcdWidth                = 12,   # CCD maximum width
    qinfCcdHeight               = 13,   # CCD maximum height
    qinfFirmwareBuild           = 14,   # Build number of the firmware
    qinfUniqueId                = 15,   # Same as uniqueId in QCam_CamListItem
    qinfIsModelB                = 16,   # Cameras manufactured after March 1, 2004 return 1, otherwise 0
    qinfIntensifierModel        = 17,   # Intensifier tube model (see QCam_qcIntensifierModel)
    qinfExposureRes             = 18,   # Exposure time resolution (nanoseconds)
    qinfTriggerDelayRes         = 19,   # Trigger delay Resolution (nanoseconds)
    qinfStreamVersion           = 20,   # Streaming version
    qinfNormGainSigFigs         = 21,   # Normalized Gain Significant Figures resolution
    qinfNormGaindBRes           = 22,   # Normalized Gain dB resolution (in micro units)
    qinfNormITGainSigFigs       = 23,   # Normalized Intensifier Gain Significant Figures
    qinfNormITGaindBRes         = 24,   # Normalized Intensifier Gain dB resolution (micro units)
    qinfRegulatedCooling        = 25,   # 1 if camera has regulated cooling
    qinfRegulatedCoolingLock    = 26,   # 1 if camera is at regulated temperature, 0 otherwise
    qinfFanControl              = 29,   # 1 if camera can control fan speed
    qinfHighSensitivityMode     = 30,   # 1 if camera has high sensitivity mode available
    qinfBlackoutMode            = 31,   # 1 if camera has blackout mode available
    qinfPostProcessImageSize    = 32,   # Returns the size (in bytes) of the post-processed image
    qinfAsymmetricalBinning     = 33,   # 1 if camera has asymmetrical binning (ex: 2x4)
    qinfEMGain                  = 34,   # 1 if EM gain is supported, 0 if not
    qinfOpenDelay               = 35,   # 1 if shutter open delay controls are available, 0 if not
    qinfCloseDelay              = 36,   # 1 if shutter close delay controls are available, 0 if not
    qinfColorWheelSupported     = 37,   # 1 if color wheel is supported, 0 if not	
    qinfReserved2               = 38,   
    qinfReserved3               = 39,   
    qinfReserved4               = 40,   
    qinfReserved5               = 41,
    qinfEasyEmModeSupported     = 42,   # 1 if camera supports Easy EM mode
    qinfLockedGainModeSupported = 43,
    qinf_last                   = 44,
    _qinf_force32               = 0xFFFFFFFF


# Error Codes
class QCam_Err(Enum):
    qerrSuccess             = 0,        
    qerrNotSupported        = 1,    # Function is not supported for this device
    qerrInvalidValue        = 2,    # A parameter used was invalid
    qerrBadSettings         = 3,    # The QCam_Settings structure is corrupted
    qerrNoUserDriver        = 4,
    qerrNoFirewireDriver    = 5,    # Firewire device driver is missing
    qerrDriverConnection    = 6,
    qerrDriverAlreadyLoaded = 7,    # The driver has already been loaded
    qerrDriverNotLoaded     = 8,    # The driver has not been loaded.
    qerrInvalidHandle       = 9,    # The QCam_Handle has been corrupted
    qerrUnknownCamera       = 10,   # Camera model is unknown to this version of QCam
    qerrInvalidCameraId     = 11,   # Camera id used in QCam_OpenCamera is invalid
    qerrNoMoreConnections   = 12,   # Deprecated
    qerrHardwareFault       = 13,
    qerrFirewireFault       = 14,
    qerrCameraFault         = 15,
    qerrDriverFault         = 16,
    qerrInvalidFrameIndex   = 17,
    qerrBufferTooSmall      = 18,   # Frame buffer (pBuffer) is too small for image
    qerrOutOfMemory         = 19,
    qerrOutOfSharedMemory   = 20,
    qerrBusy                = 21,   # The function used cannot be processed at this time
    qerrQueueFull           = 22,   # The queue for frame and settings changes is full
    qerrCancelled           = 23,
    qerrNotStreaming        = 24,   # The function used requires that streaming be on
    qerrLostSync            = 25,   # The host and the computer are out of sync, the frame returned is invalid
    qerrBlackFill           = 26,   # Data is missing in the frame returned
    qerrFirewireOverflow    = 27,   # The host has more data than it can process, restart streaming.
    qerrUnplugged           = 28,   # The camera has been unplugged or turned off
    qerrAccessDenied        = 29,   # The camera is already open
    qerrStreamFault         = 30,   # Stream allocation failed, there may not be enough bandwidth
    qerrQCamUpdateNeeded    = 31,   # QCam needs to be updated
    qerrRoiTooSmall         = 32,   # The ROI used is too small
    qerr_last               = 33,
    _qerr_force32           = 0xFFFFFFFF



                 
