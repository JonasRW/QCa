# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:10:05 2020

@author: jonas
"""

from LELa import LEL_M
import os
import pandas as pd
import matplotlib.pyplot as plt
import skimage.io as io
def qca(folder_with_img,calibration_img_PATH,DESTIN_PATH,yymmdd):
    lel_Mo, th_Mo, img_ROI_Mo = LEL_M(calibration_img_PATH,calibration_img_PATH)
    qD_9 = pd.DataFrame()
    qD_2 = pd.DataFrame()
    case_1 = []
    D_1 =[]
    case_2 = []
    D_2 =[]
    for filename in os.listdir(folder_with_img):
        lel_M, th_M, img_ROI_M = LEL_M(folder_with_img+filename,calibration_img_PATH)
        img_RGB_diff = img_ROI_M
        img_RGB_diff[img_ROI_Mo[:,:,0]==255] = 0,0,0
        c= (filename.split('-')[1]).split('_')[0]
        i=float(filename[-8:-5].replace(',','.'))
        d=round(lel_M-lel_Mo,2)
        if i == 9.0:
            case_1.append(c)
            D_1.append(d) 
        else:
            case_2.append(c)
            D_2.append(d)            
        
        plt.figure()
        io.imshow(img_RGB_diff)    
        plt.title('Degraded area in red of case:'+c+', I:'+str(i))
        #plt.imsave('601872_200506_1_9,0_D.tiff',img_ROI_diff)
        plt.imsave(DESTIN_PATH+'601873_200603_1_9,0_D-'+d.astype(str)+'_red.tiff',img_RGB_diff)
        
    qD_9['Case']=case_1
    # qD['I']=I
    qD_9['D']=D_1
    qD_2['Case']=case_2
    # qD['I']=I
    qD_2['D']=D_2
    return qD_9,qD_2
if __name__=="__main__":
   # calibration_img_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\Til Jonas\\6018xx-191015-test-tif\\IxIbg_Output\\601871-191015_191015_1_9,000000.xIbg.tiff"
    calibration_img_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601864_tiff\\601864-9-0,9_200603_1_9,0.tiff" #I_Input\\9\\601861-191015_191015_1_9,000000.tiff" 
    #calibration_img_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\xIbg_Input\\601871_200506_1_9,0.tiff" #I_Input\\9\\601861-191015_191015_1_9,000000.tiff" 
    cracked_img_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601873_tiff\\601873_2_200603_1_9,0.tiff"    #cracked_img_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\xIbg_Input\\601872_200506_1_9,0.tiff" 
    folder_with_img = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601873_tiff\\"    #cracked_img_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\xIbg_Input\\601872_200506_1_9,0.tiff" 
    DESTIN_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601873_D\\"
    
    qD_9,qD_2 = qca(folder_with_img,calibration_img_PATH,DESTIN_PATH,200603)
    qD_9.to_csv(DESTIN_PATH+'Degredation at 9A.csv')
    qD_2.to_csv(DESTIN_PATH+'Degredation at 2A.csv')
    
    