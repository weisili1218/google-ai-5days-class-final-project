# gemini_client.py
from google import genai
from config import GEMINI_API_KEY, DEFAULT_MODEL

class GeminiClient:
    """處理所有與 Gemini API 互動的類別。"""
    
    def __init__(self, model_name=DEFAULT_MODEL):
        try:
            # 1. 初始化 Client：使用配置中的 API Key
            self.client = genai.Client(api_key=GEMINI_API_KEY)
            self.model = model_name
        except Exception as e:
            print(f"❌error {e}")
            self.client = None

    def generate_text(self, prompt: str, system_instruction: str = None) -> str:
        """
        發送提示給 Gemini 模型，並返回生成的文字。
        
        Args:
            prompt: 使用者輸入或任務指令。
            system_instruction: 給模型的行為準則（讓模型扮演特定角色）。
        
        Returns:
            模型的文字回應。
        """
        if not self.client:
            return "error"

        # 2. 建立 API 呼叫的配置
        config = None
        if system_instruction:
            config = genai.types.GenerateContentConfig(
                system_instruction=system_instruction
            )
            
        try:
            # 3. 呼叫 API
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=config
            )
            return response.text
        except Exception as e:
            return f"❌ error: {e}"
        
        # study_buddy/gemini_client.py

# ... (保留原有的 import 和 GeminiClient 類別的 __init__ 和 generate_text 方法) ...

    # --- 新增：純聊天功能所需的對話管理 ---
    def start_chat_session(self, system_instruction: str = None):
        """
        開始一個新的對話連線 (Chat Session)。
        這允許模型記住之前的對話內容。
        """
        if not self.client:
            print("some thing went wrong")
            return None
            
        config = None
        if system_instruction:
            config = genai.types.GenerateContentConfig(
                system_instruction=system_instruction
            )
            
        # 使用 client.chats 建立對話實例
        chat_session = self.client.chats.create(
            model=self.model,
            config=config,
        )
        print("✅ new session is creat")
        return chat_session


# 實例化一次，供其他模組使用
gemini_api = GeminiClient()