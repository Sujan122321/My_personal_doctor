# Step 1: Setup Text to Speech (TTS) model (gTTs & Elevenlabs)

# Step 1 A: Setup Text to Speech (TTS) model with gTTs
import os
from gtts import gTTS

def text_to_speech_gtts(input_text, output_filepath):
    """
    Convert text to speech using gTTS and save it as an MP3 file.
    
    Args:
        input_text (str): The text to convert to speech.
        output_filepath (str): The path where the MP3 file will be saved.
    """
    language = 'en'
    
    audio_object= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audio_object.save(output_filepath)
    
# test
input_text = "Hello, this is a test of the gTTS text to speech conversion. From sujan Shrestha"
output_filepath = "output_gtts.mp3"
text_to_speech_gtts(input_text=input_text, output_filepath=output_filepath)

# step 1 B: Setup Text to Speech (TTS) model with Elevenlabs
