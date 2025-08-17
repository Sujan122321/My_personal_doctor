# My_personal_doctor

My_personal_doctor is an AI-powered assistant designed to help users with health-related queries, provide basic medical advice, and guide users to appropriate resources.

## Features

- AI-driven health Q&A
- Symptom checker
- Personalized health tips
- Easy-to-use interface

## Setup

1. **Clone the repository:**
	```powershell
	git clone https://github.com/Sujan122321/My_personal_doctor.git
	cd My_personal_doctor
	```

2. **Create and activate a Conda environment:**
	```powershell
	conda create --name doctor python=3.12
	conda activate doctor
	```

3. **Install dependencies:**
	```powershell
	pip install -r requirements.txt
	```

## Usage

Run the main application (update with your main script name if different):
```powershell
python main.py
```

## Utilizations
- Using Groq API key 
- using multimode llm
- using OpenApi for the speech to text (STT AI model)
- Using meta vision model 

## Project Work flow
- 1. Audio input from the user
- 2. Image input from the user
- 3. Speech to text conversion 
- 4. Trinscribed Text/User query
- 5. Vison model
- 6. LLM Response
- 7. Text to speech (TTS AI Model)
- 8.  Finnal audio output

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.