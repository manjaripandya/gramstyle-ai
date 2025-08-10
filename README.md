# gramstyle-ai
gramstyle-ai is an AI-powered Instagram assistant app that helps users generate creative captions, relevant hashtags, slect filters, and music suggestions based on uploaded images and selected moods. Built with Streamlit and OpenAI’s GPT model.

## Features

- Upload an image and get AI-generated caption suggestions in various styles (funny, quirky, sarcastic, poetic, and more).
- Receive relevant hashtags tailored to the image and caption style.
- Get Instagram filter recommendations to match the mood.
- Discover music suggestions that fit the image’s vibe and selected music mood.

## Tech Stack

- Python  
- Streamlit (for the web UI)  
- OpenAI GPT-4o-mini API (image understanding + text generation)  
- PIL / Pillow (image processing)

## How to Run

1. Clone the repo:  
   ```bash
   git clone https://github.com/yourusername/gramstyle-ai.git
   cd gramstyle-ai

2. Install dependencies:
   pip install -r requirements.txt

3. Set your OpenAI API key in .env:
   OPENAI_API_KEY=your_api_key_here

4. Run the app:
   streamlit run gramstyle_ai.py
