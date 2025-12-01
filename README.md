# 🤖 AI Learning Partner - Multi-Agent Study Companion

## Project Status

* **Running**: CLI Interface
* **Base Model**: Google Gemini (via google-genai SDK)

This is a professional, modular AI learning system designed for deep learning and time management. It leverages Google Gemini, a multi-agent architecture, and session persistence to provide a coherent, context-aware learning experience.

---

## ✨ Key Features & Techniques

This project demonstrates how to use the Google Gen AI SDK to build a multi-agent system with agentic capabilities, organized through clearly separated Python modules.

### 1. Multi-Agent Routing 🎛️

The main script `main.py` routes user-selected CLI inputs to the correct specialized Agent module.

* Interface: CLI menu to switch between teaching, planning, and chat modes
* Modularization: Each Agent uses its own System Instruction to maintain consistent, domain-specific responses

### 2. Context-Aware Session Persistence 💬

Conversation history is saved locally in `chat_sessions.json`.

* Technique: Session Persistence
* Functionality: `chat_buddy.py` uses Gemini Chat Sessions to maintain conversational context

### 3. Advanced Tool Calling (Tools) 🛠️

Agents execute tasks through Python functions, supported by the shared `gemini_client.py` for all API requests.

* The planning logic is handled by `planner.py`, which generates optimized daily schedules using role-based instructions

---

## 🏗️ Project Architecture

The project follows a modular structure, with each file focusing on a specific responsibility:

| File / Module      | Responsibility           | Key Functions                                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------------------------- |
| `main.py`          | Orchestrator             | Entry point, CLI management, Agent routing                                      |
| `gemini_client.py` | API Client               | Communicates with Gemini API, provides `generate_text` and `start_chat_session` |
| `config.py`        | Configuration Management | Loads `.env` and retrieves `GEMINI_API_KEY`                                     |
| `chat_buddy.py`    | Chat Agent               | Handles purely conversational mode with context retention                       |
| `study_guide.py`   | Teaching Agent           | Explains concepts, guides learning, asks/answers questions                      |
| `planner.py`       | Planning Agent           | Generates structured schedules                                                  |
| `.env`             | Secret Config            | Stores API key (**must not be committed to GitHub**)                            |

---

## 🚀 Quick Start

### **Requirements**

* Python 3.8+ (recommended: Python 3.13)
* A personal Gemini API Key

---

### **Step 1: Install Dependencies**

Run this in the same Python environment used for `main.py`:

```bash
python3 -m pip install python-dotenv google-genai
```

---

### **Step 2: Configure Your API Key (Important)**

run:

```
export GEMINI_API_KEY="AIzaSyAVLKQDkNd4B9w2nAuyEjsseM5L__9x6Es"
```

> Ensure `.gitignore` includes `.env`

---

### **Step 3: Run the Application**

Within the `study_buddy` directory, run:

```bash
python3 main.py
```

---

### **Step 4: Start Interacting**

In the CLI menu, type:

* `1` → Teaching Mode
* `2` → Planning Mode
* `3` → Chat Mode

---

## 🔮 Future Improvements

Upcoming possible enhancements include:

### 🔍 Google Search Tool Integration

Implement a Research Agent capable of performing live web searches for real-time information.

### 🧠 Long-Term Memory & User Preference Storage

Develop a Memory Manager to store:

* User goals
* Preferences
* Learning progress

### 🧩 Advanced Agent Framework

Upgrade the current architecture to frameworks like CrewAI or similar ADK to support:

* Complex multi-agent collaboration
* Task delegation
* Automated workflows
