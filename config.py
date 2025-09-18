from dotenv import load_dotenv
import os


load_dotenv()

FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")
if not FIREWORKS_API_KEY:
    raise RuntimeError("FIREWORKS_API_KEY not found in environment. Put it in .env")

# Fireworks model to use
FIREWORKS_MODEL = os.getenv(
    "FIREWORKS_MODEL",
    "accounts/fireworks/models/llama-v3p1-8b-instruct"
)

# Fireworks chat completions endpoint 
FIREWORKS_CHAT_URL = os.getenv(
    "FIREWORKS_CHAT_URL",
    "https://api.fireworks.ai/inference/v1/chat/completions"
)

# runtime / tuning defaults
DEFAULT_TEMPERATURE = float(os.getenv("FW_TEMPERATURE", "0.1"))
DEFAULT_MAX_TOKENS = int(os.getenv("FW_MAX_TOKENS", "400"))
