import pyttsx3
from gtts import gTTS
from tqdm import tqdm
from time import sleep
import codecs
import os.path

# Инициализация библиотеки
engine = pyttsx3.init()

# Голоса и установка голоса
voices = engine.getProperty('voices')
engine.setProperty('voice', 'ru')

# Скорость озвучки файла
rate = engine.getProperty('rate')
engine.setProperty('rate', 250)

# Исключения для try - expect
# https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
# keys = ['txt', 'rtf', 'doc']

# Ввод пути к файлу который надо озвучить
while True:
    keys = ['txt', 'rtf', 'doc']
    file_path = input('Please, enter path to the file: ')

    try:
        # Заменяет \ на /
        changed_file_path = file_path.replace('\\', '/')
        # Разделение пути файла в два кортежа на "хвост" и "голову"
        # Пример: ('C:/Users/Алексей/Desktop', 'test.txt')
        # Для того чтобы давать название файлу, когда идет его сохранение в mp3
        file_name_full = os.path.split(changed_file_path)
        # Берем "хвост" кортежа file_name_full и разбиваем его на список
        # Пример: ['test', 'txt']
        file_name_end = file_name_full[1].split('.')
        # Для нормального воспроизведения файл, вдруг у тебя кодировка хуйня
        file = codecs.open(file_path, 'r', 'utf-8')
        # Проверка на существование файла и есть ли в списке второй элемент
        # Пример того, что пройдет проверку: ['test', 'txt']
        # Пример того, что не пройдет проверку: ['test']
        if os.path.exists(file_path) and file_name_end[1] in keys:
            break
        else:
            print('Wrong path!\nPlease, enter again!')
    except FileNotFoundError:
        print('Wrong path!\nPlease, enter again!')
    except PermissionError:
        print('Wrong path!\nPlease, enter again!')
    except OSError:
        print('Wrong path!\nPlease, enter again!')
    except IndexError:
        print('Wrong path!\nPlease, enter again!')

# Читает текст с файла
theText = file.read()

# Этот цикл нужен для установки другого голоса озвучки
for voice in voices:
    # Тут установлен голос "Александр", как найти новые синтезаторы речи
    # Смотри тут https://github.com/RHVoice/RHVoice/blob/master/doc/en/Binaries.md <--- сюда тыкать колёсиком мышки
    # Тебе нужен пункт SAPI 5, там будут Русские голоса
    if voice.name == 'Aleksandr-hq':
        engine.setProperty('voice', voice.id)
        print('\nFile is being played!\n')
        engine.say(theText)
        engine.runAndWait()

file.close()

print('File has started saving!\n')

# Прогресс бар, просто косметика
for i in tqdm(range(100)):
    sleep(0.01)

# Сохранение файла в аудио формате, в папку, где у тебя находиться этот py файл
tts = gTTS(text=theText, lang='ru')

for tss in file_name_end:
    tts.save(f'{file_name_end[0]}.mp3')
    print('\nFile is saved!')
    break
# tts.save('filename.mp3')


"""
# Фигня которая не робит, но нужно сделать 


# Сделать нормальное сохранение и воспроизведение файла, а то только utf-8, 
# а в этой кодирове воспроизведенный файл нормально не сохраняеться, т.е не может прочитать некоторые символы 


"""
