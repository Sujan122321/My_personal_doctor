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
# input_text = "Hello, this is a test of the gTTS text to speech conversion. From sujan Shrestha"
# output_filepath = "output_gtts.mp3"
# # text_to_speech_gtts(input_text=input_text, output_filepath=output_filepath)


# step 1 B: Setup Text to Speech (TTS) model with Elevenlabs
 
import os
from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

def text_to_speech_elevenlabs(input_text, output_filepath, voice_id="9BWtsMINqrJLrRacOk9x"):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id=voice_id,
        output_format="mp3_22050_32",
        model_id="eleven_turbo_v2_5"
    )
    
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)

# Test
input_text = "Hello, this is a test of the Elevenlabs text to speech conversion. From Sujan Shrestha"
output_filepath = "output_elevenlabs.mp3"
text_to_speech_elevenlabs(input_text, output_filepath)