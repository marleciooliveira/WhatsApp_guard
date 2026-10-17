import httpx

from .config import settings

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPT = (
    "Você é o M2SEC Guard, um assistente que ajuda pessoas leigas a se "
    "protegerem de golpes no WhatsApp. Responda em português, de forma "
    "simples e acolhedora."
)


async def ask_llm(user_text: str) -> str:
    headers = {"Authorization": f"Bearer {settings.groq_api_key}"}
    payload = {
        "model": settings.groq_model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text},
        ],
    }
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.post(GROQ_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
    return data["choices"][0]["message"]["content"]
