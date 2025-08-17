# step 1 : Setup Groq API  key

import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
# Get the Groq API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")


# step 2: Convert image to required format
import base64  # Function to convert image to base64 string

def convert_image_to_base64(image_path):
    """
    Convert an image file to a base64 encoded string.
    
    :param image_path: Path to the image file.
    :return: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    

# Step 3: Setup Multimodal LLM

from groq import Groq

client = Groq()
query = "Placeholder query"
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
      {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": query  
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": convert_image_to_base64("path/to/your/image.jpg") 
            }
        ]
      }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")