#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:41:59 2019

@author: jerryyoung
"""
from playsound import playsound
import time

print("What time do you want to wake up? Use this form. \nExample: 06:30 ")
alarm_time = input()

current_time = time.strftime("%H:%M")

while current_time != alarm_time:
    current_time = time.strftime("%H:%M")
    loading_time = time.strftime("%H:%M:%S")
    time.sleep(1)
    print(loading_time)
    while current_time == alarm_time:
        print("Wake up! The time is {}".format(time.strftime("%H:%M")))
        play_alarm = [0,100]
        for s in play_alarm:
            alarm_sound = playsound('/Users/jerryyoung/Desktop/Programs/AlarmClock/RadarSound.mp3')
        
    
    