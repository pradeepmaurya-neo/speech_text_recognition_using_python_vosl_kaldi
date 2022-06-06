from vosk import KaldiRecognizer, Model
import wave
import json

audio=wave.open('test1.wav', 'rb')
if audio.getnchannels() != 1 or audio.getsampwidth() != 2 or audio.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model=Model('/home/neosoft/Documents/Dev/speechtotext/st_vosk_pro/vosk-model-small-en-us-0.15')

rec = KaldiRecognizer(model, audio.getframerate())
rec.SetMaxAlternatives(10)
rec.SetWords(True)





while True:
    data= audio.readframes(4000)

    if len(data)==0:
        break

    if rec.AcceptWaveform(data):
        print(json.loads(rec.PartialResult()))
    
        