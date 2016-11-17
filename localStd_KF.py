# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:24:10 2016

@author: kayvanf
"""
import numpy as N
from scipy import signal
import tifffile as T
#from skimage import data
#from skimage.morphology import disk
import time


class LCSI():    
    def getMask(self,r):
        x = N.linspace(-r,r,2*r)
        X,Y = N.meshgrid(x,x)
        rho = N.hypot(X,Y)
        msk = (rho<r).astype(float)
        self.msk = msk/msk.sum()
        return 0
    
    def lstd(self,arr):
        if not hasattr(self,'msk'):
            self.getMask(2)
        kernel = self.msk
        ex = signal.fftconvolve(arr,kernel,mode="same")
        ex2 = signal.fftconvolve(arr**2,kernel,mode="same")
        self.img_lstd = N.sqrt(abs(ex2 - ex**2))
#        return img_lstd
        
    def doAll(self,arr,ff=200,lf=400):
        nz,ny,nx = arr.shape
        self.tmp = N.zeros((lf-ff,ny,nx))
        for i in range(ff,lf):
            self.lstd(arr[i])
            self.tmp[i-lf] = self.img_lstd.copy()
        return 0
    
    def averageAll(self,verbose=True):
        nz,ny,nx = self.tmp.shape
        avg = N.zeros((ny,nx),dtype=N.float64)
        for i in range(nz):
            avg+=(self.tmp[i]/nz)
        if verbose:
            T.imshow(avg)
        self.avg = avg
        
    def decode_bayer(self,arr):
        if arr.ndim==3:
            nz,ny,nx = arr.shape
        else:
            ny,nx = arr.shape
            nz=1
        i = N.arange(0,ny-1,2)
        j = N.arange(0,nx-1,2)
        res = N.zeros((4,nz,ny/2,nx/2))
        for a in range(2):
            for b in range(2):
                X,Y = N.meshgrid(j+a,i+b)
                if arr.ndim==3:
                    res[a*2+b] = arr[:,Y,X]
                else:
                    res[a*2+b] = arr[Y,X]
        return res

    def tempStd(self,arr):
        nz,ny,nx = arr.shape
        tmp = N.zeros((ny,nx))
        for i in range(ny):
            for j in range(nx):
                tmp[i,j] = arr[:,i,j].std()
        return tmp


        