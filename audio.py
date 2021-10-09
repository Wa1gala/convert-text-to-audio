import pyttsx3

tss = pyttsx3.init()

voices = tss.getProperty('voices')
tss.setProperty('voice', 'ru')

for voice in voices:
    if voice.name == 'Irina':
        tss.setProperty('voice', voice.id)

tss.say(
    'Привет, меня завут Ирина!'
        )

tss.runAndWait()
