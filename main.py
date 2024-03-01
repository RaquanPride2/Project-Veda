from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# speech engine 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 = male #1 = female
activationWord = 'computer' # single word

def parseCommand():
  listener = sr.Recognizer()
  print('Waiting for request')


  with sr.Microphone() as source:
      listener.pause_threshold = 2
      input_speech = listener.listen(source)

  try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query}')
  except Exception as exceptio:
        print('I did not catch that')   
        
          