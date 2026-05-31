# Gender, AI & Diversity Bias Benchmark

This repository contains a small prototype for testing demographic bias in LLM financial sentiment analysis.

## Goal

The tool checks whether an LLM gives different financial sentiment scores when the same financial statement is linked to different CEO names.

## Method

- 15 financial scenarios
- 2 bias dimensions: gender and specific origin marker
- neutral baseline plus named CEO variants
- 15 named CEO personas plus one neutral baseline
- local LLM execution through Ollama
- CSV and Markdown result export

The origin markers are intentionally narrow. The prototype uses specific name signals such as German, White American, Mexican American, Chinese, Indian, Nigerian, Emirati, and Italian instead of broad categories like Western or Asian.

## Run

Dry run without Ollama:

```bash
python3 src/benchmark.py --dry-run
```

Run with Ollama:

```bash
ollama pull mistral
python3 src/benchmark.py --model mistral
```

Results are written to `results/`.

Each run creates four files:

- `results/benchmark-YYYYMMDD-HHMMSS.csv`
- `results/benchmark-YYYYMMDD-HHMMSS.md`
- `results/summary-YYYYMMDD-HHMMSS.csv`
- `results/summary-YYYYMMDD-HHMMSS.md`

The benchmark files contain every single model response.  
The summary files contain group statistics and a short interpretation.

Dry-run summaries are only for checking the code. Real interpretation should use an actual LLM run.

## Test

```bash
python3 -m unittest discover -s tests
```

## Responsibility

Lukas Egger is responsible for the concept, promptotyping docs, implementation, testing, and final documentation.
