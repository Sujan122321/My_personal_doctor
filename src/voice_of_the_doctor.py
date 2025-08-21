# Step 1: Setup Text to Speech (TTS) model (gTTs & Elevenlabs)

# this is the simple text to speech converison using gTTS and Elevenlabs.

# Step 1 A: Setup Text to Speech (TTS) model with gTTs
# import os
# from gtts import gTTS

# def text_to_speech_gtts_old(input_text, output_filepath):
#     """
#     Convert text to speech using gTTS and save it as an MP3 file.
    
#     Args:
#         input_text (str): The text to convert to speech.
#         output_filepath (str): The path where the MP3 file will be saved.
#     """
#     language = 'en'
    
#     audio_object= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audio_object.save(output_filepath)
    
# # test
# # input_text = "Hello, this is a test of the gTTS text to speech conversion. From sujan Shrestha"
# # output_filepath = "output_gtts.mp3"
# # # text_to_speech_gtts_old(input_text=input_text, output_filepath=output_filepath)


# # step 1 B: Setup Text to Speech (TTS) model with Elevenlabs
 
# import os
# from elevenlabs import ElevenLabs
# from dotenv import load_dotenv

# load_dotenv()
# ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# def text_to_speech_elevenlabs_old(input_text, output_filepath, voice_id="9BWtsMINqrJLrRacOk9x"):
#     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
#     audio = client.text_to_speech.convert(
#         text=input_text,
#         voice_id=voice_id,
#         output_format="mp3_22050_32",
#         model_id="eleven_turbo_v2_5"
#     )
    
#     with open(output_filepath, "wb") as f:
#         for chunk in audio:
#             f.write(chunk)

# # Test
# # input_text = "Hello, this is a test of the Elevenlabs text to speech conversion. From Sujan Shrestha"
# # output_filepath = "output_elevenlabs.mp3"
# # text_to_speech_elevenlabs_old(input_text, output_filepath)










# step 2: Use Model for Text output to voice 
"""
Here we have to auto play the saved audio file without clicking on it.
This can be done using different methods depending on the operating system.
"""
import os
from gtts import gTTS
import subprocess
import platform
from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# ✅ Tell Pydub exactly where ffmpeg is
# AudioSegment_location = r"C:\ffmpeg\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe"  

def text_to_speech_gtts(input_text, output_filepath):
    """
    Convert text to speech using gTTS and save it as an MP3 file.
    
    Args:
        input_text (str): The text to convert to speech.
        output_filepath (str): The path where the MP3 file will be saved.
    """
    language = 'en'
    
    audio_object = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audio_object.save(output_filepath)
    
    # auto play the saved audio file    
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(
                [r"C:\ffmpeg\ffmpeg-7.1.1-full_build\bin\ffplay.exe", "-nodisp", "-autoexit", output_filepath],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT
            )
        elif os_name == "Linux":  # Linux
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath],
                           stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# test
# input_text = "Hello, this is a test of the gTTS text to speech conversion. From Sujan Shrestha This is a gtts autotest of the doctor voice"
# output_filepath = "output_gtts.mp3"
# text_to_speech_gtts(input_text=input_text, output_filepath=output_filepath)

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
    
    # auto play the saved audio file
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(
                [r"C:\ffmpeg\ffmpeg-7.1.1-full_build\bin\ffplay.exe", "-nodisp", "-autoexit", output_filepath],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT
            )
        elif os_name == "Linux":  # Linux
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath],
                           stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# # Test
# input_text = "Hello, this is a test of the Elevenlabs text to speech conversion. From Sujan Shrestha This is a Elevenlabs autotest of the doctor voice"
# output_filepath = "output_elevenlabs.mp3"
# text_to_speech_elevenlabs(input_text, output_filepath)
