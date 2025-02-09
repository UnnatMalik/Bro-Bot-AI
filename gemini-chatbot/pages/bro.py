from turtle import width
import PIL.Image
import google.generativeai as genai
import streamlit as st
import time
import os
import re

# Configure Gemini API
genai.configure(api_key="AIzaSyCDRV4NCysRofqKJIQD8PdFZecDSIXxmBE")
model = genai.GenerativeModel("gemini-1.5-flash", tools='code_execution', system_instruction="You are a kind Programmer assistant.")

# Ensure the 'files' directory exists
if not os.path.exists("files"):
    os.makedirs("files")

st.set_page_config(page_title="Bro-Bot-AI", layout="wide")
st.title("💬 Chat with your Bro")

def sanitize_filename(filename):
    """Sanitize filename to only contain lowercase letters, numbers, and dashes."""
    sanitized = re.sub(r'[^a-z0-9-]', '', filename.lower())
    sanitized = sanitized.strip('-')  # Remove leading/trailing dashes
    return sanitized if sanitized else 'file'

def save_uploaded_file(uploadedfile):
    """Save uploaded file after sanitizing its name."""
    safe_filename = sanitize_filename(os.path.splitext(uploadedfile.name)[0])
    file_extension = os.path.splitext(uploadedfile.name)[1].lower()
    full_filename = f"{safe_filename}{file_extension}"
    file_path = os.path.join("files", full_filename)

    with open(file_path, "wb") as f:
        f.write(uploadedfile.getbuffer())
    
    return file_path, file_extension

def chat_bro(prompt, uploadedfile, chat_history):
    """Handles chat with optional image, PDF, or video inputs."""
    input_data = [prompt, chat_history]

    if uploadedfile:
        file_path, file_extension = save_uploaded_file(uploadedfile)

        if file_extension in ['.png', '.jpg', '.jpeg']:
            st.image(file_path, width=400)
            try:
                image = PIL.Image.open(file_path)  # ✅ Open the image correctly
                input_data.insert(1, image)  # ✅ Add image to model input
            except Exception as e:
                st.error(f"Error opening image: {e}")
        
        elif file_extension == ".pdf":
            st.success(f"Uploaded PDF: {uploadedfile.name}")
            with open(file_path, "rb") as pdf_file:
                pdf_content = pdf_file.read()
            pdf_data = {"mime_type": "application/pdf", "data": pdf_content}
            input_data.insert(1, pdf_data)

        elif file_extension == ".mp4":
            st.video(file_path)
            with open(file_path, "rb") as video_file:
                video_content = video_file.read()
            video_data = {"mime_type": "video/mp4", "data": video_content}
            input_data.insert(1, video_data)

    response = model.generate_content(input_data)
    return response.text

uploaded_file = st.file_uploader("Upload an image, PDF, or video", type=["jpg", "jpeg", "png", "mp4", "pdf"])
user_input = st.chat_input(placeholder="Message BRO")

with st.container(border=True, height=450):
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        with st.chat_message('User', avatar="user"):
            st.markdown(user_input)

        # Generate chat history after adding user input
        chat_history = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state["messages"]])

        if uploaded_file:
            st.session_state["messages"].append({"role": "user", "content": f"Uploaded: {uploaded_file.name}"})

        with st.spinner("Bro is typing..."):
            response_text = chat_bro(user_input, uploaded_file, chat_history)
            with st.chat_message('assistant', avatar="ai"):
                response_container = st.empty()
                streamed_response = ""

                for chunk in response_text:
                    streamed_response += chunk
                    response_container.markdown(streamed_response)
                    time.sleep(0.05)

        st.session_state["messages"].append({"role": "ai", "content": streamed_response})
