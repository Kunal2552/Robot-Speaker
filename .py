import os
#import numpy as np
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

while True:
    x = input("say something: ")
    if x == "bubye":
        os.system("tata")
        break
    else:
        speak.Speak(x)
