#!/usr/bin/env python3
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_FILE = os.path.join(SCRIPT_DIR, "results.jsonl")
README_FILE = os.path.join(SCRIPT_DIR, "README.md")


def main():
    rows = []
    baseline = {}
    with open(RESULTS_FILE) as f:
        for line in f:
            r = json.loads(line)
            rows.append(r)
            if r["model"] == "openai/gpt-5.5":
                baseline = r

    for r in rows:
        r["total"] = r["lp_en.txt"] + r["aq_zh.txt"] + r["py.txt"]

    baseline_total = baseline["total"]

    rows.sort(key=lambda x: x["total"])

    lines = [
        "| Model | LP tok | LP % | AQ tok | AQ % | PY tok | PY % | Total tok | Total % |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for r in rows:
        name = r["model"].split("/", 1)[1]
        lp = r["lp_en.txt"]
        aq = r["aq_zh.txt"]
        py = r["py.txt"]
        total = r["total"]
        lp_pct = round(lp / baseline["lp_en.txt"] * 100)
        aq_pct = round(aq / baseline["aq_zh.txt"] * 100)
        py_pct = round(py / baseline["py.txt"] * 100)
        total_pct = round(total / baseline_total * 100)

        is_baseline = r["model"] == "openai/gpt-5.5"
        if is_baseline:
            name = f"**{name}** (baseline)"

        lines.append(f"| {name} | {lp:,} | {lp_pct}% | {aq:,} | {aq_pct}% | {py:,} | {py_pct}% | {total:,} | {total_pct}% |")

    table = "\n".join(lines)

    with open(README_FILE) as f:
        content = f.read()

    # Find and replace the table (from the first "| Model |" line to the last "| ..." line)
    start = content.index("| Model |")
    end = start
    for i in range(start, len(content)):
        if content[i] == "\n" and (i + 1 >= len(content) or content[i + 1] != "|"):
            end = i
            break
    else:
        end = len(content)

    new_content = content[:start] + table + content[end:]
    with open(README_FILE, "w") as f:
        f.write(new_content)

    print(table)


if __name__ == "__main__":
    main()
