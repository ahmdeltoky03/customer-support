from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from config import MODELS, OPENROUTER_API_KEY, OPENROUTER_BASE_URL
from tools import search_products, get_product_by_id, check_stock

SYSTEM_PROMPT = """
أنت متخصص في خدمة عملاء قسم المنتجات لمتجر إلكتروني للملابس.
بتساعد العملاء في:
- البحث عن منتجات معينة
- معرفة الأسعار والمقاسات المتاحة
- التحقق من توفر المنتج
- مقارنة المنتجات

تعامل مع العميل بأسلوب ودي واحترافي.
"""

def get_product_agent():
    llm = ChatOpenAI(
        model=MODELS["product"],
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
        max_tokens=500
    )
    tools = [search_products, get_product_by_id, check_stock]
    return create_react_agent(llm, tools, prompt=SYSTEM_PROMPT)