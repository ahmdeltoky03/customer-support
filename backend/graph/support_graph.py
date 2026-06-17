from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from agents.classifier import classify
from agents.order_agent import get_order_agent
from agents.product_agent import get_product_agent
from agents.refund_agent import get_refund_agent
from agents.general_agent import get_general_agent

# ── State ────────────────────────────────────────────────
class SupportState(TypedDict):
    messages: List[dict]
    category: str
    response: str

# ── Nodes ────────────────────────────────────────────────
def classifier_node(state: SupportState) -> SupportState:
    last_message = state["messages"][-1]["content"]
    category = classify(last_message)
    return {**state, "category": category}

def order_node(state: SupportState) -> SupportState:
    agent = get_order_agent()
    result = agent.invoke({"messages": state["messages"]})
    response = result["messages"][-1].content
    return {**state, "response": response}

def product_node(state: SupportState) -> SupportState:
    agent = get_product_agent()
    result = agent.invoke({"messages": state["messages"]})
    response = result["messages"][-1].content
    return {**state, "response": response}

def refund_node(state: SupportState) -> SupportState:
    agent = get_refund_agent()
    result = agent.invoke({"messages": state["messages"]})
    response = result["messages"][-1].content
    return {**state, "response": response}

def general_node(state: SupportState) -> SupportState:
    agent = get_general_agent()
    result = agent.invoke({"messages": state["messages"]})
    response = result["messages"][-1].content
    return {**state, "response": response}

# ── Router ───────────────────────────────────────────────
def route(state: SupportState) -> str:
    return state["category"]

# ── Build Graph ──────────────────────────────────────────
def build_graph():
    graph = StateGraph(SupportState)

    graph.add_node("classifier", classifier_node)
    graph.add_node("order",      order_node)
    graph.add_node("product",    product_node)
    graph.add_node("refund",     refund_node)
    graph.add_node("general",    general_node)

    graph.set_entry_point("classifier")

    graph.add_conditional_edges("classifier", route, {
        "order":   "order",
        "product": "product",
        "refund":  "refund",
        "general": "general",
    })

    graph.add_edge("order",   END)
    graph.add_edge("product", END)
    graph.add_edge("refund",  END)
    graph.add_edge("general", END)

    return graph.compile()

support_graph = build_graph()