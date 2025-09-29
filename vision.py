from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])


model = genai.GenerativeModel("gemini-2.5-flash")


def get_ai_response(prompt, image):
    if prompt or image:
        response = model.generate_content([prompt, image])
        return response.text
    return "Please provide a prompt or upload an image."

st.set_page_config(
    page_title="PixelSage",
    page_icon="🖼️",
    layout="wide"
)

st.sidebar.title("PixelSage 🖼️")
st.sidebar.markdown("""
**Your AI Image Assistant**  
Upload an image or provide a prompt,  
and PixelSage will generate insights for you.
""")
st.sidebar.markdown("---")
st.sidebar.markdown("Developed by: **Shivansh**") 


st.markdown(
    "<h1 style='text-align: center; color: #4B0082;'>PixelSage 🖼️</h1>",
    unsafe_allow_html=True
)
st.markdown("<p style='text-align: center; color: #6A5ACD;'>AI-powered Image Analysis & Text Generation</p>", unsafe_allow_html=True)


col1, col2 = st.columns([2, 3])

with col1:
    prompt = st.text_input("Enter your prompt:", key="prompt")
    submit = st.button("Analyze Image", use_container_width=True)

with col2:
    uploaded_file = st.file_uploader("Upload an image", type=['jpg','jpeg','png'])
    image = None
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)


if submit:
    with st.spinner("Generating response..."):
        response = get_ai_response(prompt, image)
        st.subheader("AI Response")
        st.write(response)


st.markdown("---")
st.markdown("<p style='text-align:center; color: gray;'>PixelSage © 2025</p>", unsafe_allow_html=True)
