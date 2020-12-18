from gtts import gTTS
import os
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
technique = input("Enter reading Method (audio file)or(live audio):\n")
if technique == "audio file":
    choice = input("Enter text to speech or speech to text:\n")


def voice_to_text_speech_to_text():
    try:
        path = input("Enter file path:\n")
        voiceFile = sr.AudioFile(path)
        with voiceFile as source:
            audio = r.record(source)
        audioText = r.recognize_google(audio)
        print("Voice converted to Text is:\n" + audioText)

    except FileNotFoundError:
        path = input("ENTER VALID PATH:\n")
        voiceFile = sr.AudioFile(path)
        with voiceFile as source:
            audio = r.record(source)
        audioText = r.recognize_google(audio)
        print("Voice converted to Text is:\n" + audioText + "\n")


def voice_to_text_live_audio():
    while technique == "live audio":
        with mic as source:
            try:
                print("-------------------Start Talking {say BREAK or EXIT to exit}-------------------")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
                print("listening")
                audioText = r.recognize_google(audio)
                print("the text is:")
                print(audioText)
                if audioText == "exit" or audioText == "break":
                    break
            except Exception:
                print("Value error")


def text_to_voice():
    language = 'en'
    text = input("Enter Text to Convert:\n")
    textToConvert = gTTS(text=text, lang=language, slow=False)
    textToConvert.save("test.mp3")
    print("The output of the above program should be a voice saying," + text)
    os.system("test.mp3")


if technique == "audio file" and choice == "speech to text":
    voice_to_text_speech_to_text()
elif technique == "audio file" and choice == "text to speech":
    text_to_voice()
if technique == "live audio":
    voice_to_text_live_audio()
