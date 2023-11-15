import subprocess
import time
import pyautogui
from pynput.keyboard import Controller
import winsound
def coding_mode():
    winsound.PlaySound('playInBG.wav', winsound.SND_FILENAME)
    def open_spotify():
        subprocess.run(["spotify"])
    def open_chrome():
        subprocess.run(["C:\Program Files\Google\Chrome\Application\chrome.exe"])  
    pyautogui.hotkey("win","ctrl", "d")
    open_spotify()
    time.sleep(2)  
    pyautogui.hotkey("win","ctrl", "d")
    time.sleep(1)
    open_chrome()
coding_mode()


