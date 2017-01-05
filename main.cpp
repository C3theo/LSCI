/*
	qcamLSCI
*/



#include "QCamApi.h"
#include "QCamImgfnc.h"
#include "QImgTypes.h"




// global
QCam_Handle handle;
QCam_ImageFormat format = qfmtMono8;
int exposure = 100; 
unsigned long ccdType;
int cooler; 

/*Function Prototypes TODO: QCAM Class*/
QCam_Handle openQCam(QCam_Handle handle);
void killQCam(QCam_Handle handle);
void setQCam(QCam_Handle handle, unsigned long ccdType, unsigned long exposure, unsigned long cooler, QCam_ImageFormat* pFormat);
void snapMono(QCam_Handle handle);
void snapBayer(QCam_Handle handle, QCam_ImageFormat format);





// Function Definitions

/*openQCam

*/

QCam_Handle openQCam(QCam_Handle handle) {
	
	QCam_CamListItem list[10];
	unsigned long listLen = sizeof(list);


	QCam_LoadDriver();
	QCam_ListCameras(list, &listLen);

	// Open Camera
	if ((listLen > 0) && (list[0].isOpen == false)) // 1 if already open, 0 if closed
	{
		QCam_OpenCamera(list[0].cameraId, &handle);
	}

	return handle;
}

/* killQCam

*/

void killQCam(QCam_Handle handle) {

	QCam_CloseCamera(&handle);
	QCam_ReleaseDriver();
}

/* setQCam
Notes: 
	exposure in us
*/

void setQCam(QCam_Handle handle, unsigned long ccdType, unsigned long exposure, unsigned long cooler, QCam_ImageFormat* pFormat)
{
	

	QCam_GetInfo(handle, qinfCcd, &ccdType); //Set CCD 
	QCam_SettingsEx      settings;
	QCam_ImageFormat     format;
	unsigned long        expMax;
	unsigned long        expMin;
	unsigned long        uTable[32];
	int                  uSize = 32;
	int                  i;

	// Get default settings from the camera.

	 QCam_CreateCameraSettingsStruct(&settings);

	 QCam_InitializeCameraSettings(handle, &settings);
	
	 QCam_ReadDefaultSettings(handle, (QCam_Settings*)&settings);
	
	// Get min/max exposure times.

	 QCam_GetParamMin((QCam_Settings*)&settings, qprmExposure, &expMin);

	 QCam_GetParamMax((QCam_Settings*)&settings, qprmExposure, &expMax);
	
	// Turn Cooling ON/OFF 

	 QCam_SetParam((QCam_Settings*)&settings, qprmCoolerActive, cooler);
	

	// Set exposure time
	 QCam_SetParam((QCam_Settings*)&settings, qprmExposure, exposure);
	

	// Set the format... either 16 bit mono or 16 bit bayer.

	 QCam_GetParamSparseTable((QCam_Settings*)&settings, qprmImageFormat, uTable, &uSize);

	format = (ccdType == qcCcdColorBayer) ? qfmtBayer16 : qfmtMono16;

	for (i = 0; i<uSize; i++)
	{
		if (format == (QCam_ImageFormat)uTable[i])
			break;
	}

	// If we support the 16-bit format use it.  Else, drop down to 8-bit
	if (format != (QCam_ImageFormat)uTable[i])
		format = (qfmtBayer16 == format ? qfmtBayer8 : qfmtMono8);


	 QCam_SetParam((QCam_Settings*)&settings, qprmImageFormat, format);

	*pFormat = format;

	// Set the exposure time.  Validate against max and min exposure times.

	if (exposure < expMin)
	{
		printf("Exposure is too small, adjusting to %u us.\n", expMin);
		exposure = expMin;
	}
	else if (exposure > expMax)
	{
		printf("Exposure is too large, adjusting to %u us.\n", expMax);
		exposure = expMax;
	}

	// Here's where the camera is changed.

	 QCam_SendSettingsToCam(handle, (QCam_Settings*)&settings);
}


/*Image Functions*/


/*snapMono
*/

void snapMono(QCam_Handle handle)
{
	
	unsigned long       imageSize;            // Size of image in bytes
	QCam_Frame          frame;


	// Get size of image.
	 QCam_GetInfo(handle, qinfImageSize, &imageSize);
	

	// Create our frame buffer.
	frame.pBuffer = new unsigned char[imageSize];
	frame.bufferSize = imageSize;

	// Grab the frame.
	QCam_GrabFrame(handle, &frame);

	// Delete the frame buffer.    
	delete frame.pBuffer;

	
}

/*snapBayer

*/

void  snapBayer(QCam_Handle handle, QCam_ImageFormat format)
{
	
	unsigned long       imageSize;            // Size of image in bytes
	QCam_Frame          frame;


	// Get size of image.
	QCam_GetInfo(handle, qinfImageSize, &imageSize);
	

	// Create our frame buffer.
	frame.pBuffer = new unsigned char[imageSize];
	frame.bufferSize = imageSize;

	// Grab the frame.
	 QCam_GrabFrame(handle, &frame);
	
		QCam_Frame        frameInterp;
		unsigned long     interpSize;            // Size of interpolated image.

		if (format == qfmtBayer16)
			format = qfmtRgb48;
		else if (format = qfmtBayer8)
			format = qfmtBgr24;

		// Get size of interpolated image.
		interpSize = QCam_CalcImageSize(format, frame.width, frame.height);

		// Create a buffer for the interpolated image.
		frameInterp.pBuffer = new unsigned char[interpSize];
		frameInterp.bufferSize = interpSize;
		frameInterp.format = format;

		// Bayer interpolation.  Note: we don't do color balance.
		QCam_BayerToRgb(qcBayerInterpAvg4, &frame, &frameInterp);


		
		// Delete the interpolation buffer.
		delete frameInterp.pBuffer;
	

	// Delete the frame buffer.    
	delete frame.pBuffer;

	
}


