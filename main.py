import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks

topic = "Universal Basic Income"

blue_pundit, red_pundit, editor = create_agents()
tasks = create_tasks(blue_pundit, red_pundit, editor, topic)

newsroom_crew = Crew(
    agents=[blue_pundit, red_pundit, editor],
    tasks=tasks,
    process=Process.hierarchical,
    manager_llm="gpt-4o",
    verbose=True
)

result = newsroom_crew.kickoff()
print(result)