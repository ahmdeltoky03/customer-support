from langchain_openai import ChatOpenAI
from config import MODELS, OPENROUTER_API_KEY, OPENROUTER_BASE_URL

def get_classifier_llm():
    return ChatOpenAI(
        model=MODELS["classifier"],
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
        max_tokens=500
    )

CLASSIFIER_PROMPT = """
أنت نظام تصنيف لخدمة عملاء متجر إلكتروني.
مهمتك تحديد نوع رسالة العميل وترجع واحدة من الكلمات دي بس:

- order    → أي سؤال عن أوردر، شحن، تتبع، كنسلة
- product  → أي سؤال عن منتج، سعر، مقاس، توفر
- refund   → أي سؤال عن مرتجع أو استرداد فلوس
- general  → أي سؤال تاني

رد بكلمة واحدة بس من الأربع دول.
"""

def classify(message: str) -> str:
    llm = get_classifier_llm()
    response = llm.invoke([
        {"role": "system", "content": CLASSIFIER_PROMPT},
        {"role": "user", "content": message}
    ])
    category = response.content.strip().lower()
    if category not in ["order", "product", "refund", "general"]:
        return "general"
    return category