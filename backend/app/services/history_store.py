query_history = []

def add_to_history(question: str, response: str):
    query_history.append({"question": question, "response": response})

def get_history():
    return query_history[-20:]  # limit to last 20 entries
