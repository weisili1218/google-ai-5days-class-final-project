# chat_buddy.py
from gemini_client import gemini_api

CHAT_BUDDY_SYSTEM_INSTRUCTION = (
    "你是一位友善、熱情且具有好奇心的全能聊天夥伴。使用者用任何語言問你你就用那個語言回應他，他用英文問你你就用英文回應他"
    "保持簡潔和生活化的語氣與使用者交流。你可以聊任何話題，但請保持樂觀和正向的態度。"
    "在每句回覆的結尾，可以加上一個相關的表情符號。"
)

def run_chat_session():
    """
    啟動並運行一個持久化的純聊天會話。
    """
    print("---")
    print("hello nice to see you ,let's start our new chat!!!")
    print("write 'exit' or 'quit' to end the chat")
    print("---")
    
    # 1. 啟動一個帶有角色設定的聊天會話
    chat_session = gemini_api.start_chat_session(
        system_instruction=CHAT_BUDDY_SYSTEM_INSTRUCTION
    )
    
    if not chat_session:
        return

    while True:
        user_input = input("you: ").strip()
        
        # 退出指令
        if user_input.lower() in ['exit', 'quit']:
            print("\n👋 hope to see u again！")
            break
            
        if not user_input:
            continue

        try:
            # 2. 發送訊息並取得回應（模型會自動記住上下文）
            response = chat_session.send_message(user_input)
            
            # 3. 輸出模型的文字回應
            print(f"AI: {response.text}")
            
        except Exception as e:
            print(f"❌ sorry theres some mistake： {e}")
            break