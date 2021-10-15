from gtts import gTTS
import playsound
text_user = "chào mừng bạn đến với chương trình ai là triệu phú,sau đây là câu hỏi đầu tiên"
tts = gTTS(text=text_user, lang='vi', slow=False)
tts.save("audio/start.mp3")
playsound.playsound('audio/start.mp3')