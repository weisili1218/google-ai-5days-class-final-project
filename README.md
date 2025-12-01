# 🤖 AI Learning Partner - Multi-Agent Study Companion

**專案狀態：** 運行中 (CLI Interface) | **底層模型：** Google Gemini (via `google-genai` SDK)

一個專業、長期的學習助手，超越簡單聊天機器人的功能。本系統採用模組化、Agentic 的設計方法，提供專業的幫助，涵蓋研究、時間規劃、科目輔導和長期記憶管理。

---

## ✨ 核心功能與技術亮點 (Key Features & Techniques)

這個專案展示了如何使用 Google Gemini SDK 實現複雜的 Agentic AI 能力。

### 1. 多 Agent 選擇與路由 🎛️
系統的核心控制層根據用戶的選擇，將查詢精準地路由到具備專業技能的 Agent，確保查詢由最佳的專業 Agent 處理，提供更準確的幫助。
* **機制:** 透過 CLI 介面選擇不同的 Agent 模式：
    * `1` / `2` / `3` / `4` → 選擇專業 Agent (例如：Researcher, Planner, Tutor, Assistant)。

### 2. 基於 AI 整合的長期記憶 🧠
您的學習偏好和目標將跨越會話持久化儲存 (`user_memory.json`)。
* **技術: AI 輔助記憶整合 (AI-Powered Consolidation)。**
* **運作方式:** 當有新資訊（例如改變學習目標）與現有記憶發生衝突時，一個背景 LLM 流程會啟動，負責合併重複項、刪除過時資料，並以**語義化**的方式保持用戶資料的一致性。

### 3. 上下文感知會話持久性 💬
完整的聊天記錄會儲存在本地 (`chat_sessions.json`)。
* **技術: 會話持久化 (Session Persistence)。**
* **運作方式:** 您可以隨時關閉應用程式，並從上次離開的地方精確恢復對話。回訪用戶會自動獲得上次進度的摘要。

### 4. 進階函式呼叫 (Tools) 🛠️
Agent 可以呼叫外部工具和 API 來執行實際任務，提高實用性和準確性：
* **時間規劃與提醒:** 系統採用嚴格的 **「先列舉再行動」(List-then-Action SOP)** 設計，要求先列出準確 ID 後再進行修改或刪除。這項設計是為了防止 LLM 幻覺導致錯誤地操作資料庫。
* **媒體與資源:** Agent 可以在建議複雜主題時，檢索高品質的影片或文章連結，作為用戶的學習指引。

---

## 🏗️ 專案架構 (Project Architecture)

本專案採用模組化設計，以便於擴展和維護，將職責清晰地分離到不同的 Python 檔案中。

| 檔案/模組 | 職責 | 關鍵功能 |
| :--- | :--- | :--- |
| **`main.py`** | **Orchestrator** | 協調聊天循環、管理 LLM 生命週期、將記憶上下文注入 System Instructions。 |
| **`tools.py`** | **函式層 (Tools)** | 包含外部 API (如排程、媒體查找) 和時間日期的工具函數封裝。 |
| **`memory_manager.py`**| **長期記憶邏輯** | 處理 `user_memory.json`。核心 `consolidate_memory_with_llm` 函數通過一個二次 AI 呼叫來清理和組織用戶數據。 |
| **`session_manager.py`**| **會話管理** | 負責讀取和寫入原始聊天記錄 (`chat_sessions.json`)。 |
| **`data/`** | **本地儲存** | 儲存 JSON 數據庫 (`user_memory.json`, `chat_sessions.json`)。 |

---

## 🚀 快速開始 (Quick Start)

### 前置要求

* Python 3.8+
* 您個人的 **Gemini API Key** (可從 Google AI Studio 獲取)。

### 步驟 1: 克隆儲存庫並安裝依賴

```bash
# 假設您已將程式碼上傳到 GitHub
git clone [您的儲存庫 URL]
cd [您的專案目錄，例如 study_buddy]

# 安裝必要的函式庫
pip install google-genai python-dotenv
