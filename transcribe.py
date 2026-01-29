import whisper
import json

AUDIO_PATH = r"D:\PROJECTS\MINE\AI Powered Call Intelligence System\audio samples\processed calls\sample_16k.wav"

model = whisper.load_model("base")
result = model.transcribe(AUDIO_PATH, verbose=False)

# Save full transcript
full_text = result["text"]

# Save segments
segments = [
    {
        "start": round(seg["start"], 2),
        "end": round(seg["end"], 2),
        "text": seg["text"]
    }
    for seg in result["segments"]
]

output = {
    "full_text": full_text,
    "segments": segments
}

with open("transcript.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4)

print(" Transcript saved as transcript.json")
