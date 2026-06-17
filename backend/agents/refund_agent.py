from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from config import MODELS, OPENROUTER_API_KEY, OPENROUTER_BASE_URL
from tools import get_order_by_id, get_orders_by_customer

SYSTEM_PROMPT = """
أنت متخصص في خدمة عملاء قسم المرتجعات والاسترداد لمتجر إلكتروني.
بتساعد العملاء في:
- طلبات إرجاع المنتجات
- الاستفسار عن حالة الاسترداد
- شرح سياسة الإرجاع (14 يوم من تاريخ الاستلام)
- حل مشاكل المرتجعات

تعامل مع العميل بأسلوب ودي ومتفهم.
"""

def get_refund_agent():
    llm = ChatOpenAI(
        model=MODELS["refund"],
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
        max_tokens=500
    )
    tools = [get_order_by_id, get_orders_by_customer]
    return create_react_agent(llm, tools, prompt=SYSTEM_PROMPT)