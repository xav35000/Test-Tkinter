from io import BytesIO
import pygame
import tkinter as tk
from gtts import gTTS
pygame.init()
pygame.mixer.init()
def speak(text, language='en'):
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    x = pygame.mixer.music.load(mp3_fo, 'mp3')
    pygame.mixer.music.play()


root = tk.Tk()
tx = tk.Text(root)
tx.pack()
bt = tk.Button(root, text="PLAY",
    command=lambda: speak(tx.get('0.0', tk.END)))
bt.pack()
root.mainloop()