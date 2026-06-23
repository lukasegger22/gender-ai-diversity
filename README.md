# Gender, AI & Diversity Bias Benchmark

This repository contains a small prototype for testing demographic bias in LLM financial sentiment analysis.

## Goal

The tool checks whether an LLM gives different financial sentiment scores when the same financial statement is linked to different CEO names.

## Method

- 15 scenarios total
- 10 controlled financial scenarios
- 5 ambiguous headline-style stress scenarios
- 2 bias dimensions: gender and specific origin marker
- neutral baseline plus named CEO variants
- 15 named CEO personas plus one neutral baseline
- local LLM execution through Ollama
- CSV and Markdown result export
- group statistics with mean and standard deviation

The origin markers are intentionally narrow. The prototype uses specific name signals such as German, White American, Mexican American, Chinese, Indian, Nigerian, Emirati, and Italian instead of broad categories like Western or Asian.

## Run

Dry run without Ollama:

```bash
python3 src/benchmark.py --dry-run
```

Run only the ambiguous stress scenarios:

```bash
python3 src/benchmark.py --model mistral --stress-only
```

Run the stress scenarios with a more open investor-confidence prompt:

```bash
python3 src/benchmark.py --model mistral --stress-only --prompt-mode open --verbose
```

Quick real test with fewer prompts:

```bash
python3 src/benchmark.py --model mistral --limit-scenarios 5 --limit-personas 5 --verbose
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

The scenario set stays compact on purpose. Ten scenarios use clearer financial facts, while five scenarios are deliberately more ambiguous and headline-like. The ambiguous scenarios act as a stress test for whether demographic name signals matter more when the business situation leaves more room for interpretation.

Dry-run summaries are only for checking the code. Real interpretation should use an actual LLM run.

## Interpretation

The benchmark does not treat every score difference as bias. Deltas from 0 to 2 points are treated as no clear signal, and small differences are interpreted cautiously. The main evidence would be a repeated group-level pattern, not one isolated row.

The current exploratory result is that `mistral` and `llama3` often give identical or very similar scores when only the CEO name changes. This should be interpreted as no stable repeated demographic scoring bias detected in the current setup, not as proof that the models are unbiased.

Standard deviation in the summary helps interpret spread. A low `std_delta` with mean delta close to 0 supports the interpretation that the group stayed near the neutral baseline. A high `std_delta` means individual scenarios or outliers should be inspected manually.

## Test

```bash
python3 -m unittest discover -s tests
```

## Responsibility

Lukas Egger is responsible for the concept, promptotyping docs, implementation, testing, and final documentation.
