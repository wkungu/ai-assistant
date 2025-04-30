import asyncio
import httpx
from app.core.config import settings
from httpx import ReadTimeout
from app.services.history_store import add_to_history

import traceback

API_KEY = settings.OPENAI_API_KEY
ENDPOINT = "https://api.openai.com/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Engineer the prompt
SYSTEM_PROMPT = (
    "You are a highly knowledgeable and practical AI assistant specialized in advising small businesses and entrepreneurs. "
    "Your role is to offer clear, actionable, and insightful advice on a wide range of business topics including: \n\n"
    "- Business planning and idea validation\n"
    "- Market research and competitor analysis\n"
    "- Marketing strategies (digital, social media, local outreach)\n"
    "- Sales tactics and customer engagement\n"
    "- Financial planning, budgeting, and funding options\n"
    "- Legal and regulatory compliance for small businesses\n"
    "- Operations, hiring, and team building\n"
    "- Tools and technologies for small business efficiency\n\n"
    "When responding:\n"
    "- Break down advice into steps or bullet points.\n"
    "- Keep explanations simple and jargon-free unless requested otherwise.\n"
    "- Use real-world examples where helpful.\n"
    "- Be encouraging, solution-focused, and honest about challenges.\n"
    "- Assume the user may be new to business, unless context says otherwise.\n"
)

# Generate the responses
async def generate_ai_response(user_question: str) -> str:
    payload = {
        "model": "gpt-3.5-turbo",  # You can switch to gpt-4 if available on your plan
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_question}
        ],
        "temperature": 0.7
    }

    retries = 3 # Number of times to try hitting the API
    
    # Set timeout
    timeout = httpx.Timeout(30.0, connect=10.0)  # 30s total, 10s to connect
    
    for attempt in range(retries):
        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.post(ENDPOINT, headers=HEADERS, json=payload)

                response.raise_for_status()
                result = response.json()
                add_to_history(user_question, result["choices"][0]["message"]["content"])
                return result["choices"][0]["message"]["content"]

        except httpx.HTTPStatusError as e:
            # Print error in case it fails
            print(f"[HTTP Error] {e.response.status_code} - {e.response.text}")
            
            # If the issue is too many tries, try 3 more times before failing
            if e.response.status_code == 429 and attempt < retries - 1:
                wait_time = 2 ** attempt
                print(f"[Rate Limit] Retrying in {wait_time} seconds...")
                await asyncio.sleep(wait_time)
            # If the issue is timing out retry after 2 more seconds before failing
            elif isinstance(e, ReadTimeout) and attempt < retries - 1:
                print(f"[Timeout] Retrying in 2 seconds...")
                await asyncio.sleep(2)
            else:
                raise

        except Exception as e:
            print(f"[Unexpected Error] {e}")
            traceback.print_exc()
            raise
