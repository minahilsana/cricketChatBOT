import requests
import json
import logging
import config
from prompts import SYSTEM_PROMPT

logger = logging.getLogger("cricket-chatbot")

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {config.FIREWORKS_API_KEY}"
}

def get_cricket_answer(question: str) -> str:
    """Send user question to Fireworks API and return the model's answer text."""
    payload = {
        "model": config.FIREWORKS_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        "temperature": config.DEFAULT_TEMPERATURE,
        "max_tokens": config.DEFAULT_MAX_TOKENS,
    }

    try:
        resp = requests.post(
            config.FIREWORKS_CHAT_URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.exception("Fireworks API request failed")
        return "Error: Failed to connect to the model."

    try:
        data = resp.json()
        # Validating the response structure before accessing it
        if (
            "choices" in data
            and isinstance(data["choices"], list)
            and len(data["choices"]) > 0
            and "message" in data["choices"][0]
            and "content" in data["choices"][0]["message"]
        ):
            return data["choices"][0]["message"]["content"].strip()
        else:
            logger.error("Unexpected response format: %s", data)
            return "Error: Invalid response from model."
    except json.JSONDecodeError:
        logger.exception("Response was not valid JSON")
        return "Error: Invalid response from model."
