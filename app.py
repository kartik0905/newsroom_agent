import os
import streamlit as st
import pandas as pd
import altair as alt
from textblob import TextBlob
from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks
from dotenv import load_dotenv
import re
from fpdf import FPDF
import io

load_dotenv(override=True)

st.set_page_config(page_title="Anti-Echo Chamber", page_icon="📰", layout="wide")

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
    
    clean_text = text.replace("**", "").replace("##", "").replace("###", "")
    clean_text = clean_text.encode('latin-1', 'replace').decode('latin-1')
    
    pdf.multi_cell(0, 10, clean_text)
    return pdf.output(dest='S').encode('latin-1')

with st.sidebar:
    st.header("⚙️ Configuration")
    st.markdown("Control the intensity of the debate.")
    radicalness = st.slider("Polarization Level", 0, 100, 50)
    
    if radicalness > 75:
        st.error("🔥 Mode: RADICAL")
    elif radicalness < 25:
        st.success("🍵 Mode: PEACEFUL")
    else:
        st.info("⚖️ Mode: STANDARD")

st.title("📰 The Anti-Echo Chamber")
st.markdown("### 🤖 AI-Powered Bias Detector")

topic = st.text_input("Enter a controversial topic:", "Crypto Regulation")

if st.button("🚀 Run Analysis"):
    
    with st.spinner("🤖 The Agents are researching and debating..."):
        try:
            blue_pundit, red_pundit, editor = create_agents(radical_level=radicalness)
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
                try:
                    blue_part = full_text.split("Left View")[1].split("Right View")[0]
                    blue_score = TextBlob(blue_part).sentiment.polarity
                except: pass
            
            if "Right View" in full_text:
                try:
                    red_part = full_text.split("Right View")[1].split("Divergence")[0]
                    red_score = TextBlob(red_part).sentiment.polarity
                except: pass
            
            st.success("Analysis Complete!")

            st.divider()
            
            tab1, tab2, tab3 = st.tabs(["📝 The Report", "📊 Bias Data", "💾 Download"])
            
            with tab1:
                st.markdown(result)
                
                st.divider()
                st.subheader("📚 Sources Cited")
                urls = re.findall(r'(https?://[^\s]+)', str(result))
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
                st.write("Download a clean PDF version of this debate for offline reading.")
                
                pdf_bytes = create_pdf(full_text, topic)
                
                st.download_button(
                    label="📄 Download PDF Report",
                    data=pdf_bytes,
                    file_name=f"{topic}_Analysis.pdf",
                    mime="application/pdf"
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")