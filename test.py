import argparse
import json
import os
import urllib.request

API_KEY = os.environ["OPENROUTER_API_KEY"]
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

ALL_FILES = [
    "lp_en.txt",
    "aq_zh.txt",
    "py.txt",
]

# GPT-5.5 baseline prompt_tokens
BASELINE = {
    "lp_en.txt": 22334,
    "aq_zh.txt": 24341,
    "py.txt": 20575,
}


def call_model(model, content):
    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "max_completion_tokens": 16,
    }).encode()
    req = urllib.request.Request(
        BASE_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  ERROR {e.code}: {body[:200]}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Test tokenizer efficiency across LLM models.")
    parser.add_argument("models", nargs="+", help="Model IDs to test")
    parser.add_argument("-d", "--data", nargs="+", choices=ALL_FILES, default=ALL_FILES,
                        help="Datasets to test (default: all)")
    args = parser.parse_args()

    for model in args.models:
        print(f"\n=== {model} ===")
        tokens = {}
        for fname in args.data:
            path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", fname)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            data = call_model(model, content)
            if data is None:
                continue
            usage = data["usage"]
            tokens[fname] = usage["prompt_tokens"]
            pct = usage["prompt_tokens"] / BASELINE[fname] * 100
            print(f"{fname}: prompt_tokens={usage['prompt_tokens']}, {pct:.1f}%")

        total = sum(tokens.values())
        total_baseline = sum(BASELINE[f] for f in tokens)
        print(f"total: {total}, {total / total_baseline * 100:.1f}%")


if __name__ == "__main__":
    main()
