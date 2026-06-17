from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langgraph.prebuilt import create_react_agent
from config import MODELS, OPENROUTER_API_KEY, OPENROUTER_BASE_URL
from tools import get_order_by_id, get_orders_by_customer

SYSTEM_PROMPT = """
أنت متخصص في خدمة عملاء قسم الطلبات لمتجر إلكتروني.
بتساعد العملاء في:
- تتبع الطلبات ومعرفة حالتها
- الاستفسار عن مواعيد التسليم
- إلغاء الطلبات
- أي مشكلة متعلقة بالطلبات

تعامل مع العميل بأسلوب ودي واحترافي.
لو محتاج معلومات زي رقم الأوردر أو الإيميل، اطلبها من العميل.
"""

def get_order_agent():
    llm = ChatOpenAI(
        model=MODELS["order"],
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
        max_tokens=500
    )
    tools = [get_order_by_id, get_orders_by_customer]
    return create_react_agent(llm, tools, prompt=SYSTEM_PROMPT)