# main.py

from planner import create_schedule
from study_guide import explain_concept
from gemini_client import gemini_api # 確保客戶端已初始化
from chat_buddy import run_chat_session

def run_ai_buddy():
    """主程式運行函數。"""
    
    # 程式啟動時，確認 API 客戶端是否成功初始化
    if not gemini_api.client:
        print("\n🚫 error")
        return

    
    while True:
        print("\nchoose what do you want to do：")
        print("1. plan your time (ex：Could you help me schedule 8 hours of study for tomorrow?)")
        print("2. learn some new things (ex：Explain what quantum entanglement is)")
        print("3. just chat")
        print("4. ❌ exit")
        
        choice = input("please answer your choice (1/2/3/4): ").strip()

        if choice == '1':
            task = input("請輸入您希望規劃的任務和時間範圍：\n> ")
            result = create_schedule(task)
            print("\n" + "="*50)
            print(result)
            print("="*50 + "\n")
        
        elif choice == '2':
            concept = input("請輸入您想學習或提問的概念：\n> ")
            result = explain_concept(concept)
            print("\n" + "="*50)
            print(result)
            print("="*50 + "\n")

        elif choice == "3":
            run_chat_session()
            
        elif choice == '4':
            print("bye~ hope to see you soon 👋")
            break
            
        else:
            print("輸入無效，請重新選擇。")

if __name__ == "__main__":
    run_ai_buddy()