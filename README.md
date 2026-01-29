# Audio to Text Sentiment Analysis Dashboard

## Description :
This project implements an end-to-end audio analytics pipeline that converts audio calls into text, performs sentiment and keyword analysis on the transcribed content, and visualizes the insights through an interactive dashboard. The system demonstrates how audio processing, speech recognition, natural language processing, and data visualization can be combined to build an AI-powered call intelligence solution.

## Project Pipeline :
The project follows a clear multi-stage workflow:

1. Audio inspection and validation  
2. Audio preprocessing (resampling to 16kHz)  
3. Speech-to-text transcription  
4. Text-based sentiment and keyword analysis  
5. Visualization of insights using a dashboard  

Each stage is handled by a dedicated Python script.

## File Description :

### `audio_inspect.py`
- Loads the raw audio file.
- Displays sample rate, total samples, and audio duration.
- Helps validate audio quality before processing.

### `audio_preprocess.py`
- Converts raw audio to a 16kHz sample rate.
- Saves the processed audio in a separate directory.
- Ensures compatibility with speech-to-text models.

### `transcribe.py`
- Uses the Whisper speech recognition model.
- Converts processed audio into text.
- Saves:
  - Full transcription
  - Timestamped text segments  
- Output is stored in `transcript.json`.

### `text_analysis.py`
- Performs sentiment analysis using VADER.
- Extracts key topics using YAKE keyword extraction.
- Generates a short summary from the transcript.
- Saves insights such as sentiment, score, keywords, and summary in `analysis.json`.

### `dashboard.py`
- Builds an interactive dashboard using Streamlit.
- Displays:
  - Overall sentiment
  - Sentiment score
  - Key topics
  - Call summary
  - Timestamped transcript  
- Provides a clear visual representation of call insights.

## Technologies Used :
- Python
- Librosa
- SoundFile
- OpenAI Whisper
- NLTK
- VADER Sentiment Analyzer
- YAKE
- Streamlit
- JSON

## How to Run the Project

1. Install required dependencies:
pip install librosa soundfile openai-whisper nltk vaderSentiment yake streamlit

2. Inspect the raw audio:
python audio_inspect.py

3. Preprocess the audio:
python audio_preprocess.py

4. Transcribe audio to text:
python transcribe.py

5. Analyze the transcribed text:
python text_analysis.py

6. Launch the dashboard:
streamlit run dashboard.py

## Output Files :
- `transcript.json` – Full transcript and timestamped segments
- `analysis.json` – Sentiment, sentiment score, key topics, and summary

## Use Cases :
- Call center analytics
- Customer feedback analysis
- Speech-based sentiment analysis
- AI-powered call intelligence systems
- Learning end-to-end audio and NLP pipelines
