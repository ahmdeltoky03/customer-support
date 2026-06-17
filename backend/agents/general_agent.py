from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from config import MODELS, OPENROUTER_API_KEY, OPENROUTER_BASE_URL

SYSTEM_PROMPT = """
أنت موظف خدمة عملاء لمتجر إلكتروني للملابس.
بتساعد العملاء في أي استفسار عام زي:
- ساعات العمل والتواصل
- طرق الدفع المتاحة
- مناطق التوصيل
- أي سؤال تاني

تعامل مع العميل بأسلوب ودي واحترافي.
"""

def get_general_agent():
    llm = ChatOpenAI(
        model=MODELS["general"],
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
        max_tokens=500
    )
    return create_react_agent(llm, [], prompt=SYSTEM_PROMPT)