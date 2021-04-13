import speech_recognition
import pyttsx3
import webbrowser
import datetime
import wikipedia
import pyjokes
import kivy
import urllib.request
import re
kivy.require('2.0.0')

from kivymd.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

listener = speech_recognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with speech_recognition.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language = 'hr-HR')
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    run_jarvis(command)

def run_jarvis(command):
    if 'play' in command:
        song = command.replace('play ', '')
        talk('Playing')
        bok = (song[1:]) + bok.replace(' ', '_')
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + bok)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
    elif 'sati' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'tko si ti' in command:
        talk('I am JARVIS AI bot made by Jandra')
    elif 'kako se zovem' in command:
        talk('You should already know that')
    else:
        talk('Please say the command again.')

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.submit = Button(text="JARVIS", pos =(360, 270), size =(100, 100), background_color =(1, 52, 152, 219), color =(0, 0, 0, 1), font_size =(25))
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        take_command()

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()

'while True:'
'run_jarvis()'







