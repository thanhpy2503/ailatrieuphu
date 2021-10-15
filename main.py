import speech_recognition as sr
from playsound import playsound
def speech_user():
        r = sr.Recognizer()
        with sr.Microphone() as mic:
            print("bot đang nghe")
            audio = r.record(mic, duration=5)
        try:
            input_player = r.recognize_google(audio, language='vi-VN')
            return input_player
        except:
            print("tôi chưa nghe rõ câu trả lời của bạn")
def main():
    playsound('audio/start.mp3')
    input_user = speech_user()
    print(input_user)


if __name__ == '__main__':
    main()


