# config.py
import os


# 載入 .env 檔案中的環境變數


# 從環境變數中獲取 API Key
# 建議您在終端機中設定：export GEMINI_API_KEY="YOUR_API_KEY"
GEMINI_API_KEY = "AIzaSyCRlfsLTMlkkslZ1c2tu8rKDvWP4LCvv6A"

if not GEMINI_API_KEY:
    print("錯誤：找不到 GEMINI_API_KEY。請確保已在環境變數或 .env 檔案中設定。")

# 這裡也可以定義其他配置，例如預設模型
DEFAULT_MODEL = "gemini-2.5-flash"