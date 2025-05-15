import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

async def create_test():
    current_topic = "Inteligencia Artificial en la educación (2025)"

    browser = Browser(
        config=BrowserConfig(
            chrome_instance_path="C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome-profile"
,  # Ruta común en Windows
            headless=False
        )
    )

    agent = Agent(
        task=f"""
        Abre https://docs.google.com/document/ y crea un nuevo documento.
        Escribe un TEST de opción múltiple sobre el tema actual: **{current_topic}**.

        Instrucciones:
        - Escribe 5 preguntas de opción múltiple.
        - Cada una debe tener 4 opciones (a, b, c, d).
        - Marca la respuesta correcta en **negrita**.
        - Usa títulos y subtítulos para organizar.
        - Guarda el documento al final.
        """,
        llm=ChatOpenAI(
            model='gpt-4o',
            openai_api_key=api_key
        ),
        browser=browser,
    )

    await agent.run()
    await browser.close()

if __name__ == '__main__':
    asyncio.run(create_test())
