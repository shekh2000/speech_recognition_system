import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("speak something")
    audio_data = r.listen(source)
    try:
        # Convert speech to text using Google's Speech Recognition
        myText = r.recognize_google(audio_data)
        myText = myText.lower()
        print(f"You said: {myText}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from the service.")