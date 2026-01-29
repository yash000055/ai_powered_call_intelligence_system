import librosa
import soundfile as sf
import os

input_path = r"D:\PROJECTS\MINE\AI Powered Call Intelligence System\audio samples\raw calls\sample.wav" 
output_path = r"D:\PROJECTS\MINE\AI Powered Call Intelligence System\audio samples\processed calls\sample_16k.wav"

y, sr = librosa.load(input_path, sr=16000)

os.makedirs(os.path.dirname(output_path), exist_ok=True)

sf.write(output_path, y, 16000)

print("Audio converted to 16kHz and saved ")
