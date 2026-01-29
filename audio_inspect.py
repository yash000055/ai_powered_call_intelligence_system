import librosa

audio_path = r"D:\PROJECTS\MINE\AI Powered Call Intelligence System\audio samples\raw calls\sample.wav"  
y, sr = librosa.load(audio_path, sr=None)

print("Audio Loaded Successfully ")
print("Sample Rate:", sr)
print("Total Samples:", len(y))
print("Duration (seconds):", len(y) / sr)
