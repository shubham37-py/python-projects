import pygame
import os
import time


os.system("code ")
pygame.mixer.init()

audio_path = r"C:\Users\user\Downloads\jarvis-147563.mp3"

if os.path.exists(audio_path):
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0)
else:
    print("file not found")    

