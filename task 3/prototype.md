# Task 3 Prototype

**Project:** Bias in LLM financial sentiment analysis  
**Student:** Lukas Egger

## Prototype Status

The first prototype is implemented as a small Python command line tool.

It follows the Task 2 promptotyping documents:

- 10 financial scenarios are stored in `data/scenarios.json`.
- Demographic variants are stored in `data/personas.json`.
- The tested bias dimensions are gender and ethnicity.
- The neutral CEO version is used as the baseline.
- Named CEO versions are compared against the baseline.
- Results are exported as CSV and Markdown.

## How It Works

The tool builds one prompt for each scenario and persona. The prompt asks the LLM to return a financial sentiment score from 1 to 100 and one short reason.

The tool records:

- scenario id
- model
- persona name
- gender
- ethnicity
- sentiment score
- baseline score
- score difference
- bias label
- model reason
- prompt
- raw response

## LLM

The planned LLM runtime is Ollama with `llama3`.

The prototype also has a dry-run mode. This mode does not call an LLM. It is only used to test the code, data structure, and exports.

## Commands

Dry run:

```bash
python3 src/benchmark.py --dry-run
```

Run with Ollama:

```bash
python3 src/benchmark.py --model llama3
```

## Responsibility

Lukas Egger is responsible for the prototype implementation, prompt data, testing, and documentation updates.
