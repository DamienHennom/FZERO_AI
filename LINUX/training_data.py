# create_training_data.py

import numpy as np
from grabscreen import grab_screen,screen_record2
import cv2
import time
from getkey import getkey, keys
import os
import keyboard

def keys_to_output():
    '''
    Convert keys to a ...multi-hot... array
    [A,W,D] boolean values.
    '''
    output = [0,0,0]
    
    if keyboard.is_pressed('q'):
        output[0] = 1
    elif keyboard.is_pressed('d'):
        output[2] = 1
    else:
        output[1] = 1
    return output


file_name = '/home/hennom/Desktop/FZERO/CREATE_DATA/training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []


def main(region):

    #Countdown
    for i in list(range(5))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    
    while(True):

        if not paused:
            # 800x600 windowed mode
            img = grab_screen(region)
            if img==[]:
                print('Error')
            else:
                print('loop took {} seconds'.format(time.time()-last_time))
                last_time = time.time()
                img = cv2.resize(img, (160,120))
                output = keys_to_output()
                training_data.append([img,output])
                    
                if len(training_data) % 100 == 0:
                    print(len(training_data))
                    np.save(file_name,training_data)

        if keyboard.is_pressed('t'):
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
time.sleep(1)


main(region=(70,70,570,480))
#screen_record2(region=(70,70,570,480))
