from tkinter import *
import pygame

root = Tk()
root.title('mp3 player')
root.geometry('500x400')

pygame.mixer.init()


def play():
    pygame.mixer.music.load('audio/Digital Warrior.mp3')
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()


play_btn = Button(root, text='Play', font=('Times New Roman', 32), command=play)
play_btn.pack(pady=20)

play_btn = Button(root, text='Stop', font=('Times New Roman', 32), command=stop)
play_btn.pack(pady=20)



root.mainloop()