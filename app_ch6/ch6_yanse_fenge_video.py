# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:39:38 2020

@author: YUANLI
"""

import cv2
import numpy as np
cap=cv2.VideoCapture(0)
#image=cv2.imread("./src/7.png")
while(1):
    ret,image=cap.read()
#    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
 
    
#    # 蓝色目标的上限、下限
    lower=np.array([100,60,100])
    upper=np.array([120,120,180])
#    
      # 肤色目标的上限、下限
#    lower=np.array([0, 43, 46])
#    upper=np.array([24, 255, 255])
    
    mask=cv2.inRange(hsv,lower,upper)
    res=cv2.bitwise_and(image,image,mask=mask)
    cv2.imshow('image',image)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    #cv2.waitKey(0)
    k=cv2.waitKey(5)&0xff
    if k==27:
        break
cv2.destroyAllWindows()