#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:41:59 2019

@author: jerryyoung
"""

##Imports
import simpleaudio as sa
import time
from datetime import datetime
from tkinter import *


##Definitions and essentials
root = Tk()
root.title('Simple Alarm Clock')
current_time_hour = time.strftime("%I")
current_time_minute = time.strftime("%M")
alarm_sound = sa.WaveObject.from_wave_file('RadarSound.wav')
alarm_hour = None
alarm_minute = None

##Functions
def submit_time():
	global alarm_hour
	global alarm_minute
	alarm_hour = entry_hour.get()
	alarm_minute = entry_minute.get()
	user_alarm_label = Label(root, text = f"Alarm: {alarm_hour}:{alarm_minute}")
	user_alarm_label.grid(row = 4, column = 0, columnspan = 3)

def play_sound():
	play_alarm_times = [0, 100]
	for s in play_alarm_times:
		play_alarm = alarm_sound.play()
		play_alarm.wait_done()

def main_loop():
	global current_time_hour
	global current_time_minute
	current_time_hour = time.strftime("%I")
	current_time_minute = time.strftime("%M")
	if (alarm_hour != current_time_hour) and (alarm_minute != current_time_minute):
		current_time_hour = time.strftime("%I")
		current_time_minute = time.strftime("%M")
	elif (alarm_hour == current_time_hour) and (alarm_minute == current_time_minute):
		play_sound()
	root.after(1000, main_loop)

##Labels & Entries
alarm_label = Label(root, text = 'Enter alarm time in this format 00:00')
entry_hour = Entry(root, width = 5, borderwidth = 3)
colon = Label(root, text = ':')
entry_minute = Entry(root, width = 5, borderwidth = 3)
accept_time = Button(root, text = 'Submit Time', command = submit_time)
wake_up_label = Label(root, text = '_____________')

##Packs
alarm_label.grid(row = 0, column = 0, columnspan = 3)
entry_hour.grid(row = 1, column = 0)
colon.grid(row = 1, column = 1)
entry_minute.grid(row = 1, column = 2)
accept_time.grid(row = 2, column = 0, columnspan = 3)
wake_up_label.grid(row = 3, column = 0, columnspan = 3)

root.after(1000, main_loop)
root.mainloop()
    