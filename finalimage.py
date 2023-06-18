import math

import matplotlib.pyplot as pl
import numpy as np
from PIL import Image


def rgb_of_pixel(img_path, x, y):
    im = img_path.convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a

I1=[]
I=[]
R=[]
T=[]
theata=[]
Rx=[]
Ix=[]
I1x=[]
Ixx=[]
img = Image.open("testimage.jpg") 


for i in range(512):                                                            
    R.append((i-256)/256)
    a =(rgb_of_pixel(img, i, 256))
    I1.append(((a[0]+a[1]+a[2])/3))
    
k = max(I1)
#print(k)




for i in range(512):
    I.append(I1[i]/k)
    T.append(pow(I[i],0.25))

Ra = 233.5

for i in range(0,256):
    r = Ra-i
    l = r/Ra
    m = np.arcsin(l)
    costh = np.cos(m)
    theata.append(costh)
    
# print(theata)
avgslope = 0.00

for i in range(60,225): 
    avgslope = avgslope + ((I[i]-I[i+1])/(theata[i]-theata[i+1]))/164
    



pl.figure(1)
pl.plot(R,T,color="orange") #plots for Radius vs Temperature
pl.grid()
pl.xlabel("Radius")
pl.ylabel("T/Tmax")
pl.title("Radius vs Temp.")

pl.figure(2)
pl.plot(R,I,color="blue") #plots for Radius vs Intensity
pl.xlabel("Radius")
pl.ylabel("I/Imax")
pl.title("Radius vs Intensity")
pl.grid()


pl.figure(3)
pl.plot(theata[20:256],I[43:279],color="green") #only positive values of theata are taken
#pl.plot((0,1),(1-avgslope,I[279]))
#pl.plot((theata[260],theata[467]),(I[260],I[467])),  #RD
print("the slope is",avgslope),
pl.xlabel("cosθ")
pl.ylabel("I/Imax")

pl.grid()
pl.show()




