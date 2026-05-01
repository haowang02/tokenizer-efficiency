# Tokenizer Efficiency Evaluation

Evaluating token efficiency of different LLM tokenizers on English and Chinese text inputs.

## Test Data

| Name | Language |
|------|----------|
| The Little Prince | English |
| 阿Q正传 | Chinese |

## Results

| Model           | *The Little Prince* Tokens | vs GPT-5.5 | *阿Q正传* Tokens | vs GPT-5.5 | Total Tokens | Total vs GPT-5.5 |
| --------------- | -----------------------: | ---------: | --------------: | ---------: | -----------: | ---------------: |
| GPT-5.5<br />GPT-5.4 |                   22,676 |     100.0% |          24,341 |     100.0% |       47,017 |           100.0% |
| Qwen 3.6 Plus   |                   22,442 |      99.0% |          20,569 |      84.5% |       43,011 |            91.5% |
| MiMo v2.5 Pro   |                   22,791 |     100.5% |          21,486 |      88.3% |       44,277 |            94.2% |
