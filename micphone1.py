from vosk import KaldiRecognizer, Model
import pyaudio


model=Model('/home/neosoft/Documents/Dev/speechtotext/st_vosk_pro/vosk-model-small-en-us-0.15')

recognizer=KaldiRecognizer(model, 16000)

cap=pyaudio.PyAudio()
stream=cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data= stream.read(4096)

    if len(data)==0:
        break

    if recognizer.AcceptWaveform(data):
        print(recognizer.Result())
    

