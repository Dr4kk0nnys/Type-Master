from time import sleep
from subprocess import Popen
from os import remove

from PIL import Image

import pyautogui

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'


def get_image():
    # remove('C:\\Users\\Dr4kk0nnys\\Documents\\Lightshot\\Screenshot_1.png')

    pyautogui.hotkey('alt', 'tab')
    sleep(.25)
    
    pyautogui.press('printscreen')
    
    pyautogui.moveTo(170, 560)

    sleep(3)


def get_text():
    return pytesseract.image_to_string(Image.open('C:\\Users\\Dr4kk0nnys\\Documents\\Lightshot\\Screenshot_1.png')).replace('|', 'I')


get_image()

sleep(1.5)

text = get_text()
print(f'Text is: {text}')

text = text.replace('\n', ' ').split(' ')
for i in range(len(text)):
    pyautogui.typewrite(text[i] + ' ')
