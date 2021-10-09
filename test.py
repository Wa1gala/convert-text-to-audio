# class Animal:
#    def __init__(self):
#       self.__init__()

"""
print('Option №2\n')
file_path = input('Введите путь к файлу: ')
changed_file_path = file_path.replace('\\', '/')
print(changed_file_path)
file_name_full = os.path.split(changed_file_path)
print(file_name_full)
file_name_end = file_name_full[1].split('.')
print(file_name_end)

file = codecs.open(file_path, 'r', 'utf-8')
theText = file.read()

tts = gTTS(text=theText, lang='ru')
for tss in file_name_full:
    tts.save(f'{file_name_end[0]}.mp3')
    print('\nFile is saved!')
    break


print('File saved!')


# Test
# path = C:/Users/Алексей/Desktop/17.txt










# Тесты  замены символов

# 2
print('Option №2\n')
file_path = input('Введите путь к файлу: ')
changed_file_path = file_path.replace('\\', '/')
print(changed_file_path)
file_name = os.path.split(changed_file_path)
print(file_name)


# 3
print('Option №3\n')
file_path = input('Введите путь к файлу: ')
multiline_str_split_list = file_path.split('\n')
for s in multiline_str_split_list:
    print(s)

# 1
print('Option №1\n')
file_path = input('Введите путь к файлу: ')
file_name = file_path.split('\n')
print(file_name)
"""

import pyttsx3
from gtts import gTTS
from tqdm import tqdm
from time import sleep
import codecs
import os.path
import re

keys = ['txt', 'rtf', 'doc']

while True:
    file_path = input('Please, enter path to the file: ')

    try:
        changed_file_path = file_path.replace('\\', '/')
        file_name_full = os.path.split(changed_file_path)
        file_name_end = file_name_full[1].split('.')
        file = codecs.open(file_path, 'r', 'utf-8')
        if os.path.exists(file_path) and file_name_end[1] in keys:
            print('Start read!')
            break
        else:
            print('Wrong path!\nPlease, enter again!')
    except:
        print('Error!')
