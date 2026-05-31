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
ollama pull llama3
python3 src/benchmark.py --model llama3
```

Results are written to `results/`.

Each run creates two files:

- `results/benchmark-YYYYMMDD-HHMMSS.csv`
- `results/benchmark-YYYYMMDD-HHMMSS.md`

## Test

```bash
python3 -m unittest discover -s tests
```

## Responsibility

Lukas Egger is responsible for the concept, promptotyping docs, implementation, testing, and final documentation.
