# Tokenizer Efficiency Evaluation

Evaluating token efficiency of different LLM tokenizers on English and Chinese text inputs.

## Test Data

| Name | Language | Description |
|------|----------|------|
| LP | English | *The Little Prince* by Antoine de Saint-Exupéry |
| AQ | Chinese | *阿Q正传* by 鲁迅 |

## Results

- **LP**: *The Little Prince* (English)
- **AQ**: *阿Q正传* (Chinese)
- **%**: token count relative to GPT-5.5 / GPT-5.4

| Model | LP Tokens | LP % | AQ Tokens | AQ % | Total | Total % |
| --------------- | -----------------------: | ---------: | --------------: | ---------: | -----------: | ---------------: |
| MiniMax M2.7    |                   22,190 |      97.9% |          18,471 |      75.9% |       40,661 |            86.5% |
| Kimi K2.6       |                   22,691 |     100.1% |          19,438 |      79.9% |       42,129 |            89.6% |
| DeepSeek V4 Pro<br />DeepSeek V4 Flash |                   22,685 |     100.0% |          19,826 |      81.4% |       42,511 |            90.4% |
| GLM 5.1         |                   22,496 |      99.2% |          20,872 |      85.8% |       43,368 |            92.2% |
| Qwen 3.6 Plus   |                   22,442 |      99.0% |          20,569 |      84.5% |       43,011 |            91.5% |
| MiMo v2.5 Pro   |                   22,791 |     100.5% |          21,486 |      88.3% |       44,277 |            94.2% |
| GPT-5.5<br />GPT-5.4 |                   22,676 |     100.0% |          24,341 |     100.0% |       47,017 |           100.0% |
| Claude Opus 4.6 |                   24,367 |     107.5% |          32,987 |     135.5% |       57,354 |           122.0% |
| Claude Opus 4.7 |                   31,272 |     137.9% |          33,029 |     135.7% |       64,301 |           136.8% |
