
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
import pyautogui as pag
import cv2
import pyscreenshot as ImageGrab
import time

import pickle
import win32gui, win32ui, win32con, win32api
from lib.game_position import get_position,get_screen
from lib.process_image import process_img
from lib.capture_keys import log_keys,get_keys


def train():
    for i in range(1,4):
        print(i ,'seconds')
        time.sleep(1)
    print('training...')
    fps=0
    training_frames=pd.DataFrame()
    training_keys=pd.DataFrame()
    while True:
        t=time.time()
        intsarray,height,width=get_screen(pos,win32gui, win32ui, win32con, win32api)
        img=process_img(intsarray,height,width,np,cv2)
        fps=fps+(time.time()-t)
        key = get_keys(win32api)
        training_frames=training_frames.append(img.tolist())
        training_keys= training_keys.append([key])
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break;
    print('fps: ',fps/len(training_frames),'trained frames: ', len(training_frames))
    training_frames=training_frames[10:len(training_frames)-10]
    training_keys=training_keys[10:len(training_keys)-10]
    training_frames.to_csv('training_frames1.csv')
    training_keys.to_csv('training_keys1.csv')

def drive(clf):
    
    for i in range(1,4):
        print(i ,'seconds')
        time.sleep(1)
    k=cv2.waitKey(1)
    keyboard = Controller()
    while True:
        intsarray,height,width=get_screen(pos,win32gui, win32ui, win32con, win32api)
        img=process_img(intsarray,height,width,np,cv2)
        X=img.tolist()
       # y=clf.predict(X)
        #predict handle the game
        

        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break;
        keyboard.release('w')

inp="train"
t=input("press a key to start if *press space* screen has appeared")

pos=get_position(pag)


print('frames will be captured at',pos)
t=input("press a key if game is car is in terrain and car is movable")
ti=time.time()
if(inp=="train"):
    train()

print('total time taken: 'time.time()-ti)
# In[ ]:




