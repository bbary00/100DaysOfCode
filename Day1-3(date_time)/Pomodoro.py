from datetime import datetime
from datetime import date
from datetime import timedelta
import time
import pygame as pg
import sys
import os


clear = lambda: os.system('clear')


class User:

    def __init__(self):

        custom = os.path.isfile("custom.txt")
        if custom:
            with open("custom.txt", "r") as file:
                settings = [int(el) for el in file.readline().split()]
        else:
            with open("default.txt", "r") as file:
                settings = [int(el) for el in file.readline().split()]
        self.work = settings[0]
        self.relax = settings[1]
        self.chill = settings[2]
        self.rounds = settings[3]

    def custom_setup(self):

        read = input("Enter your settings with spaces 'w r c p': ")
        settings = [int(el) for el in read.split()]
        self.work = settings[0]
        self.relax = settings[1]
        self.chill = settings[2]
        self.rounds = settings[3]
        with open("custom.txt", "w") as file:
            file.writelines(read)

    def info(self):
        print("Working time: {0}\nSmall break: {1}"
              "\nLong break: {2}\nPomodoros: {3}".format(self.work,
                                                         self.relax,
                                                         self.chill,
                                                         self.rounds))

    def get_data(self):
        return [self.work, self.relax, self.chill, self.rounds]


def play_music(music_file, volume=0.8):
    # set up the mixer
    freq = 44100     # audio CD quality
    bit_size = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bit_size, channels, buffer)
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
    except Exception:
        return 0
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(1000)


def load_user():
    user = User()
    user.info()
    ch = input("Leave this settings or make new? [L/N]: ").lower()
    if ch == 'l':
        return user
    elif ch == 'n':
        user.custom_setup()
        return user
    else:
        clear()
        print("Make correct choice!")
        load_user()


def chop(delta):
    return delta - timedelta(microseconds=delta.microseconds)


def pomodoro(user):
    work, relax, chill = [timedelta(minutes=el) for el in user.get_data()[:-1]]
    rounds = user.get_data()[-1]
    sets = 0
    try:
        for i in range(rounds):
            while sets != 4:
                play_music("start.mp3")
                pomo = datetime.today() + work
                while datetime.today().time() < pomo.time():
                    clear()
                    now = datetime.now()
                    print("Working {}\n".format(chop(pomo - now)))
                    print(now.strftime("%H:%M:%S"), end="", flush=True)
                    print("\r", end="", flush=True),
                    time.sleep(1)
                play_music("break.mp3")
                clear()
                sets += 1
                if sets == 3:
                    brake = datetime.today() + chill
                else:
                    brake = datetime.today() + relax
                while datetime.today().time() < brake.time():
                    clear()
                    now = datetime.now()
                    print("RELAX {}\n".format(chop(brake - now)))
                    print(now.strftime("%H:%M:%S"), end="", flush=True)
                    print("\r", end="", flush=True)
                    time.sleep(1)
    except KeyboardInterrupt:
        return 0


if __name__=='__main__':
    clear()
    us = load_user()
    clear
    pomodoro(us)
