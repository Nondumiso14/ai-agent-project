import os
from dotenv import load_dotenv
from agents import Agent, Runner
#from tools.weather_tool import get_weather
from tools.time_tool import get_time

load_dotenv()

#Defining agent with tools
smart_assistant = Agent(
    name = "SmartAssistant",
    instructions = "You are a helpful assistant, use tools whenever the user asks about the weather or time.",
    model= "gpt-4o-mini",
    tools = [get_time] # once merged with nondumiso -> #tools = [get_weather, get_time]
)


async def run_smart_agent_with_steps(user_prompt: str):
    result = await Runner.run(smart_assistant, user_prompt)

    steps = []
    # Use final_turns to catch the reasoning process
    if hasattr(result, 'final_turns'):
        for turn in result.final_turns:
            if hasattr(turn, 'tool_calls') and turn.tool_calls:
                for call in turn.tool_calls:
                    steps.append(f"Decision: Calling {call.function.name}")

    return {
        "reply": result.final_output,
        "steps": steps
    }