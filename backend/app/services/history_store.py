from datetime import datetime

query_history = []

# Add to history
def add_to_history(question: str, response: str):
    query_history.append({"question": question, "response": response, "timestamp": datetime.utcnow().isoformat()})

# Fetch history entries
def get_history():
    return query_history[-20:]  # limit to last 20 entries
