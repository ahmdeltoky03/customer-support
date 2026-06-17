from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Models config - سهل تغيرهم
MODELS = {
    "classifier": "openai/gpt-4o-mini",
    "order":      "anthropic/claude-sonnet-4-6",
    "product":    "openai/gpt-4o-mini",
    "refund":     "anthropic/claude-sonnet-4-6",
    "general":    "openai/gpt-4o-mini",
}

# Data paths
BASE_DIR = os.path.dirname(__file__)
PRODUCTS_PATH  = os.path.join(BASE_DIR, "data/mock_products.json")
ORDERS_PATH    = os.path.join(BASE_DIR, "data/mock_orders.json")
CUSTOMERS_PATH = os.path.join(BASE_DIR, "data/mock_customers.json")