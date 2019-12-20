import simpleaudio as sa
from tkinter import *
from PIL import ImageTk, Image
import random

song1 = sa.WaveObject.from_wave_file('Hephaestus.wav')

song2 = sa.WaveObject.from_wave_file('iBlossom.wav')

song_list = [song1, song2]
song1_info = {"Hephaestus": ["I Am Human", "2018"]}
song2_info = {"iBlossom": ["I Am Human", "2018"]}
random_selection = 0
play_song = 0
playlist = []

def play_button():
	global random_selection
	global play_song
	random_selection = random.choice(song_list)
	playlist.append(random_selection)
	if random_selection == song1:
		song_name.configure(text = "Hephaestus")
		song_artist_year.configure(text = "I Am Human, 2018")
		play_song = song1.play()
	elif random_selection == song2:
		song_name.configure(text = "iBlossom")
		song_artist_year.configure(text = "I Am Human, 2018")
		play_song = song2.play()
	play_button.configure(text = 'Pause', command = pause_button)

def pause_button():
	global play_song
	play_song.stop()
	play_song = 0
	play_button.configure(text = 'Play', command = play_button)

def back_button():
	pass

def forward_button():
	pass

root = Tk()
root.title('REJECT$ MP3')

song_img = Image.open('TheFrontier.jpg')
song_img = song_img.resize((150, 150), Image.ANTIALIAS)
song_img = ImageTk.PhotoImage(song_img)
album_label = Label(image = song_img)

song_name = Label(root, text = 'No song is playing')
song_artist_year = Label(root, text = '')

play_button = Button(root, text = 'Play', command = play_button)
back_button = Button(root, text = 'Back', command = back_button)
forward_button = Button(root, text = 'Forward', command = forward_button)

album_label.grid(row = 0, column = 1, columnspan = 1)
song_name.grid(row = 1, column = 1)
song_artist_year.grid(row = 2, column =1)
play_button.grid(row = 3, column = 1)
back_button.grid(row = 3, column = 0)
forward_button.grid(row = 3, column = 2)

root.mainloop()
