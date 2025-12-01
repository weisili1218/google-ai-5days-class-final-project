# 🤖 AI Learning Partner - Multi-Agent Study Companion

**Project Status:** Functional (CLI Interface) | **Underlying Model:** Google Gemini (via `google-genai` SDK)

A professional, modular AI learning system designed for focused study and time management. It utilizes a **simulated Multi-Agent architecture** with dedicated Python modules and Session Persistence, all powered by **Google Gemini**.

---

## ✨ Core Features & Techniques

This project demonstrates Agentic capabilities achieved through highly specialized Python module functions, leveraging the Google Gen AI SDK.

### 1. Agent Specialization & Routing 🎛️
The system manages distinct modes via the main program (`main.py`) interface, routing user choices to the appropriate specialized Agent module.
* **Mechanism:** CLI options allow the user to select the specialized mode (Tutoring, Planning, or Chat).
* **Division of Labor:** Each Agent module uses a unique **System Instruction** to set its role (e.g., a "Strict Planner" or a "Patient Tutor"), ensuring consistent and high-quality output for its specific task.

### 2. Context-Aware Session Persistence 💬
The current dialogue history is maintained to ensure conversational flow and coherence.
* **Technique: Session Persistence.**
* **How it works:** The Chat mode (`chat_buddy.py`) utilizes the dedicated **Gemini API Chat Session** feature to maintain continuous memory, allowing the AI to recall previous turns within the current conversation.

### 3. Functional Tool Utilization 🛠️
Agents execute complex tasks by calling structured Python functions.
* **API Layer:** The shared `gemini_client.py` module handles all API connection and communication, acting as the bridge for all Agent functions.
* **Planning Functionality:** The `planner.py` module employs a dedicated Planner System Instruction to generate organized and optimized schedules.

---

## 🏗️ Project Architecture

The project adopts a modular design, with responsibilities clearly separated across Python files for maintainability and clarity.

| File / Module | Role | Key Functionality |
| :--- | :--- | :--- |
| **`main.py`** | **Orchestrator** | Program entry point; manages the CLI, and routes user selection to the correct Agent module. |
| **`gemini_client.py`** | **API Client** | Handles all connectivity and communication with the Gemini API (`generate_text`, `start_chat_session`). |
| **`config.py`** | **Configuration** | Responsible for loading the `.env` file and retrieving the `GEMINI_API_KEY`. |
| **`chat_buddy.py`** | **Chat Agent** | Implements the free-form conversation logic using the dedicated `Chat Session`. |
| **`study_guide.py`** | **Tutoring Agent** | Implements the educational function, setting a Tutor System Instruction for concept explanation and quizzing. |
| **`planner.py`** | **Planning Agent** | Implements the time management function, setting a Planner System Instruction to generate structured schedules. |
| **`.env`** | **Private Config** | Stores the `GEMINI_API_KEY` (MUST NOT be uploaded to GitHub). |

---

## 🚀 Quick Start

### Prerequisites

* Python 3.8+ (The system was developed and tested using Python 3.13)
* Your personal **Gemini API Key**.

### Step 1: Install Dependencies

Ensure you use the **same Python environment** for installation as you use for execution:

```bash
# Install required libraries
python3 -m pip install python-dotenv google-genai
