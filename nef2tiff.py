# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:01:53 2020

BGR2Gray

@author: jonas
"""

import cv2
import os
import rawpy

def nef2tiff(ORIGIN_PATH,DESTIN_PATH,module):
    for filename in os.listdir(ORIGIN_PATH): 
        if filename.find(str(module))!=-1 and filename.find('NEF')!=-1:
        # if filename[len(filename)-3:]=='nef':    
            
            #filename = '601867_200506_10_0,0.nef'
            #img = io.imread('C:\\Users\\jonasrw\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\Ibg\\'+ filename)
            
            raw_py = rawpy.imread(ORIGIN_PATH + filename)
            #plt.imshow(raw_io)
            rgb = raw_py.postprocess()
         #  print(image)
              
            image_gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
            #gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
        #    img = cv2.cvtColor(cv2.imread(ORIGIN_PATH + filename), cv2.COLOR_BGR2GRAY)  
            filename = filename[:len(filename)-3]    
            tiff = 'tiff'                                                                                                                                          
            cv2.imwrite(DESTIN_PATH + filename +tiff,image_gray) 

if __name__=="__main__":
    
  #  ORIGIN_PATH = "C:/Users/jonasrw/OneDrive - Norwegian University of Life Sciences/skole/Master IFE BIPV/Kode/nef2x/Input/" #
   # DESTIN_PATH = "C:/Users/jonasrw/OneDrive - Norwegian University of Life Sciences/skole/Master IFE BIPV/Kode/nef2x/Output/" #
    # #nef2tiff(ORIGIN_PATH,DESTIN_PATH)
    
    # ORIGIN_PATH = 'C:\\Users\\jonasrw\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\'
    # DESTIN_PATH = 'C:\\Users\\jonasrw\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601873\\'
    # for filename in os.listdir(ORIGIN_PATH): 

        
    
    ORIGIN_PATH = 'C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03(linear)\\WW-cam\\'
    DESTIN_PATH = 'C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03(linear)\WW-cam\\WW-cam-tiff\\'
    nef2tiff(ORIGIN_PATH,DESTIN_PATH,'DSC')
#cv2.imwrite('C:\Users\jonas\OneDrive - Norwegian University of Life Sciences\skole\Master IFE BIPV\EL-bilder\2020.01.16 - test\DC 8bit\8bit_601817_200116_1_0,0.png', image_gray)
