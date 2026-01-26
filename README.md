# 📰 The Anti-Echo Chamber (Newsroom Agent)

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![OpenAI](https://img.shields.io/badge/LLM-GPT--4o-black)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**The Anti-Echo Chamber** is an advanced **AI-powered Multi-Agent
Newsroom** designed to combat media bias and ideological echo chambers.\
It simulates a virtual newsroom where autonomous AI agents investigate
the *same topic* from **opposing political perspectives**, challenge
each other's conclusions, and ultimately synthesize a **neutral,
fact-based report**.

This project is built as a **portfolio-grade system** to demonstrate
advanced skills in: - Multi-agent orchestration - Cognitive
architectures - Real-time research pipelines - Interactive AI systems

------------------------------------------------------------------------

## 🚀 Key Features

### 🧠 Autonomous Multi-Agent Workflow (CrewAI)

-   **🔵 Blue Pundit**\
    Researches topics using a *Progressive / Social-Justice* lens.
-   **🔴 Red Pundit**\
    Researches topics using a *Conservative / Economic-Freedom* lens.
-   **📰 The Editor**\
    A neutral agent that evaluates both sides and compiles the final,
    balanced dossier.

------------------------------------------------------------------------

### ⚔️ Rebuttal Logic (Cognitive Architecture)

Agents don't just work in parallel.

They: 1. Share context 2. Read each other's drafts 3. Generate
**explicit rebuttals and counter-arguments** 4. Refine their positions
before synthesis

This simulates **real editorial debate**, not isolated LLM calls.

------------------------------------------------------------------------

### 🎚️ Dynamic Personality Engine

A **Polarization Slider (0--100%)** in the UI dynamically alters system
prompts at runtime:

-   `0%` → Polite academics
-   `50%` → Opinionated pundits
-   `100%` → Radical partisans

This allows real-time experimentation with **prompt engineering and
ideological intensity**.

------------------------------------------------------------------------

### 🎧 Multi-Modal Output

-   **Audio Briefings** 🎙️\
    Generates podcast-style summaries using **gTTS**
-   **PDF Reports** 📄\
    Downloadable dossiers via **FPDF**
-   **Live Web Research** 🌐\
    Uses **Tavily API** to fetch real-time sources (minimizing
    hallucinations)

------------------------------------------------------------------------

### 💬 Interactive Interrogation Chat

Users can directly question individual agents using **Session State**:

> *"Hey Red Agent, why did you ignore the climate data?"*

This enables **agent-specific accountability and explainability**.

------------------------------------------------------------------------

### 📊 Sentiment & Bias Visualization

-   **TextBlob** analyzes sentiment polarity
-   **Altair** visualizes the ideological gap between agents
-   Makes bias **quantifiable and observable**

------------------------------------------------------------------------

### ⚡ Performance-Oriented Design

-   Asynchronous tasks for **parallel web research**
-   Reduced latency despite multiple agents and live data fetching

------------------------------------------------------------------------

## 🧩 How It Works

### 1️⃣ Research Phase

Both the **Blue Pundit** and **Red Pundit** independently: - Query
Tavily for live sources - Analyze data through their ideological
lenses - Produce structured draft reports

------------------------------------------------------------------------

### 2️⃣ Rebuttal Phase

Agents: - Read each other's drafts - Identify weak assumptions, bias, or
missing data - Write targeted rebuttals and counterpoints

------------------------------------------------------------------------

### 3️⃣ Synthesis Phase

The **Editor Agent**: - Evaluates both perspectives and rebuttals -
Cross-checks factual overlap - Produces a **neutral, evidence-backed
final report**

------------------------------------------------------------------------

## 🛠️ Tech Stack

  Category              Technology
  --------------------- -----------------
  Language              Python 3.12+
  Agent Orchestration   CrewAI
  LLM                   GPT-4o (OpenAI)
  Web Framework         Streamlit
  Search                Tavily API
  Audio                 gTTS
  PDF                   FPDF
  Visualization         Altair
  NLP                   TextBlob
  Package Manager       uv

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/kartik0905/newsroom_agent.git
cd newsroom_agent
```

------------------------------------------------------------------------

### 2️⃣ Set Up Environment Variables

Create a `.env` file in the root directory:

``` env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

------------------------------------------------------------------------

### 3️⃣ Install Dependencies

Using **uv** (recommended):

``` bash
uv sync
```

Or using **pip**:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 4️⃣ Run the Application

``` bash
uv run streamlit run app.py
```

The app will be available at:

    http://localhost:8501

------------------------------------------------------------------------

## 🎯 Why This Project Matters

This system goes beyond simple AI demos: - Demonstrates **real-world
multi-agent coordination** - Showcases **debate, critique, and
synthesis** - Highlights skills in **AI safety, bias mitigation, and
explainability** - Designed to impress **hiring managers and technical
reviewers**

------------------------------------------------------------------------

## 👤 Author

**Kartik (kartik0905)**\
AI & Full-Stack Developer

🔗 GitHub: https://github.com/kartik0905

------------------------------------------------------------------------

## 📜 License

MIT License
