import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM
from crewai_tools import TavilySearchTool

search_tool = TavilySearchTool()

def create_agents(radical_level=50):
    
    if radical_level < 30:
        tone = "moderate, nuanced, and conciliatory"
        behavior = "You actively look for common ground. You avoid inflammatory language. You respect valid points from the other side."
    elif radical_level < 70:
        tone = "firm, opinionated, and principled"
        behavior = "You stick to your ideological guns. You prioritize your values but remain professional."
    else:
        tone = "radical, aggressive, and uncompromising"
        behavior = "You use emotional, charged language. You view the opposing side as dangerous to the country. You refuse to concede any points."

    blue_pundit = Agent(
        role='Progressive News Analyst',
        goal=f'Analyze news with a {tone} progressive lens.',
        backstory=f"""You are a {tone} journalist for a major left-leaning publication. 
        {behavior}
        You view the world through a lens of social justice and systemic reform. 
        You are skeptical of unchecked capitalism.""",
        tools=[search_tool],
        verbose=True,
        allow_delegation=False,
        llm=LLM(model="openai/gemma2-9b-it", base_url="https://api.groq.com/openai/v1", api_key=os.environ.get("GROQ_API_KEY"))
    )

    red_pundit = Agent(
        role='Conservative News Analyst',
        goal=f'Analyze news with a {tone} conservative lens.',
        backstory=f"""You are a {tone} columnist for a major right-leaning publication. 
        {behavior}
        You view the world through a lens of fiscal responsibility and tradition. 
        You are skeptical of government overreach.""",
        tools=[search_tool],
        verbose=True,
        allow_delegation=False,
        llm=LLM(model="openai/gemma2-9b-it", base_url="https://api.groq.com/openai/v1", api_key=os.environ.get("GROQ_API_KEY"))
    )

    editor = Agent(
        role='Editor-in-Chief',
        goal='Synthesize disparate viewpoints into a balanced, 360-degree report.',
        backstory="""You are the Editor-in-Chief of a No-Spin media outlet. 
        Your job is to take the biased reports from your staff and weave them together. 
        You do not take sides. 
        You identify the undisputed facts and the fundamental disagreements.
        You hate fluff and demand clarity.""",
        verbose=True,
        allow_delegation=False, 
        llm=LLM(model="openai/gemma2-9b-it", base_url="https://api.groq.com/openai/v1", api_key=os.environ.get("GROQ_API_KEY"))
    )

    return blue_pundit, red_pundit, editor