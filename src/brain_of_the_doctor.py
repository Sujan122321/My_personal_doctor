
import os
import base64
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path

# Step 1: Load API key from .env
load_dotenv()  # looks for .env file in project root
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY is not set in environment variables")

# Step 2: Encode image to base64
# Use raw string or Path() to avoid invalid escape warnings
image_path = Path(r"G:\Git_hub_projects\Ai_Doctor\My_personal_doctor\src\image.jpeg")

def convert_image_to_base64(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

encoded_image = convert_image_to_base64(image_path)

# Step 3: Setup Multi-Modal LLM
client = Groq(api_key=GROQ_API_KEY)

query = "Is there something wrong with my hair?"
model = "meta-llama/llama-4-scout-17b-16e-instruct"  # vision-enabled model

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
    temperature=0.2,
    max_completion_tokens=512,
)

print("🤖 AI Response:")
print(chat_completion.choices[0].message.content)

# Step 4: Build prompt with vision model
