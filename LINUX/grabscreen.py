import numpy as np
import pyscreenshot as ImageGrab
import cv2
import time

def screen_record(region): 
    last_time = time.time()
    while(True):
        img = np.array(ImageGrab.grab(bbox=region))
        if img.shape==(410, 500, 3):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            cv2.imshow('window',img)
        else:
            print('Error frame')
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def grab_screen(region): 
    img = np.array(ImageGrab.grab(bbox=region))
    if img.shape==(410, 500, 3):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        img=[]
    return img


def screen_record2(region): 
    last_time = time.time()
    while(True):
        img = grab_screen(region)
        if img==[]:
            print('Error')
        else:
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            cv2.imshow('window',img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
