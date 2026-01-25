
# 📰 Newsroom Agent: The Anti-Echo Chamber

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange)
![OpenAI](https://img.shields.io/badge/LLM-GPT--4o-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-ff4b4b)
![Tavily](https://img.shields.io/badge/Search-Tavily-purple)
![Altair](https://img.shields.io/badge/Charts-Altair-lightgrey)
![License](https://img.shields.io/badge/License-MIT-black)

**Newsroom Agent: The Anti-Echo Chamber** is an AI-powered **Multi-Agent System** designed to combat media bias and ideological echo chambers.  
It simulates a virtual newsroom where autonomous AI agents — each with distinct, programmed political personalities — research the *same* news topic from opposing ideological perspectives.  
A neutral **Editor** agent then synthesizes these perspectives into a single, structured, objective dossier.

---

## 🚀 Project Overview

In an era of polarized media, Newsroom Agent provides a structured way to:

- Compare how the same story is framed across ideological lines  
- Separate **verifiable facts** from **ideological narratives**  
- Quantify polarization using sentiment analysis  
- Present findings in a clean, interactive dashboard  

At its core, the system operates as a **hierarchical multi-agent workflow**, orchestrated using **CrewAI**.

---

## 🧠 System Architecture

### Autonomous Multi-Agent Crew

The application orchestrates three specialized agents:

- **🔵 The Blue Pundit**  
  Researches progressive and left-leaning media sources, focusing on social justice, equity, and systemic impact.

- **🔴 The Red Pundit**  
  Researches conservative and right-leaning media sources, emphasizing economic freedom, individual responsibility, and traditional values.

- **📝 The Editor**  
  Acts as a neutral authority that:
  - Extracts consensus facts  
  - Identifies conflicting narratives  
  - Produces a structured *“Facts vs. Narratives”* report

All agents operate autonomously and concurrently.

---

## ✨ Key Features

### 🧩 Multi-Agent Orchestration
- Built using **CrewAI** with a **hierarchical process**
- Clear separation of roles, responsibilities, and outputs

### 🎛️ Dynamic Personality Engine
- Interactive **Polarization Slider**
- Adjusts agent radicalness in real time via **dynamic prompt injection**
- Ranges from *“Polite Academic Debate”* to *“Cable News Shout-fest”*

### 🌐 Real-Time Internet Search
- Integrated **Tavily Search API**
- Fetches live, up-to-date articles
- Minimizes hallucinations and stale knowledge

### 📊 Sentiment Intelligence
- Uses **TextBlob** for NLP sentiment analysis
- Calculates a **Polarity Score** (-1.0 to +1.0) for each ideological report
- Visualizes the **Ideological Gap** using **Altair charts**

### 🖥️ Interactive Dashboard
- Built with **Streamlit**
- Tabbed views for each agent
- Clickable source citations
- Real-time logs of agent reasoning and execution

### 📄 PDF Export
- Final synthesized report downloadable as a **formatted PDF**
- Enables offline reading and sharing

---

## 🛠️ Tech Stack

**Core**
- Python 3.12+

**Agent Orchestration**
- CrewAI (Hierarchical Process)

**LLM**
- GPT-4o (OpenAI)

**Web UI**
- Streamlit

**Tools & Libraries**
- Tavily Search Tool (Live Web Search)
- TextBlob (Sentiment Analysis)
- Altair (Data Visualization)
- FPDF (PDF Generation)

**Package Management**
- uv (Astral)

---

## 📦 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kartik0905/newsroom_agent.git
cd newsroom-agent
```

### 2️⃣ Set Up Environment Variables
Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 3️⃣ Install Dependencies (via `uv`)
```bash
uv sync
```

### 4️⃣ Run the Application
```bash
uv run streamlit run app.py
```

---

## 📂 Project Structure (Simplified)

```text
.
├── agents/
├── tools/
├── app.py
├── crew.py
├── utils/
├── requirements.lock
└── README.md
```

---

## 🔮 Future Roadmap

- 🎙️ Audio Briefings  
- ⚔️ Rebuttal Mode  
- 🧠 Source Credibility Scoring  
- 👥 Additional Ideological Agents  

---

## 📜 License

MIT License
