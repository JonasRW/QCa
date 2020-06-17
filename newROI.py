'''
Created on 16.03.2018

@author: oezkan
'''
import cv2
import numpy as np

def mainBorder(img):
    '''
    This function extracts the main border.
    It has to be applied after histogram equalization!
    '''
    
     #possibly lower threshold?
    th,_ = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    _,ROI = cv2.threshold(img,th+20,255,cv2.THRESH_BINARY)
    invertROI = cv2.bitwise_not(ROI)
    # plt.figure()
    # plt.imshow(invertROI)
    # plt.title('invROI')
    
    #setting rectangle kernels
    rect_y = cv2.getStructuringElement(cv2.MORPH_RECT,(8,int(img.shape[0]/6))) 
    rect_x = cv2.getStructuringElement(cv2.MORPH_RECT,(int(img.shape[1]/6),8))
    
    rect_opened_y = cv2.morphologyEx(invertROI,cv2.MORPH_OPEN,rect_y)
    rect_opened_y = cv2.bitwise_not(rect_opened_y)
    # plt.figure()
    # plt.imshow(rect_opened_y)
    # plt.title('y')
    
    rect_opened_x = cv2.morphologyEx(invertROI,cv2.MORPH_OPEN,rect_x)
    rect_opened_x = cv2.bitwise_not(rect_opened_x)
    # plt.figure()
    # plt.imshow(rect_opened_x)
    # plt.title('x')
    

    rect = rect_opened_x * rect_opened_y
    # plt.figure()
    # plt.imshow(rect)
    # # plt.title('rect')
    
    #%% Increas thickness of boarder to cover all.
    kernel_x = np.ones((1,8),np.uint8)
    img_morph2 = cv2.morphologyEx(rect, cv2.MORPH_ERODE, kernel_x) #colse more  
    kernel_y = np.ones((8,1),np.uint8)
    img_morph1 = cv2.morphologyEx(rect, cv2.MORPH_ERODE, kernel_y)
    
    img_morph = img_morph2 * img_morph1 
    # plt.figure()
    # plt.imshow(img_morph)   
    # plt.title('border')
    
    return img_morph

#%%
def busBars(img):
    '''
    This function extracts the main border and bus bars together.
    It has to be applied after histogram equalization!
    '''
    border = mainBorder(img)
    th,_ = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    _,ROI = cv2.threshold(img,th+20,255,cv2.THRESH_BINARY) #Increase thershold 
    # to include all endges and busbars.
    # plt.figure()
    # plt.imshow(ROI)

    invertROI = cv2.bitwise_not(ROI)
    # plt.figure()
    # plt.imshow(invertROI)
    
    #%% Creat ROI of module without edges and boarders
    _,ROI = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(32,32))
    ROI = cv2.morphologyEx(ROI, cv2.MORPH_CLOSE, kernel)
    
    #%% Invert detected boarder to detect busbars
    invborder = cv2.bitwise_not((border*255).astype(np.uint8))
    # plt.figure()
    # plt.imshow(invborder)
    ROI *= invborder.astype(ROI.dtype) #Get busbars.
    # plt.figure()
    # plt.imshow(ROI) 
    # plt.title('Busbars1')
    
    center = cv2.getStructuringElement(cv2.MORPH_RECT,(16,16)) 
    center_opened = cv2.morphologyEx(invertROI,cv2.MORPH_OPEN,center) #Detecti
    center_opened = cv2.bitwise_not(center_opened)
    # #center edges.
    # plt.figure()
    # plt.imshow(center_opened)
    
    rect_y = cv2.getStructuringElement(cv2.MORPH_RECT,(1,400)) #Try scale of image dim?
    #reduced to filter out more of the busbars
    rect_opened_y = cv2.morphologyEx(ROI,cv2.MORPH_OPEN,rect_y) #Detectin
    #g vertical busbars, specify in lab manual.
    rect_opened_y = cv2.bitwise_not((rect_opened_y*255).astype(np.uint8))
    
    busbars = center_opened*rect_opened_y
    # plt.figure()
    # plt.imshow('busbars2')
    
    
    return busbars,border


def createROI(img_in):
    '''
    This function gets main border and bus bars together.
    It needs to be applied on an image which has histogram equalization!!!!!!!!!!!!
    '''
    bus_bars,border = busBars(img_in)

    ROI = (bus_bars*border)#/255
    
    return ROI

if __name__ == '__main__':

    #Image path: change to load own images
    img_path = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\Til Jonas\\6018xx-191015-test-tif\\IxIbg_Output\\601860-191015_191015_1_9,000000.xIbg.tiff"#'RawImages/maske+crop-savetest.png' #crack_image.tif
    
            
    
