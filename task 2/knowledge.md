# Knowledge

**Project:** Bias in LLM financial sentiment analysis  
**Student:** Lukas Egger  
**Course:** Gender, Diversity & AI, SS2026

## Domain

The project is about finance and AI. Large language models can be used to read company texts, for example earnings call excerpts or corporate reports. They can give a sentiment score that may be used as a trading or risk signal.

The main question is:

Do LLMs rate the same financial statement differently when the speaker has a different gender or specific origin marker?

## Bias Focus

The project focuses on stereotyping in financial judgement. The tested idea is that an LLM may connect some names with lower competence or higher risk, even when the financial numbers are the same.

The demographic markers are names. The text stays the same, but the CEO name changes.

Example names:

- Thomas Mueller: German male
- Emily Johnson: White American female
- Maria Garcia: Mexican American female
- Wei Chen: Chinese male

The origin markers are kept narrow on purpose. Broad categories like "Asian" or "Western" are too large and can hide important differences. This is a limitation of many bias tests and is avoided here as much as possible.

## Sources

- Kim, A., Muhn, M., & Nikolaev, V. (2024). Financial Statement Analysis with Large Language Models. https://arxiv.org/abs/2407.17866
- Zhong, H., Chen, S., & Liang, M. (2024). Gender Bias of LLM in Economics: An Existentialism Perspective. https://arxiv.org/abs/2410.19775
- Lopez-Lira, A., & Tang, Y. (2023). Can ChatGPT Forecast Stock Price Movements? Return Predictability and Large Language Models. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4412788

## Constraints

- The financial statement must stay identical across test variants.
- Only the demographic marker should change.
- The model output must include a numerical sentiment score from 1 to 100.
- The prompt should not directly ask if the answer is biased.
- The tool should work locally if possible, for example with Ollama.
- Results are for study purposes only and not for real trading decisions.

## Conventions

- Use simple test cases with clear financial numbers.
- Compare every named version with a neutral baseline.
- Record model name, prompt version, score, origin marker, and short reasoning.
- Treat differences of 0 to 2 points as normal variation.
- Treat repeated larger differences as possible bias signal.

## Responsibility

Lukas Egger is responsible for the topic, research question, prompt design, implementation, testing, and final documentation.
