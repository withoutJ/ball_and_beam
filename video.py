import cv2 
import numpy as np


def snimanje(video, horizontal, vertical, n, m):
    t, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if t:
        gray = cv2.medianBlur(gray,5)
    gray = gray > 150
    locy = 1*gray
    locx = 1*gray
    a = locy.sum()
    locy *= horizontal
    locx *= vertical
    if a!=0:
        x = int(locx.sum()/a)
        y = int(locy.sum()/a)
    else:
        x = 0
        y = 0
    gray = 255*gray
    thresh = np.array(gray, dtype = np.uint8)
    thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    for i in range(y-3, y+3):
        for j in range (x-3, x+3):
            if i<n and i>=0 and j<m and j>=0:
                thresh[i][j] = (0, 0 , 255)
    d = np.sqrt((x-320)*(x-320)+(y-255)*(y-255))
    return d, thresh
    #cv2.imshow('Capturing', thresh)
    
    '''if cv2.waitKey(1) & 0xFF == ord('q'):
        break'''

'''video.release()
cv2.destroyAllWindows()'''