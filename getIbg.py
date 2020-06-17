# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:32:23 2020
Ibg as average
@author: jonas
"""


import os
import skimage.io as io
import cv2
import numpy as np




def getIbg(ORIGIN_PATH,DESTIN_PATH):

    imgs = [io.imread(ORIGIN_PATH + filename) for filename in os.listdir(ORIGIN_PATH)]
    imgs = np.stack(imgs, axis=2)
    Ibg = np.average(imgs,axis=2).astype(int)
    #io.imshow(Ibg)
    cv2.imwrite(DESTIN_PATH + 'Ibg.tiff',Ibg)
    return Ibg

if __name__=="__main__":
    ORIGIN_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\Til Jonas\\6018xx-191015-test-tif\\Ibg_Input\\" #
    DESTIN_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\Til Jonas\\6018xx-191015-test-tif\\Ibg\\" #
    Ibg = getIbg(ORIGIN_PATH,DESTIN_PATH)
