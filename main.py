from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('mp3 player')
root.geometry('500x350')

pygame.mixer.init()


def play():
    song = songs_list.get(ACTIVE)
    song = f'/home/dci-student/all/ON_GITHUB/GUI-mp3-player/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()

global pause_status
pause_status = False

def pause(is_paused):
    global pause_status
    pause_status = is_paused

    if pause_status:
        pygame.mixer.music.unpause()
        pause_status = False
    else:
        pygame.mixer.music.pause()
        pause_status = True


def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title='Add Song', filetypes=(('mp3 Files', '*.mp3'), ))
    song = song.replace('/home/dci-student/all/ON_GITHUB/GUI-mp3-player/audio/', '')
    song = song.replace('.mp3', '')

    songs_list.insert(END, song)


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title='Add Many Songs', filetypes=(('mp3 Files', '*.mp3'), ))

    for song in songs:
        song = song.replace('/home/dci-student/all/ON_GITHUB/GUI-mp3-player/audio/', '')
        song = song.replace('.mp3', '')

        songs_list.insert(END, song)


def next():
    next_song = songs_list.curselection()
    next_song = next_song[0]+1

    song = songs_list.get(next_song)
    song = f'/home/dci-student/all/ON_GITHUB/GUI-mp3-player/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

    songs_list.selection_clear(0, 'end')
    songs_list.activate(next_song)
    songs_list.selection_set(next_song, last=None)


def back():
    next_song = songs_list.curselection()
    next_song = next_song[0]-1

    song = songs_list.get(next_song)
    song = f'/home/dci-student/all/ON_GITHUB/GUI-mp3-player/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

    songs_list.selection_clear(0, 'end')
    songs_list.activate(next_song)
    songs_list.selection_set(next_song, last=None)


def delete_song():
    songs_list.delete(ANCHOR)
    pygame.mixer.music.stop()


def delete_all_songs():
    songs_list.delete(0, 'end')
    pygame.mixer.music.stop()


songs_list = Listbox(root, bg='black', fg='white', width=60)
songs_list.pack(pady=15)

frame = Frame(root)
frame.pack(pady=10)

play_btn_img = PhotoImage(file='images/play.png')
stop_btn_img = PhotoImage(file='images/stop.png')
pause_btn_img = PhotoImage(file='images/pause.png')
next_btn_img = PhotoImage(file='images/next.png')
back_btn_img = PhotoImage(file='images/back.png')

play_button = Button(frame, image=play_btn_img, borderwidth=0, command=play)
stop_button = Button(frame, image=stop_btn_img, borderwidth=0, command=stop)
pause_button = Button(frame, image=pause_btn_img, borderwidth=0, command= lambda: pause(pause_status))
next_button = Button(frame, image=next_btn_img, borderwidth=0, command=next)
back_button = Button(frame, image=back_btn_img, borderwidth=0, command=back)

play_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=1, padx=10)
pause_button.grid(row=0, column=3, padx=10)
next_button.grid(row=0, column=4, padx=10)
back_button.grid(row=0, column=0, padx=10)

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Add Song', command=add_song)
file_menu.add_command(label='Add Many Songs', command=add_many_songs)

delete_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Delete', menu=delete_menu)
delete_menu.add_command(label='Delete Current Song', command=delete_song)
delete_menu.add_command(label='Delete All Songs', command=delete_all_songs)

root.mainloop()