import speech_recognition as sr
from gtts import gTTS
import os

voice = ""
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio,language='pt-BR')

            print(text)
            
            if 'quem é você' in text.lower():
                print("Quem sou eu? Eu ainda não aprendi")
            elif 'quem sou eu' in text:
                print("Você é o Davi")
            elif text == "encerrar":
                break
                
            text = r.recognize_google(audio,language='pt-BR')
            voice = voice + str(text)
        except:
            print("Não entendi, pode repetir?")

