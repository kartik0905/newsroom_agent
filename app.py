import os
import streamlit as st
import pandas as pd
import altair as alt
from textblob import TextBlob
from crewai import Crew, Process, Task
from agents import create_agents
from tasks import create_tasks
from dotenv import load_dotenv
import re
from fpdf import FPDF
import io
from gtts import gTTS

load_dotenv(override=True)

st.set_page_config(page_title="Anti-Echo Chamber", page_icon="📰", layout="wide")

if 'report_text' not in st.session_state:
    st.session_state.report_text = ""
if 'topic' not in st.session_state:
    st.session_state.topic = ""
if 'radicalness' not in st.session_state:
    st.session_state.radicalness = 50
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []



def clean_text_for_display(text):
    """Removes the markdown code block wrappers so Streamlit renders it as HTML."""
    return text.replace("```markdown", "").replace("```", "").strip()

def create_pdf(text, topic):
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, f'Analysis Report: {topic}', 0, 1, 'C')
            self.ln(10)
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    
    clean_text = text.replace("**", "").replace("##", "").replace("###", "").replace("```markdown", "").replace("```", "")
    clean_text = clean_text.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 10, clean_text)
    return pdf.output(dest='S').encode('latin-1')

def generate_audio(text):
    clean_text = text.replace("##", "").replace("**", "").replace("###", "").replace(">", "").replace("```", "")
    tts = gTTS(clean_text, lang='en')
    audio_fp = io.BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

def ask_specific_agent(agent_name, user_question, context_text, radical_level):
    blue, red, editor = create_agents(radical_level)
    
    target_agent = editor
    if agent_name == "Blue Pundit (Left)":
        target_agent = blue
    elif agent_name == "Red Pundit (Right)":
        target_agent = red

    answer_task = Task(
        description=f"""
        The user has a follow-up question about the report you just wrote.
        Topic: {st.session_state.topic}
        Context: {context_text}
        User Question: "{user_question}"
        Answer directly to the user in your persona ({agent_name}). Keep it under 100 words.
        """,
        expected_output="A conversational answer.",
        agent=target_agent
    )

    mini_crew = Crew(agents=[target_agent], tasks=[answer_task], verbose=True)
    return mini_crew.kickoff()

with st.sidebar:
    st.header("⚙️ Configuration")
    st.markdown("Control the intensity of the debate.")
    radicalness_input = st.slider("Polarization Level", 0, 100, 50)
    
    if radicalness_input > 75:
        st.error("🔥 Mode: RADICAL")
    elif radicalness_input < 25:
        st.success("🍵 Mode: PEACEFUL")
    else:
        st.info("⚖️ Mode: STANDARD")

st.title("📰 The Anti-Echo Chamber")
st.markdown("### 🤖 AI-Powered Bias Detector")

topic_input = st.text_input("Enter a controversial topic:", "Crypto Regulation")

if st.button("🚀 Run Analysis"):
    st.session_state.topic = topic_input
    st.session_state.radicalness = radicalness_input
    st.session_state.chat_history = [] 
    
    with st.spinner("🤖 The Agents are researching and debating..."):
        try:
            blue_pundit, red_pundit, editor = create_agents(radical_level=radicalness_input)
            tasks = create_tasks(blue_pundit, red_pundit, editor, topic_input)

            newsroom_crew = Crew(
                agents=[blue_pundit, red_pundit, editor],
                tasks=tasks,
                process=Process.sequential,
                verbose=True 
            )

            result = newsroom_crew.kickoff()
            st.session_state.report_text = clean_text_for_display(str(result))
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

if st.session_state.report_text:
    
    full_text = st.session_state.report_text
    
    blue_score = 0
    red_score = 0
    try:
        if "Section 2: The Left View" in full_text and "Section 3: The Right View" in full_text:
            blue_part = full_text.split("Section 2: The Left View")[1].split("Section 3: The Right View")[0]
            blue_score = TextBlob(blue_part).sentiment.polarity
        if "Section 3: The Right View" in full_text and "Section 4: The Divergence" in full_text:
            red_part = full_text.split("Section 3: The Right View")[1].split("Section 4: The Divergence")[0]
            red_score = TextBlob(red_part).sentiment.polarity
    except: pass

    st.success("Analysis Complete!")
    st.divider()
    
    tab1, tab2, tab3, tab4 = st.tabs(["📝 The Report", "📊 Bias Data", "💾 Download", "💬 Chat with Pundits"])
    
    with tab1:
        st.subheader("🎧 Audio Briefing")
        with st.spinner("Generating Audio..."):
            audio_bytes = generate_audio(full_text)
            st.audio(audio_bytes, format='audio/mp3')
        
        st.divider()
        st.markdown(full_text)
        
        st.divider()
        st.subheader("📚 Sources Cited")
        urls = re.findall(r'(https?://[^\s]+)', full_text)
        if urls:
            unique_urls = list(set(urls))
            cols = st.columns(3)
            for i, url in enumerate(unique_urls):
                with cols[i % 3]:
                    st.link_button(f"Link {i+1}", url, use_container_width=True)

    with tab2:
        st.subheader("Bias Analysis")
        chart_data = pd.DataFrame({
            "Pundit": ["Blue (Left)", "Red (Right)"],
            "Sentiment": [blue_score, red_score]
        })
        c = alt.Chart(chart_data).mark_bar().encode(
            x=alt.X('Pundit', sort=None),
            y=alt.Y('Sentiment', scale=alt.Scale(domain=[-1, 1])),
            color=alt.Color('Pundit', scale=alt.Scale(range=['#2986CC', '#CC0000']), legend=None),
            tooltip=['Pundit', 'Sentiment']
        ).properties(height=300)
        st.altair_chart(c, use_container_width=True)

    with tab3:
        st.subheader("Export Report")
        st.write("Download a clean PDF version of this debate.")
        pdf_bytes = create_pdf(full_text, st.session_state.topic)
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_bytes,
            file_name=f"{st.session_state.topic}_Analysis.pdf",
            mime="application/pdf"
        )

    with tab4:
        st.subheader("💬 Interrogate the Agents")
        st.caption("Ask specific questions based on their analysis.")
        
        selected_agent = st.selectbox("Who do you want to ask?", ["Editor (Neutral)", "Blue Pundit (Left)", "Red Pundit (Right)"])
        
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
        
        if prompt := st.chat_input("Ask a follow-up question..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            with st.chat_message("assistant"):
                with st.spinner(f"{selected_agent} is thinking..."):
                    answer = ask_specific_agent(
                        selected_agent, 
                        prompt, 
                        st.session_state.report_text,
                        st.session_state.radicalness
                    )
                    clean_answer = str(answer).replace("```markdown", "").replace("```", "")
                    st.markdown(clean_answer)
                    
            st.session_state.chat_history.append({"role": "assistant", "content": clean_answer})