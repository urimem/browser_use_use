from browser_use import ChatOllama, Agent
import asyncio

# More info: https://github.com/browser-use/awesome-prompts?tab=readme-ov-file#testing-and-qa-prompts
task = """
Your task is to go to the Instagram user profile page: https://www.instagram.com/zuzkalight/

And report the following information:
1. The number of followers
2. The number of followings
3. The number of posts
4. The description in the profile
5. The URLs in the profile
"""

# task = """What is the capital of France? Answer in one short sentence."""

llm = ChatOllama(model="gemma2:2b") # "qwen3-vl:8b")

async def main():
    agent = Agent(
        task=task,
        llm=llm,
#        flash_mode=True, # remove Eval steps
        llm_timeout=300,
        step_timeout=300,
        #tool_call_in_content=False
    )
    await agent.run()

asyncio.run(main())