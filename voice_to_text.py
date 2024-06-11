import speech_recognition as sr

# 创建一个识别器对象
recognizer = sr.Recognizer()

# 从文件中读取音频
audio_file = "1 (1).wav"  # 替换成您的音频文件路径
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# 使用Google Web语音API进行语音识别
try:
    text = recognizer.recognize_google(audio_data, language="zh-CN")  # 可以更改语言
    print("识别结果：", text)
except sr.UnknownValueError:
    print("无法识别音频内容")
except sr.RequestError:
    print("无法连接到Google Web API")
