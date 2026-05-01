import json
import os
import sys
import urllib.request

API_KEY = os.environ["OPENROUTER_API_KEY"]
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

files = [
    "lp_en.txt",
    "aq_zh.txt",
]


def call_model(model, content):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "max_completion_tokens": 1,
    }).encode()
    req = urllib.request.Request(
        BASE_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <model_id> [model_id ...]")
        sys.exit(1)
    models = sys.argv[1:]

    for model in models:
        print(f"\n=== {model} ===")
        for fname in files:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", fname)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            data = call_model(model, content)
            usage = data["usage"]
            print(f"{fname}: prompt_tokens={usage['prompt_tokens']}, completion_tokens={usage['completion_tokens']}, total_tokens={usage['total_tokens']}")


if __name__ == "__main__":
    main()
