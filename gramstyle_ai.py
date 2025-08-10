import os
import io
import base64
import openai
from PIL import Image
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
# Load env
load_dotenv()

# Set your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="gramstyle-ai", layout="centered")
st.title("Gramstyle-ai")

# Step 1: Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Step 2: Get user preferences
caption_style = st.selectbox(
    "Choose a caption style:",
    ["funny", "quirky", "sarcastic", "poetic", "aesthetic", "motivational"]
)

music_mood = st.selectbox(
    "Choose a music mood:",
    ["chill", "romantic", "party", "melancholy", "energetic", "lofi", "quirky"]
)

# Step 3: On button click, process image
if uploaded_file and st.button("Generate Suggestions"):
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Analyzing..."):
        # Convert image to base64 string
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        b64_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

        # GPT-4 Vision request
        response = client.chat.completions.create(model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": "You're an Instagram assistant that suggests creative captions, relevant hashtags, filters, and music."},
            {
            "role": "user",
            "content": [
                    {"type": "text", "text": f"""
                        This is an Instagram post. Analyze the image in detail and generate:
                        - One caption {caption_style} caption
                        - 5-7 relevant hashtags that match the image’s subjects, vibe, and audience appeal
                        - A famous Instagram filter according to the {caption_style} and {music_mood} mood
                        - A music suggestion in {music_mood} mood (song name + artist if possible), ensuring it fits the photo’s visual theme, the caption’s tone, and the emotional feel of the post

                        Keep it short and fun. Don't explain anything, just output clearly.
                        """},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_image}"}}
                ]
            }
        ],
        max_tokens=500)

        # Display result
        st.markdown("### InstaGinnie Suggestions")
        st.markdown(response.choices[0].message.content)