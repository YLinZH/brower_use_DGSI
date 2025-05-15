import os
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig

load_dotenv()

async def answer_test():
    browser = Browser(
        config=BrowserConfig(
            chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            headless=False
        )
    )

    agent = Agent(
        task="""
        Abre Google Docs y localiza el documento titulado “Test sobre Inteligencia Artificial en la educación (2025)”.

        Por cada pregunta del test:
        1. Copia la pregunta y sus opciones.
        2. Abre una nueva pestaña, busca en internet cuál es la mejor respuesta.
        3. Vuelve al documento y marca en **negrita** la respuesta correcta.

        Guarda el documento al terminar.
        """,
        llm=ChatOpenAI(model='gpt-4o'),
        browser=browser,
    )

    await agent.run()
    await browser.close()

if __name__ == '__main__':
    asyncio.run(answer_test())
