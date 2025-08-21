
import os
import base64
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path

# Step 1: Load API key from .env
load_dotenv()                                           # looks for .env file in project root
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is not set in environment variables")

# Step 2: Encode image to base64
# Use raw string or Path() to avoid invalid escape warnings
# image_path = Path(r"G:\Git_hub_projects\Ai_Doctor\My_personal_doctor\src\image.jpeg")

def encode_image(image_path):
    """
    Encode an image file to base64 string.
    """
    image_file = open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode("utf-8")


# Step 3: Setup Multi-Modal LLM

query = "Is there any problem with the image?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image_with_groq(query, model, encoded_image):
    """
    Analyze an image using Groq's multi-modal LLM.
    
    Args:
        image_path (Path): Path to the image file.
        query (str): Text query to analyze the image.
    
    Returns:
        str: AI response from the model.
    """
    client = Groq(api_key=GROQ_API_KEY)
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text",
                "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}
                },
            ],
        }
    ]

    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return chat_completion.choices[0].message.content

