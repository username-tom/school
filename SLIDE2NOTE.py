# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 12:26:38 2020

SLIDE2NOTE
Version: 0.0.0

@author: tomwu
"""

import pyautogui as pyauto
import cv2
import pytesseract as pyta
import pyperclip
pyta.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pyauto.PAUSE = 3
section_loc = pyauto.position()
next_loc = pyauto.position()
down_loc = pyauto.position()
print_loc = pyauto.position()
img = cv2.imread('test1.png')
logo_ref = cv2.imread('logo_ref.png')
logo_ref_bl = cv2.imread('logo_ref_btm_left.png')

text = pyta.image_to_string(img)

logo_center = pyauto.locateCenterOnScreen(logo_ref_bl, confidence=0.9)
pyauto.moveTo(logo_center)
pyauto.scroll(-150)
while True:
    while True:
        loc_bl = pyauto.locateOnScreen(logo_ref_bl, confidence=0.8)
        btm_left = [loc_bl[0], loc_bl[1]]
        top_right = [loc_bl[0] + 1500, loc_bl[1] - 1000]
        if (btm_left[1] > 1100):
            break
        else:
            pyauto.scroll(-30)
    pyauto.screenshot('1.png', (btm_left[0], top_right[1], top_right[0] - btm_left[0], btm_left[1] - top_right[1]))
    img = cv2.imread('1.png')
    text = pyta.image_to_string(img)
    text = text.replace('\n\n', '\n')
    text = text.replace('\n\n', '\n')
    text = text.replace('\n\n', '\n')
    text = text.replace('\n\n', '\n')
    text = text.replace('\n\n', '\n')
    
    
    pyauto.click(2200, 400, 2)
    pyperclip.copy(text)
    pyauto.hotkey('ctrl', 'v')
    pyauto.scroll(-420)
    if (loc_bl == -1):
        break
    
i = 1
while True:
    pyauto.click(down_loc[0], down_loc[1])
    pyauto.click(print_loc[0], print_loc[1])
    pyauto.hotkey('enter')
    pyauto.moveTo(section_loc[0], section_loc[1])
    pyauto.click()
    pyauto.hotkey('enter')
    pyauto.moveTo(next_loc[0], next_loc[1])
    pyauto.click(next_loc[0], next_loc[1])
    pyauto.moveRel(60, 0, 1)
    pyauto.scroll(-1500)
    i=i+1
    if (i>7):
        break
    
page_loc = pyauto.position()
center_loc = pyauto.position()

while True:
    pyauto.click(center_loc[0], center_loc[1], button='right')
    pyauto.moveRel(60, 130, .5)
    pyauto.click()
    pyauto.moveRel(800, -500, .5)
    pyauto.click(clicks=2)
    pyauto.hotkey('ctrl', 'v')
    i=i+1
    pyauto.scroll(-590)
    if (i>9):
        break
    
tl_loc = pyauto.position()
br_loc = pyauto.position()