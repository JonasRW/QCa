# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:41:11 2020

Quantifying Solar Cell Cracks in Photovoltaic Modules. IEC-DTS 60904-13.

@author: io318
"""
import cv2
import skimage.io as io
import numpy as np
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
from skimage.filters import laplace
from skimage.filters import gaussian
from skimage import feature
from newROI import createROI
#%% Otsu on normalized histogram
    
def ELavOtsu(calibration_img_PATH):
    img = io.imread(calibration_img_PATH)
    img = rgb2gray(img)

    img = cv2.bilateralFilter(img,9,75,75) 
    
    img_roi = createROI(img)

    img_ROI = img_roi.copy()
    img_ROI[img_ROI == 0] = 255
    img_ROI = cv2.multiply(img,img_roi,dtype=cv2.CV_8U)#.astype(np.uint8)
    th2,roi2 = cv2.threshold(img_ROI[img_ROI<254],0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    
    return th2,img_roi

def LEL_M(cracked_img_PATH,calibration_img_PATH):

    c_img = io.imread(cracked_img_PATH)
    c_img = rgb2gray(c_img)
    c_img = cv2.bilateralFilter(c_img,9,75,75)    
    
    th,roi = ELavOtsu(calibration_img_PATH)

    roi = roi.astype(float)
    roi[roi == 0] = np.nan
    
    img_ROI = cv2.multiply(c_img.astype(float),roi)

    img_RGB = cv2.cvtColor(c_img,cv2.COLOR_GRAY2BGR)#.astype(float)

    img_RGB[img_ROI<th] = 255,0,0  

    roi = (roi*255).astype(np.uint8)
    hist = cv2.calcHist([c_img],[0],roi,[256],[0,256])
    img_ROI = np.ma.masked_invalid(img_ROI)#.astype(np.uint8)
    lel2 = 0
    for i in range(int(th+1)):
        lel2 += int(hist[i])
    lel2 = 100*(lel2/(img_ROI.count())) #Her må det deles på antall "levende" pixler    

    return lel2, th, img_RGB  

if __name__ == "__main__":
   # calibration_img_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\Til Jonas\\6018xx-191015-test-tif\\IxIbg_Output\\601871-191015_191015_1_9,000000.xIbg.tiff"
    calibration_img_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601864_tiff\\601864-9-0,9_200603_1_9,0.tiff" #I_Input\\9\\601861-191015_191015_1_9,000000.tiff" 
    #calibration_img_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\xIbg_Input\\601871_200506_1_9,0.tiff" #I_Input\\9\\601861-191015_191015_1_9,000000.tiff" 
   
    cracked_img_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601873_tiff\\601873_2_200603_1_9,0.tiff"    #cracked_img_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\xIbg_Input\\601872_200506_1_9,0.tiff"
    
    lel_Mo, th_Mo, img_ROI_Mo = LEL_M(calibration_img_PATH,calibration_img_PATH)
    plt.figure()
    io.imshow(img_ROI_Mo)    
    plt.title('Low EL area with of calibration image')
    
    lel_M, th_M, img_ROI_M = LEL_M(cracked_img_PATH,calibration_img_PATH)
    plt.figure()
    io.imshow(img_ROI_M)    
    plt.title('Low EL area of craked module')

    img_RGB_diff = img_ROI_M
    img_RGB_diff[img_ROI_Mo[:,:,0]==255] = 0,0,0

    D2 = lel_M-lel_Mo

    plt.figure()
    io.imshow(img_RGB_diff)    
    plt.title('Degraded area in red')
    #plt.imsave('601872_200506_1_9,0_D.tiff',img_ROI_diff)
    plt.imsave('601873_200603_1_9,0_D2-'+D2.astype(str)+'_red.tiff',img_RGB_diff)

    
    

    
    

