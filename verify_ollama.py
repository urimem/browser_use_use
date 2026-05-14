import sys

import httpx
from ollama import ResponseError, chat

MODEL = "gemma2:2b" # "qwen3-vl:8b"
PROMPT = "What is the capital of France? Answer in one short sentence."


def main() -> int:
    try:
        response = chat(
            model=MODEL,
            messages=[{"role": "user", "content": PROMPT}],
        )
    except httpx.ConnectError as e:
        print(f"[FAIL] Cannot reach Ollama at http://localhost:11434 — is `ollama serve` running?\n       {e}")
        return 1
    except ResponseError as e:
        print(f"[FAIL] Ollama responded with an error (status {e.status_code}): {e.error}")
        return 1

    print(f"[OK]   model={MODEL}")
    print(f"[Q]    {PROMPT}")
    print(f"[A]    {response.message.content}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
