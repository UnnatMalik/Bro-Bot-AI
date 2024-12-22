import flet as ft 
from langchain_ollama import OllamaLLM 
from langchain_core.prompts import ChatPromptTemplate
from threading import Thread
import time

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:

"""

model = OllamaLLM(model="llama3",role="Bank manager", stream=True)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def main(page: ft.Page):
    page.title = "Bro.bot.io"
    page.padding = 20
    page.auto_scroll = True
    
    messages = ft.Column(expand=True,width=1500, height=500, scroll="auto" ,spacing=10)
    context = ""
    thinking = ft.Text("Bro is thinking...", color=ft.Colors.GREY)
    def bot_typing_animation(response_text):
        messages.controls.remove(thinking)
        typing_message = ft.Text("Bro is typing...", color=ft.Colors.GREY)
        messages.controls.append(typing_message)
        page.update()

        time.sleep(3)
        messages.controls.remove(typing_message)
        bot_message = ft.Text("Bro: ", color=ft.Colors.GREEN, weight=ft.FontWeight.BOLD,enable_interactive_selection=True)
        messages.controls.append(ft.Row([bot_message], alignment="start", expand=0))
        page.update()

        for chunk in response_text:
            for char in chunk:
                bot_message.value += char
                page.update()
                time.sleep(0.05)  # Adjust delay as needed
        page.update()

    def handle_conversation(e):
        nonlocal context
        user_message = user_input.value.strip()
        if user_message:
            # Add user message immediately
            messages.controls.append(
                ft.Row([ft.Text(f"User: {user_message}", color="blue",enable_interactive_selection=True)],alignment="end",expand=0)
            )
            user_input.value = ""  # Clear the input field
            page.update()  # Update the page to show the user message

            if user_message.lower() in ['quit', 'bye', 'exit']:
                messages.controls.append(
                    ft.Row([ft.Text("Bro: Goodbye!", color="green")],alignment="start",expand=0)
                )
                page.update()
                return
            messages.controls.append(thinking)
            page.update()
            result = chain.invoke({"context": context, "question": user_message})
            Thread(target=bot_typing_animation, args=(result,)).start()
            context += f"\nUser:{user_message}\nBro:{result}"

            page.update()  # Update the page to show the bot's response
    
    user_input = ft.TextField(hint_text="Type your message here...", expand=True,autofocus=True, border_color=ft.Colors.WHITE)
    send_button = ft.IconButton(ft.Icons.SEND, on_click=handle_conversation, icon_color=ft.Colors.WHITE, icon_size=32)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Bro.bot.io", size=20, weight=ft.FontWeight.BOLD),
                ft.Divider(),
                messages,
                ft.Divider(),
                ft.Row([user_input, send_button], alignment="center"),
            ],
            expand=True,
        )
    )

ft.app(target=main,view=ft.WEB_BROWSER)
