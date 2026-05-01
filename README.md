# Tokenizer Efficiency Evaluation

Evaluating token efficiency of different LLM tokenizers on English, Chinese, and Python code inputs.

## Test Data

| Name | Language | Description |
|------|----------|------|
| LP | English | *The Little Prince* by Antoine de Saint-Exupéry |
| AQ | Chinese | *阿Q正传* by 鲁迅 |
| PY | Python | [Flask](https://github.com/pallets/flask) source code |

## Results

- **LP**: *The Little Prince* (English)
- **AQ**: *阿Q正传* (Chinese)
- **PY**: Flask source code (Python)
- **%**: token count relative to GPT-5.5

| Model | LP tok | LP % | AQ tok | AQ % | PY tok | PY % | Total tok | Total % |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| minimax-m2.7 | 22,187 | 99% | 18,470 | 76% | 20,753 | 101% | 61,410 | 91% |
| kimi-k2.6 | 22,691 | 102% | 19,438 | 80% | 20,504 | 100% | 62,633 | 93% |
| glm-5.1 | 22,496 | 101% | 20,872 | 86% | 20,477 | 100% | 63,845 | 95% |
| grok-4.3 | 22,141 | 99% | 21,457 | 88% | 20,538 | 100% | 64,136 | 95% |
| deepseek-v4-pro | 22,685 | 102% | 19,826 | 81% | 21,734 | 106% | 64,245 | 96% |
| qwen3.6-plus | 22,442 | 100% | 20,569 | 85% | 21,846 | 106% | 64,857 | 96% |
| mimo-v2.5-pro | 22,791 | 102% | 21,486 | 88% | 20,766 | 101% | 65,043 | 97% |
| **gpt-5.5** (baseline) | 22,334 | 100% | 24,341 | 100% | 20,575 | 100% | 67,250 | 100% |
| gemini-3.1-pro-preview | 23,596 | 106% | 23,648 | 97% | 23,931 | 116% | 71,175 | 106% |
| claude-opus-4.6 | 24,367 | 109% | 32,987 | 136% | 24,852 | 121% | 82,206 | 122% |
| claude-opus-4.7 | 31,272 | 140% | 33,029 | 136% | 31,850 | 155% | 96,151 | 143% |
