import video
import time
import dynamixel as dn 
import cv2
import numpy as np

cap=cv2.VideoCapture(1)

r, f = cap.read()

n, m, o = f.shape

vertical, horizontal= np.meshgrid(range(m), range(n))

integral=0
start_time = time.time()
pretvreme=start_time-0.2
vreme = start_time
pretrastojanje=0
Kd=1
Kp=1
Ki=0.1

while True:
    
    rastojanje, thresh = video.snimanje(cap, horizontal, vertical, n, m)
    print(thresh.sum())
    integral=integral+rastojanje*(vreme-pretvreme)
    P=Kd*(rastojanje-pretrastojanje)/(vreme-pretvreme)+ Kp*rastojanje
    pretrastojanje=rastojanje
    ugao= P
    ugao=ugao*5+512
    ugao = int (round(ugao))
    if(thresh.sum() > 10000):
        dn.set_position(ugao)
    else:
        dn.set_position(512)
    pretvreme = vreme 
    vreme = time.time() - start_time
    cv2.imshow('Capturing', thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

