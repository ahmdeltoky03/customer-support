from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from graph.support_graph import support_graph
from config import PRODUCTS_PATH, ORDERS_PATH, CUSTOMERS_PATH

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Models ───────────────────────────────────────────────
class ChatRequest(BaseModel):
    message: str
    customer_id: str = ""

# ── Routes ───────────────────────────────────────────────
@app.post("/chat")
async def chat(req: ChatRequest):
    messages = [{"role": "user", "content": req.message}]
    result = support_graph.invoke({
        "messages":    messages,
        "category":    "",
        "response":    "",
    })
    return {
        "response": result["response"],
        "category": result["category"],
    }

@app.get("/products")
async def get_products():
    with open(PRODUCTS_PATH, encoding="utf-8") as f:
        return json.load(f)

@app.get("/orders")
async def get_orders():
    with open(ORDERS_PATH, encoding="utf-8") as f:
        return json.load(f)

@app.get("/customers")
async def get_customers():
    with open(CUSTOMERS_PATH, encoding="utf-8") as f:
        return json.load(f)

@app.get("/")
async def root():
    return {"status": "ok", "message": "Customer Support API is running"}