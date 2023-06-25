import speech_recognition as sr

def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something ... !")
        while True:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(text, end=' ')  
            except Exception as e:
                print(e)

get()
