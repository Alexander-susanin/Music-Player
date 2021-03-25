import pygame
from tkinter import *
import os

root = Tk()
class MusicPlayer:
    def __init__(self, root, vol):
        self.root = root
        self.root.title('MusicPlayer')
        self.root.geometry('1000x200+200+200')
        
        pygame.init()
        pygame.mixer.init()
        
        self.track = StringVar()
        self.status = StringVar()
        self.vol = vol

        #Track Frames for Song label and status label
        trackframe = LabelFrame(self.root, text='Song Track', font=('times new roman',15,'bold'), bg='Steelblue', fg='white', bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)

        #Inserting track label and status label
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=("times new roman",24,"bold"),bg="pink",fg="black").grid(row=0, column=0, pady=5)
        trackstatus = Label(trackframe, textvariable=self.status, font=("times new roman",24,"bold"),bg="pink",fg="black").grid(row=0,column=1,padx=10,pady=5)

        #Button frame
        buttonframe = LabelFrame(self.root, text='Control Panel', font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)

        #Buttons play pause unpause stop
        buttonplay = Button(buttonframe, text='PLAY', command=self.playsong, width=10, height=1, font=("times new roman",16,"bold"),fg="black",bg="pink").grid(row=0,column=0,padx=10,pady=5)
        buttonplay = Button(buttonframe, text='PAUSE', command=self.pausesong, width=8,height=1,font=("times new roman",16,"bold"),fg="black",bg="pink").grid(row=0,column=1,padx=10,pady=5)
        buttonplay = Button(buttonframe, text='UNPAUSE', command=self.unpausesong, width=10,height=1,font=("times new roman",16,"bold"),fg="black",bg="pink").grid(row=0,column=2,padx=10,pady=5)
        buttonplay = Button(buttonframe, text='STOP', command=self.stopsong, width=10,height=1,font=("times new roman",16,"bold"),fg="black",bg="pink").grid(row=0,column=3,padx=10,pady=5)

        #Playlist frame
        songsframe = LabelFrame(self.root, text='Song Playlist', font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        songsframe.place(x=600, y=0, width=400, height=200)
        #Scrollbar
        scroll_y = Scrollbar(songsframe, orient=VERTICAL)
        #Playlist listbox
        self.playlist = Listbox(songsframe, yscrollcommand = scroll_y.set, selectbackground='LightSteelBlue', selectmode=SINGLE, font=("times new roman",12,"bold"),bg="Steelblue",fg="black",bd=5,relief=GROOVE)
        #Apply scrollbar to listbox
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        #Directory for fetching songs
        os.chdir('')#Your file or directory with music
        songtracks = os.listdir()
        for track in songtracks:
            self.playlist.insert(END, track)

    def playsong(self):
        #Song Title
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set('-Playing')
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stopsong(self):
        self.status.set('-Stopped')
        pygame.mixer.music.stop()

    def pausesong(self):
        self.status.set('-Paused')
        pygame.mixer.music.pause()

    def unpausesong(self):
        self.status.set('-Playing')
        pygame.mixer.music.unpause()

MusicPlayer(root, 10)
root.mainloop()