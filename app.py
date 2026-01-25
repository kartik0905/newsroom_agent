import streamlit as st
from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Anti-Echo Chamber", page_icon="📰")

st.title("📰 The Anti-Echo Chamber")
st.markdown("### Multi-Agent News Analysis")

topic = st.text_input("Enter a controversial topic:", "Universal Basic Income")

if st.button("Run Analysis"):
    with st.spinner("The Agents are debating... Check your terminal for live logs."):
        try:
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
            
            st.success("Analysis Complete!")
            st.markdown("---")
            st.markdown(result)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")