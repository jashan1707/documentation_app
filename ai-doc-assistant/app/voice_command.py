import speech_recognition as sr

def listen_for_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
    command = recognizer.recognize_google(audio)
    return command.lower()