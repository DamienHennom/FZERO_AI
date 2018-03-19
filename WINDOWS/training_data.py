# create_training_data.py

import numpy as np
from grabscreen import grab_screen,screen_record2
import cv2
import time
from getkeys import key_check,keys_to_output
import os

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []


def main(region):

    #Countdown
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    
    while(True):

        if not paused:
            # 800x600 windowed mode
            img = grab_screen(region)
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            img = cv2.resize(img,(102,88))
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([img,output])
                    
            if len(training_data) % 500 == 0:
                print(len(training_data))
                np.save(file_name,training_data)

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)



if __name__ == "__main__":
    main(region=(0,0,510,440))

