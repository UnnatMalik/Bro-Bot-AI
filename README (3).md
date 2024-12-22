
<br/>
<div align="center">
 ![Screenshot](https://github.com/user-attachments/assets/cf55f036-8e52-499f-802e-63684e78d4c1)
<h3 align="center">Bro-Bot-AI</h3>
<p align="center">
Bro-bot-AI is here to help you bro

![Screenshot 2024-12-22 224613](https://github.com/user-attachments/assets/d18aa2d3-d1c2-42d4-9cb9-0a3c50eed5d9)
 



</p>
</div>

## About The Project

Bro.bot.ai is AI-powered chatbot applications designed to simulate human-like interactions. Using the powerful Ollama LLM using LLama3 model, this botsare tailored to respond to user queries conversationally. Bro.bot.io offers a GUI-based interaction using Flet GUI framework.

the ollama_bot.py file contain the raw functionality of Bro_bot_ai It is command-line interface. 

Both bots can be programmed to emulate the role of your choice and can answer queries interactively.

This project is create by locally setting up the Ollama LLM.

### Here are certain features of the project :

- AI chatbot powered by LangChain Ollama LLM (Llama3 model).

-  GUI support via Flet for Bro.bot.io.

-  CLI-based interaction for Ollama_bot.py

- Context-based conversation history for personalized responses.

- Role-based behavior emulating for better experience and project implementation .

- Streamed responses for a more interactive experience.
- User-friendly message handling and typing animations.

### Project ScreenShots
  ![Screenshot 2024-12-22 225019](https://github.com/user-attachments/assets/adec022e-720b-49b9-9899-8d4754ab8460)
  -------
  ![Screenshot 2024-12-22 225427](https://github.com/user-attachments/assets/f2cc9a7c-c2a3-4453-aa5d-f64421cc6002)

### Built With

This Project is built with LangChain Ollama For integrating advanced language models (Llama3) and handling conversational workflows.
Flet A Python framework for building web-based GUI applications. 
Python Standard Libraries For threading, time management, and input/output operations.

- [Python](https://python.org)
- [Flet](https://flet.dev)
- [Ollama ](https://ollama.com)
- [Lang-Chain](https://www.langchain.com)
### Prerequisites

Ensure the following are installed on your system:

 - Python 3.8 or above
- Pip package manager
  
### Installation

Follow the below steps to setup the project locally on your computer

1. Clone the repo
   ```sh
   git clone < repository-url >
   cd < repository-folder >
   ```
2. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run below command to start the Chat-bot( With UI )
   ```sh
   python Bro_Bot_AI.py
   ```
    Run the below command to start Chat-bot(Without UI)
   ```sh
   python ollama_bot.py
   ```


# Usage

### Bro.bot.io 
Run the application:

   ```bash
   python Bro_Bot_AI.py
   ```
- The GUI interface will open in your default web browser.
- Interact with the chatbot by typing your queries in the text field.


### Malik.bot
Run the script:
   ```sh 
python ollama_bot.py
   ```
- Start chatting directly in the terminal. 
- Type your queries and receive real-time responses.
- To exit the session, type quit, bye, or exit.

## Usage

- The chatbot’s role can predefined as per the needs within the LangChain Ollama model instantiation.

- Conversation template:
   ```Python 
   Answer the question below.

   Here is the conversation history: {context}

  Question: {question}

  Answer:
  ```
