from vosk import Model, KaldiRecognizer
import wave
import json


wf = wave.open('test5.wav', "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model('/home/neosoft/Documents/Dev/speechtotext/st_vosk_pro/vosk-model-small-en-us-0.15')
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetMaxAlternatives(10)
rec.SetWords(True)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(json.loads(rec.Result()))
        # pass
    else:
        print(json.loads(rec.PartialResult()))
    print(json.loads(rec.PartialResult()))

# print(json.loads(rec.FinalResult()))