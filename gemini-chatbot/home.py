import streamlit as st
import time

def main():
    st.set_page_config(page_title="AI Chatbot", layout="wide")
    
    # Custom CSS for layout and styling
    st.markdown("""
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(to right, #2c3e50, #4ca1af);
                color: white;
            }
            .navbar {
                display: flex;
                justify-content: space-between;
                background-color: rgba(255, 255, 255, 0);
                padding: 10px 50px;
                border-radius: 10px;
            }
            .navbar a {
                text-decoration: none;
                color: white;
                font-weight: bold;
                margin: 0 15px;
                font-size: 18px;
            }
            .navbar .login-button {
                background-color: #ff4b5c;
                color: white;
                padding: 8px 20px;
                border-radius: 20px;
                text-decoration: none;
                font-size: 16px;
            }
            .container {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 50px;
            }
            .text-section {
                max-width: 50%;
            }
            .title {
                font-size: 50px;
                font-weight: bold;
                color: white;
            }
            .subtitle {
                font-size: 18px;
                color: #ddd;
                margin-top: 10px;
            }
            .chat-button {
                background-color: #ff4b5c;
                color: white;
                padding: 12px 30px;
                font-size: 18px;
                border: none;
                border-radius: 25px;
                cursor: pointer;
                margin-top: 20px;
            }
            .chat-image {
                width: 600px;
                border-radius: 20px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Navigation Bar
    st.markdown("""
        <div class='navbar'>
            <div>
                <a href='#'>HOME</a>
                <a href='#about' class='nav-link'>About</a>
                <a href='#features' class='nav-link'>Features</a>
                <a href='#'>CONTACT US</a>
            </div>
            <a href='#' class='login-button'>LOGIN</a>
        </div>
    """, unsafe_allow_html=True)
    
    # Main Content Section
    st.markdown("""
        <div class='container'>
            <div class='text-section'>
                <div class='title'>Bro-Bot-AI</div>
                <div class='subtitle'>
                    Bro-Bot-AI a Chatbot project made to solve all your queries like a Big Bro
                </div>
                <div class='button-container'>
                </br>
            <a href="bro" target="_self">
                <button style="padding: 15px 25px; font-size: 18px; background-color: #ff4b5c; color: white; border: none; border-radius: 5px; cursor: pointer;">
                    Start Chatting 💬
                </button>
            </a>
        </div>
            </div>
            <div>
                <img src='https://www.computer-talk.com/images/default-source/blogs/ai-chatbot-best-practices.jpg?sfvrsn=f723c44f_1' class='chat-image'>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.image('images/about-image.jpg', caption='Chat-bot interface', width=None)
    with col2:
        st.markdown("""
            <div class='text-section' id='about'>
                <div class='title'>About</div>
                <div class='subtitle'>
                    <h5>Bro.bot.ai is AI-powered chatbot applications designed to simulate human-like interactions. Using the Gemini 1.5 flash model, </br> This bot is tailored to respond to user queries conversationally. Bro.bot.io offers a GUI-based interaction using Streamlit GUI framework.</h5></div>
            </div>
        """, unsafe_allow_html=True)
        
    col3, col4 = st.columns([1, 1])
    with col3:
        st.markdown("""
            <div class='text-section'>
                <div class='title'>Features</div>
                <div class='subtitle'>
                    <h5>This chatbot is designed to assist users with their queries using advanced AI technology. It is built to provide quick and accurate responses to a wide range of questions.</h5>
                   🤖 : Chat-bot offers features image and document analysis capabilities to enhance user engagement and help users find relevant information.
                </br>    🤖 : it also offers a user-friendly interface and can be easily integrated into various applications.
                </br>    🤖 : and also offers a chat-bot interface that allows users to interact with the bot in a more personalized and engaging way.
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.video('images/bro-bot.mp4',autoplay=True,loop=True)
    #https://cdn-wp.bulksignature.com/wp-content/uploads/2024/02/Frame-876-1024x569.png
if __name__ == "__main__":
    main()
