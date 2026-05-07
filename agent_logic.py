import os
from dotenv import load_dotenv
from agents import Agent, Runner
#from tools.weather_tool import get_weather
#from tools.time_tool import get_time

load_dotenv()

#Defining agent with tools
smart_assistant = Agent(
    name = "SmartAssistant",
    instructions = "You are a helpful assistant, use tools whenever the user asks about the weather or time.",
    model= "gpt-4o-mini",
    #tools = [get_weather, get_time]
)


async def run_smart_agen_with_steps(user_prompt: str):
    result = await Runner.run(smart_assistant, user_prompt)

    #Extracting the reasoning tool calls and final output for the ui 
    steps = []
    for turn in result.turns:
        if turn.tool_calls:
            for call in turn.tool_calls:
                steps.push(f"Decision: Calling {call.function.name} with {call.function.arguments}")
    return {
        "reply": result.final_output,
        "steps": steps
    }



