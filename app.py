import streamlit as st
import pandas as pd
import altair as alt
from textblob import TextBlob
from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Anti-Echo Chamber", page_icon="📰", layout="wide")

st.title("📰 The Anti-Echo Chamber")
st.markdown("### 🤖 AI-Powered Bias Detector")

with st.expander("ℹ️ How this works"):
    st.write("""
    1. **Blue Agent** (Left-Wing) searches progressive media.
    2. **Red Agent** (Right-Wing) searches conservative media.
    3. **Editor Agent** synthesizes the debate.
    4. **Sentiment Engine** scores the emotional tone of each side.
    """)

topic = st.text_input("Enter a controversial topic:", "Crypto Regulation")

if st.button("🚀 Run Analysis"):
    with st.spinner("🤖 The Agents are debating... (This takes about 30-60s)"):
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
            
            full_text = str(result)
            
            blue_score = 0
            red_score = 0
            
            if "Left View" in full_text:
                blue_part = full_text.split("Left View")[1].split("Right View")[0]
                blue_score = TextBlob(blue_part).sentiment.polarity
            
            if "Right View" in full_text:
                try:
                    red_part = full_text.split("Right View")[1].split("Divergence")[0]
                    red_score = TextBlob(red_part).sentiment.polarity
                except:
                    red_score = 0

            st.success("Analysis Complete!")
            st.divider()
            st.subheader("📚 Sources Cited")
            
            import re
            urls = re.findall(r'(https?://[^\s]+)', str(result))
            
            if urls:
                unique_urls = list(set(urls))
                cols = st.columns(3) 
                for i, url in enumerate(unique_urls):
                    with cols[i % 3]: 
                        st.link_button(f"Source {i+1}", url, use_container_width=True)
            else:
                st.info("No direct URLs found in the text.")

            col1, col2 = st.columns([2, 1])

            with col1:
                st.markdown("### 📝 Executive Summary")
                st.markdown(result)

            with col2:
                st.markdown("### 📊 Bias Meter")
                st.caption("Sentiment Score (-1.0 Negative to +1.0 Positive)")
                

                chart_data = pd.DataFrame({
                    "Pundit": ["Blue (Left)", "Red (Right)"],
                    "Sentiment": [blue_score, red_score]
                })
                

                c = alt.Chart(chart_data).mark_bar().encode(
                    x=alt.X('Pundit', sort=None),
                    y=alt.Y('Sentiment', scale=alt.Scale(domain=[-1, 1])), 
                    color=alt.Color(
                        'Pundit', 
                        scale=alt.Scale(
                            domain=['Blue (Left)', 'Red (Right)'], 
                            range=['#2986CC', '#CC0000']  
                        ),
                        legend=None
                    ),
                    tooltip=['Pundit', 'Sentiment']
                ).properties(height=300)

                st.altair_chart(c, use_container_width=True)

                if abs(blue_score - red_score) > 0.3:
                    st.warning("⚠️ High Polarization Detected!")
                elif abs(blue_score - red_score) < 0.1:
                    st.info("🤝 High Consensus Detected.")
                else:
                    st.info("✅ Moderate Divergence.")

        except Exception as e:
            st.error(f"An error occurred: {e}")