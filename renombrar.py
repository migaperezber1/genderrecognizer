#import OpenCV module
import cv2
#import os module for reading training data directories and paths
import os, sys
#import numpy to convert python lists to numpy arrays as 
#it is needed by OpenCV face recognizers
import numpy as np

dirs = os.listdir(".")
l=0
for dirr in dirs:
	print(dirr)
	if dirr[-4:]==".jpg":                  
	    nomb = str(l)+'.jpg'
	    print(nomb)			
	    os.rename (dirr , nomb)
	    l+=1		
	
