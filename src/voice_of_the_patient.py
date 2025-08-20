# Step 1: Setup Audio recorder ((ffmpeg and portaudio))

import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ✅ Tell Pydub exactly where ffmpeg is
AudioSegment.converter = r"C:\ffmpeg\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe"


def record_audio(file_path,timeout=20, pharse_time_limit = None):
    """
    Simplified  function recording audio from the microphone and saving it as an Mp3 file.
    
    Args:
        file_path (str): The path where the recorded audio will be saved.
        timeout (int): Maximum time to wait for the user to start speaking (in seconds).
        pharse_time_limit (int, optional): Maximum time for a single phrase to be recorded. Defaults to None.
    """
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            logging.info("🎤Adjust for ambient noise.....")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("🎤 Please start speaking...")
            
            # Record the audio
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=pharse_time_limit)
            logging.info("🎤 Recording complete.")
            
            #convert the recorded audio to and Mp3 file
            wav_data = audio.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate='128k')
            
            logging.info(f"✅ Audio saved to {file_path}")
            
    except Exception as e:
        logging.error(f"❌ An error occurred while recording audio: {e}")
        
audio_filepath = "patient_audio.mp3"
record_audio(file_path=audio_filepath)


# Step 2 : Setup speech to text_STT_model for transcription

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # looks for .env file in project root
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)
stt_model = "whisper-large-v3"
audio_file = open(audio_filepath, "rb")
transcription = client.audio.transcriptions.create(
    model=stt_model,
    file=audio_file,
    language="en"
)

print("📝 Transcription:", transcription.text)
