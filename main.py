from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
load_dotenv()

# A very general example task
# See for more examples:
# https://github.com/browser-use/awesome-prompts?tab=readme-ov-file#testing-and-qa-prompts
task = """
You are an experienced QA tester.
Your task is an exploratory blackbox testing for the website https://ibm.com

Please perform site testing and generate report for all issues you find.
"""
async def main():
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())