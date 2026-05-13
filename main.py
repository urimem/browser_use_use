from browser_use.llm import ChatOllama
from browser_use import Agent
import asyncio

# https://github.com/browser-use/awesome-prompts?tab=readme-ov-file#testing-and-qa-prompts
# task = """
# Your task is to go to the Instagram user profile page: https://www.instagram.com/zuzkalight/

# And report the following information:
# 1. The number of followers
# 2. The number of followings
# 3. The number of posts
# 4. The description in the profile
# 5. The URLs in the profile
# """

# 
task = """What do you think about raising kids in the city?"""

llm = ChatOllama(model="qwen3-vl:8b")

async def main():
    agent = Agent(
        task=task,
        llm=llm,
        #tool_call_in_content=False
    )
    await agent.run()

asyncio.run(main())