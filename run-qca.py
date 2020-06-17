# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:08:21 2020

@author: jonas
"""
from QCA import qca
from getLIVdata import getLIVdata
import matplotlib.pyplot as plt
import tikzplotlib

calibration_img_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601864_tiff\\601864-9-0,9_200603_1_9,0.tiff" #I_Input\\9\\601861-191015_191015_1_9,000000.tiff" 
#calibration_img_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\xIbg_Input\\601871_200506_1_9,0.tiff" #I_Input\\9\\601861-191015_191015_1_9,000000.tiff" 
cracked_img_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601873_tiff\\601873_2_200603_1_9,0.tiff"    #cracked_img_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\xIbg_Input\\601872_200506_1_9,0.tiff" 
folder_with_img = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601873_tiff\\"    #cracked_img_PATH = "C:\\Users\\io318\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.05.06\\xIbg_Input\\601872_200506_1_9,0.tiff" 
DESTIN_PATH = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601873_D\\"

qD_9,qD_2 = qca(folder_with_img,calibration_img_PATH,DESTIN_PATH,200603)
qD_9.to_csv(DESTIN_PATH+'Degredation at 9A.csv')
qD_2.to_csv(DESTIN_PATH+'Degredation at 2A.csv')


folder_with_data = "C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\200603-for-Jonas\\"   
moduleIDs, lightIV_data, lightIV_parameters = getLIVdata(folder_with_data)

Isc_cal1 = lightIV_parameters['601864']['stc'].iloc[1,1]
Isc_cal2 = lightIV_parameters['601864']['200W'].iloc[1,1]

Isc_var1 = ((Isc_cal1-lightIV_parameters['601873']['stc'].iloc[:,1])/Isc_cal1)*100
Isc_var2 = ((Isc_cal2-lightIV_parameters['601873']['200W'].iloc[:,1])/Isc_cal1)*100

case1 = Isc_var1.index
case2 = [2,3,4,5,6,8]
    
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(case1.astype(int),Isc_var1,label='Decraesa in Isc at 1000W')
ax1.scatter(case2,qD_9.loc[:,'D'],label='Degraded area at 9A')
ax1.scatter(case1.astype(int),Isc_var2,label='Decrease in Isc at 200W')
ax1.scatter(case2,qD_2.loc[:,'D'],label='Degraded area at 1,8A')
ax1.legend();
plt.xlabel('Degree of degredation')
plt.ylabel('%')
tikzplotlib.save("C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601873_D\\601873-c-200603_1_x,x_.D-plot.tex")
plt.savefig("C:\\Users\\jonas\\OneDrive - Norwegian University of Life Sciences\\skole\\Master IFE BIPV\\EL-bilder\\2020.06.03\\601873_D\\601873-c-200603_1_x,x_D-regplot.png")
