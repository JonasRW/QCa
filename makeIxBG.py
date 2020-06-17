# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:32:04 2020
Exclude BG
@author: jonas
"""
import os
import skimage.io as io
import cv2
import numpy as np
from getIbg import getIbg
from nef2tiff import nef2tiff

def xIbg(ORIGIN_PATH,DESTIN_PATH,Ibg_PATH):

    for filename in os.listdir(ORIGIN_PATH):
        Ibg = io.imread(Ibg_PATH)
        img = io.imread(ORIGIN_PATH + filename)
        #image_gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY) Implement if time
    #    img = cv2.cvtColor(cv2.imread(ORIGIN_PATH + filename), cv2.COLOR_BGR2GRAY)  
        #imgxIbg = img-Ibg
        imgxIbg = cv2.subtract(img,Ibg)
        #cv2.imshow(imgSubIbg)
        #io.imshow(imgSubIbg)
        #np.min(imgxIbg)
        #th = 0
        #imgxIbg = imgxIbg > th
        filename = filename[:len(filename)-4]
        edt = 'xIbg'
        tiff = '.tiff'                                                                                                                                          
        cv2.imwrite(DESTIN_PATH + filename +edt +tiff,imgxIbg) 
        
if __name__=="__main__":
    
    #%% Creat Ibg
    #ORIGIN_PATH = 'C:\\Users\\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\Ibg_raw\\'
    #DESTIN_PATH = 'C:\\Users\\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\Ibg_Input\\'
    #nef2tiff(ORIGIN_PATH,DESTIN_PATH)
    
    ORIGIN_PATH = 'C:\\Users\\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\Ibg_Input\\'
    DESTIN_PATH = 'C:\\Users\\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\avIbg\\'
    getIbg(ORIGIN_PATH,DESTIN_PATH)
    
    
    #%% xIbg
    
    ORIGIN_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.25\\Ibg-Input\\" #
    DESTIN_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.25\\Ibg-Input\\tiff\\" #
    nef2tiff(ORIGIN_PATH,DESTIN_PATH)
    
    ORIGIN_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\xIb_Input\\" #
    DESTIN_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\xIbg\\" #
    
    Ibg_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\avIbg\\Ibg.tiff" #
    xIbg(ORIGIN_PATH,DESTIN_PATH,Ibg_PATH)
