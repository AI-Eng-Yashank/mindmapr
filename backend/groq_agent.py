import os
import httpx
from dotenv import load_dotenv
import json
import re
from schemas.mindmap import MindMapResponse

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def call_groq_llm(text: str) -> MindMapResponse:
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    # Stronger system prompt to force JSON
    system_prompt = """
You are a JSON-only API.
Extract a mind map from user input. Return ONLY raw JSON in this format:
{
  "concepts": ["AI", "Machine learning"],
  "relations": [["AI", "helps", "automate tasks"]]
}
Do NOT include explanations, quotes, markdown, or anything else.
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Text: {text}"}
    ]

    payload = {
        "model": "deepseek-r1-distill-llama-70b",  # Or use mixtral-8x7b-32768 for better structure
        "messages": messages,
        "temperature": 0.3
    }

    response = httpx.post(url, headers=headers, json=payload, timeout=30.0)

    if response.status_code != 200:
        print("[ERROR] Groq API call failed:", response.status_code, response.text)
        return MindMapResponse(nodes=[], edges=[])

    try:
        content = response.json()["choices"][0]["message"]["content"]
        print("\n[DEBUG] Raw Groq Response:\n", content)

        # Try direct JSON parsing
        parsed = json.loads(content)

    except json.JSONDecodeError:
        print("[WARN] Failed to parse directly. Trying regex fallback...")

        match = re.search(r'\{[\s\S]*?\}', content)
        if match:
            try:
                parsed = json.loads(match.group(0))
            except Exception as e:
                print("[ERROR] Still failed after regex extraction:", e)
                return MindMapResponse(nodes=[], edges=[])
        else:
            print("[ERROR] No JSON found in Groq response.")
            return MindMapResponse(nodes=[], edges=[])

    # Build response
    nodes = [{"id": c} for c in set(parsed.get("concepts", []))]
    edges = [{"source": s, "target": t, "label": r} for s, r, t in parsed.get("relations", [])]
    return MindMapResponse(nodes=nodes, edges=edges)