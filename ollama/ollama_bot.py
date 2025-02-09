import time
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:

"""

model = OllamaLLM(model="llama3",role="Bank manager", stream=True)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# def typing_animation(text, delay=0.05):
#     """Simulates typing animation."""
#     for char in text:
#         print(char, end='', flush=True)
#         time.sleep(delay)
#     print()  

def handle_conversation():
    context = ""
    print("Welcome to Malik.bot! \nAsk me anything about programming and I will try to help you. \nto stop chatting to me type quit , bye , exit")
    while True:
        user_input = input('You: ')
        if user_input.lower() in ['quit', 'bye', 'exit']:
            print("Unnat.bot: Goodbye! Have a great day!")
            break
        result = chain.invoke({"context": context, "question": user_input, "role": "Bank manager"})
        for chunk in result:
            time.sleep(0.05)
            print(chunk,end="",flush=True)  # Prepare for typing animation
        # typing_animation(result)  # Simulate typing
        context += f"\nUser:{user_input}\nUnnat.bot:{result}"

if __name__ == "__main__":
    handle_conversation()
