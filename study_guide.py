# study_guide.py
from gemini_client import gemini_api

STUDY_BUDDY_SYSTEM_INSTRUCTION = (
    "你是一位耐心、鼓勵人心、且知識淵博的學習夥伴和家教。使用者用任何語言問你你就用那個語言回應他，他用英文問你你就用英文回應他"
    "以清晰、簡潔的方式解釋複雜的概念，並在解釋完畢後，提出一個小問題來確認使用者是否理解。"
)

def explain_concept(concept: str) -> str:
    """
    呼叫 Gemini 模型來解釋一個概念並提供小測驗。
    """
    prompt = f"請以學習夥伴的身份，為我解釋以下概念：【{concept}】"
    
    print(f"🧠 thinking longer for the better answer...")
    
    # 呼叫 Step Two 中定義的通用函式，並傳入學習夥伴的角色設定
    response = gemini_api.generate_text(
        prompt=prompt, 
        system_instruction=STUDY_BUDDY_SYSTEM_INSTRUCTION
    )
    return response