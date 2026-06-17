import json
from langchain_core.tools import tool
from config import PRODUCTS_PATH, ORDERS_PATH, CUSTOMERS_PATH

# ── load data ──────────────────────────────────────────
def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

# ── Product Tools ───────────────────────────────────────
@tool
def search_products(query: str = "", category: str = "", max_price: float = 0) -> str:
    """Search products by name, category, or max price."""
    products = _load(PRODUCTS_PATH)
    results = []
    for p in products:
        if query and query.lower() not in p["name"].lower() and query.lower() not in p["description"].lower():
            continue
        if category and category.lower() not in p["category"].lower():
            continue
        if max_price and p["price"] > max_price:
            continue
        results.append(p)
    return json.dumps(results, ensure_ascii=False) if results else "مفيش منتجات بالمواصفات دي"

@tool
def get_product_by_id(product_id: str) -> str:
    """Get a single product by its ID."""
    products = _load(PRODUCTS_PATH)
    for p in products:
        if p["id"] == product_id:
            return json.dumps(p, ensure_ascii=False)
    return "المنتج مش موجود"

@tool
def check_stock(product_id: str, size: str = "") -> str:
    """Check if a product is in stock, optionally for a specific size."""
    products = _load(PRODUCTS_PATH)
    for p in products:
        if p["id"] == product_id:
            if size and size not in p["sizes"]:
                return f"المقاس {size} مش متاح، المقاسات المتاحة: {p['sizes']}"
            return f"المنتج متاح، الكمية: {p['stock']}"
    return "المنتج مش موجود"

# ── Order Tools ─────────────────────────────────────────
@tool
def get_order_by_id(order_id: str) -> str:
    """Get order details by order ID."""
    orders = _load(ORDERS_PATH)
    for o in orders:
        if o["id"] == order_id:
            return json.dumps(o, ensure_ascii=False)
    return "الأوردر مش موجود"

@tool
def get_orders_by_customer(customer_id: str) -> str:
    """Get all orders for a specific customer."""
    orders = _load(ORDERS_PATH)
    results = [o for o in orders if o["customer_id"] == customer_id]
    return json.dumps(results, ensure_ascii=False) if results else "مفيش أوردرات للعميل ده"

# ── Customer Tools ──────────────────────────────────────
@tool
def get_customer_by_email(email: str) -> str:
    """Get customer details by email."""
    customers = _load(CUSTOMERS_PATH)
    for c in customers:
        if c["email"] == email:
            return json.dumps(c, ensure_ascii=False)
    return "العميل مش موجود"