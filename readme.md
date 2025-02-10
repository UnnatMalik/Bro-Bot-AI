# 🤖 Bro-Bot-AI 🤖

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

## ✨ Overview

Bro-Bot-AI is your one-stop shop for exploring AI chatbot technologies! This repository showcases two distinct chatbot implementations, each leveraging powerful AI models and frameworks:

*   **🧠 Llama3 Powered Chatbot (Ollama & Langchain):**  Experience the cutting-edge conversational abilities of the Llama3 model, locally hosted with Ollama. Enhanced with Langchain, this chatbot offers advanced features like memory and tool integration.
*   **⚡️ GEMINI 1.5 Flash Chatbot (Streamlit):**  Interact with a fast and efficient chatbot built using Streamlit for a user-friendly interface and Google's GEMINI 1.5 Flash model for rapid responses. Ideal for quick interactions and prototyping.

## 🚀 Features

*   **Ollama/Llama3 Chatbot:**
    *   Uses the Llama3 model for high-quality conversational AI.
    *   Leverages Ollama for local model hosting and easy deployment.
    *   Employs Langchain for advanced features:
        *   Conversation Memory
        *   Tool Integration (e.g., web search)
*   **Streamlit/GEMINI 1.5 Flash Chatbot:**
    *   Built with Streamlit for a clean and intuitive user interface.
    *   Utilizes Google's GEMINI 1.5 Flash for fast and efficient responses.
    *   Easy to deploy and experiment with.
    *   Upload and analyze files in real-time.

## 🛠️ Technologies Used

*   [Ollama](https://ollama.com/) - For running Llama3 locally
*   [Llama3](https://ai.meta.com/llama/) - The powerful language model
*   [Langchain](https://www.langchain.com/) - For building complex AI applications
*   [Streamlit](https://streamlit.io/) - For creating interactive web apps
*   [GEMINI 1.5 Flash](https://ai.google.dev/models/gemini) - Google's fast language model

## ⬇️ Getting Started

### Prerequisites

*   **Python 3.9+**
*   **Ollama (for Llama3 Chatbot):**  Follow the installation instructions on the [Ollama website](https://ollama.com/).
*   **Gemini (for Gemini Chatbot):** [Gemini](https://ai.google.dev/gemini-api/docs)

### Installation

1.  **Clone the repository:**

    ```
    git clone https://github.com/UnnatMalik/Bro-Bot-AI.git
    cd Bro-Bot-AI
    ```

2.  **Install dependencies:**

    ```
    pip install -r requirements.txt
    ```

### Running the Chatbots

#### Llama3 Chatbot (Ollama & Langchain)

1.  **Download the Llama3 model (if you haven't already):**

    ```
    ollama pull llama3
    ```

2.  **Run the chatbot:**

    ```
    python llama3_chatbot.py  # Replace with your actual script name
    ```

#### GEMINI 1.5 Flash Chatbot (Streamlit)

1.  **Set your GEMINI API Key:**

    ```
    #Option 1: Set as an environment variable
    export GOOGLE_API_KEY="YOUR_API_KEY"

    #Option 2: Place directly in the script (Not Recommended for security reasons)
    # in home.py (or your script name), replace "YOUR_API_KEY" with your actual key
    ```

2.  **Run the Streamlit app:**

    ```
    streamlit run home.py  # Replace with your actual script name
    ```

## 💬 Contact
For queries, reach out via [LinkedIn](https://www.linkedin.com/in/unnat-malik)