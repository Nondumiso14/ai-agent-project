import os
from dotenv import load_dotenv
from agents import Agent, Runner
#from tools.weather_tool import get_weather
#from tools.time_tool import get_time

load_dotenv()

# Define the agent with its tools
smart_assistant = Agent(
    name="SmartAssistant",
    instructions="You are a helpful assistant. Use tools whenever users ask about weather or time.",
    model="gpt-4o-mini",
    #tools=[get_weather, get_time]
)

async def run_smart_agent(user_prompt: str):
    # Runner handles the tool-call loop for you
    result = await Runner.run(smart_assistant, user_prompt)
    return result.final_output