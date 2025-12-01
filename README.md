# 🤖 AI Learning Partner - Multi-Agent Study Companion

**Project Status:** Functional (CLI Interface) | **Underlying Model:** Google Gemini (via `google-genai` SDK)

A professional, modular AI learning system designed for focused study and time management. It utilizes a multi-Agent architecture and **Session Persistence** powered by Google Gemini, providing seamless and highly contextualized learning assistance.

---

## ✨ Key Features & Techniques

This project demonstrates advanced Agentic AI capabilities leveraging the Google Gen AI SDK.

### 1. Multi-Agent Selection & Routing 🎛️
The system's central orchestration layer routes queries based on user selection, ensuring that each request is handled by the Agent with the optimal expertise for accurate results.
* **Mechanism:** Users select the desired Agent mode via the CLI:
    * `1` / `2` / `3` / `4` → Select a specialized Agent (e.g., Researcher, Planner, Tutor, Assistant).

### 2. Context-Aware Session Persistence 💬
Your conversation history is saved locally (`chat_sessions.json`) to maintain dialogue flow.
* **Technique: Session Persistence.**
* **How it works:** Users can close the application and resume their conversation exactly where they left off. Returning users are automatically greeted with a summary of their previous progress, immediately restoring conversational context.

### 3. Advanced Function Calling (Tools) 🛠️
Agents can call external tools and APIs to execute real-world tasks, enhancing utility and accuracy:
* **Scheduling & Reminders:** Integrations are designed with a strict **"List-then-Action" SOP** (Standard Operating Procedure). This design is crucial for preventing LLM hallucinations from modifying the wrong database entry, ensuring reliable, high-integrity scheduling operations.
* **Media & Resources:** Agents can retrieve high-quality video or article references to guide user learning when suggesting complex topics.

---

## 🏗️ Project Architecture

The project uses a modular design for scalability and maintainability, with responsibilities clearly separated into dedicated Python files.

| Module | Role | Key Functionality |
| :--- | :--- | :--- |
| **`main.py`** | **Orchestrator** | Manages the main chat loop, handles user routing, injects historical session context into Agent System Instructions, and controls the LLM lifecycle. |
| **`tools.py`** | **Functional Layer (Tools)** | Contains wrapper functions for external APIs (e.g., Scheduling, Media lookup) and date-time utilities. |
| **`session_manager.py`**| **Session Logic** | Dedicated logic for reading and writing the raw chat history (`chat_sessions.json`). |
| **`data/`** | **Local Storage** | Stores the local JSON database (`chat_sessions.json`). |

---

## 🚀 Quick Start

### Prerequisites

* Python 3.8+
* Your personal **Gemini API Key** (obtainable from Google AI Studio).

### Step 1: Clone Repository and Install Dependencies

```bash
git clone [YOUR_REPOSITORY_URL_HERE]
cd [YOUR_PROJECT_DIRECTORY]

# Install required libraries
pip install google-genai python-dotenv
