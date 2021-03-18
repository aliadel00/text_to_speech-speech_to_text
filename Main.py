import os

import speech_recognition as sr
from gtts import gTTS

r = sr.Recognizer()  # initializing voice reader package
mic = sr.Microphone()  # initializing microphone reader package
technique = input("Enter reading Method\n1 - audio file\n2 - live audio\n")
if technique == "audio file" or technique == "1":
    choice = input("1 - text to speech\n2 - speech to text\n")


# speech from external file to text converter
def voice_to_text_speech_to_text():
    try:
        path = input("Enter file path:\n")
        voiceFile = sr.AudioFile(path)
        with voiceFile as source:
            audio = r.record(source)
        audioText = r.recognize_google(audio)
        print("Speech converted to Text is:\n" + audioText)

    except FileNotFoundError:
        path = input("ENTER VALID PATH:\n")
        voiceFile = sr.AudioFile(path)
        with voiceFile as source:
            audio = r.record(source)
        audioText = r.recognize_google(audio)
        print("Speech converted to Text is:\n" + audioText + "\n")


# live audio (microphone) to text converter
def voice_to_text_live_audio():
    while technique == "live audio" or technique == "2":
        with mic as source:
            try:
                print("-------------------Start Talking {say BREAK or EXIT to exit}-------------------")
                # r.adjust_for_ambient_noise(source, duration=5)
                r.adjust_for_ambient_noise(source, duration=1)
                r.pause_threshold = 1
                audio = r.listen(source)
                print("listening...")
                audioText = r.recognize_google(audio)
                print("the converted speech to text is:")
                print(audioText)
                if audioText == "exit" or audioText == "break":
                    break
            except LookupError:
                print("couldn't recognize your speech, try again please. But now make your voice audible")


# text to .wav file converter
def text_to_voice():
    converted = "Converted"
    filextension = '.wav'
    convertedfile = converted + filextension
    language = 'en'
    text = input("Enter Text to Convert:\n")
    textToConvert = gTTS(text=text, lang=language, slow=False)
    textToConvert.save(convertedfile)
    print("The output of the above program should be a voice saying, ( " + text + " )")
    os.system(convertedfile)


# function calls
if technique == "live audio" or technique == "2":  # live audio (microphone) identifier
    voice_to_text_live_audio()
elif technique == "audio file" and choice == "speech to text" or technique == "1" and choice == "speech to text" or choice == "2":  # speech from external file identifier
    voice_to_text_speech_to_text()
elif technique == "audio file" and choice == "text to speech" or technique == "1" and choice == "text to speech" or choice == "1":  # text to .wav file identifier
    text_to_voice()
