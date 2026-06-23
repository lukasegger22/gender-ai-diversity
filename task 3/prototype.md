# Task 3 Prototype

**Project:** Bias in LLM financial sentiment analysis  
**Student:** Lukas Egger

## Prototype Status

The first prototype is implemented as a small Python command line tool.

It follows the Task 2 promptotyping documents:

- 15 scenarios are stored in `data/scenarios.json`.
- The scenario set contains 10 controlled financial scenarios and 5 ambiguous headline-style stress scenarios.
- Demographic variants are stored in `data/personas.json`.
- The tested bias dimensions are gender and specific origin marker.
- The neutral CEO version is used as the baseline.
- Named CEO versions are compared against the baseline.
- Results are exported as CSV and Markdown.
- Summary statistics are exported as CSV and Markdown.

## How It Works

The tool builds one prompt for each scenario and persona. The prompt asks the LLM to return a financial sentiment score from 1 to 100 and one short reason.

The tool records:

- scenario id
- model
- persona name
- gender
- origin_marker
- sentiment score
- baseline score
- score difference
- bias label
- model reason
- prompt
- raw response

The summary output records:

- group type
- group name
- number of rows
- average score
- score standard deviation
- average delta from baseline
- delta standard deviation
- lowest delta
- highest delta
- count of moderate or stronger bias signals

## LLM

The planned LLM runtime is Ollama with `mistral`. The Task 2 docs also mention `llama3` as an optional second local model.

The prototype also has a dry-run mode. This mode does not call an LLM. It is only used to test the code, data structure, and exports.

The persona categories were updated after class feedback. Broad groups like "Asian" and "Western" are too coarse, so the prototype uses narrower origin markers. The prototype now has 15 named CEO personas plus one neutral baseline.

## Current Scoring Reflection

Early test runs showed that the model often gives identical scores to different CEO names when the business statement stays the same.

Short interpretation:

- This does not mean the prototype is broken.
- The current score mainly measures the financial situation in the text.
- The model often follows the instruction to focus on business facts.
- Identical scores can therefore be interpreted as low name sensitivity in this setup.
- Small deltas are interpreted cautiously and are not treated as proof of bias.
- Standard deviation helps show whether score differences are stable or mainly caused by outliers.
- A single 1-100 sentiment score may be too broad to reveal subtle bias.
- Bias may appear more clearly in interpretive dimensions such as perceived risk, credibility, confidence, or uncertainty.

Design decision:

- Keep the strict financial sentiment score as the main controlled benchmark.
- Use the new ambiguous headline-style scenarios as a stress test.
- Use the `open` prompt mode to test investor-confidence judgments with more interpretive space.
- Do not force bias signals; if no differences appear, this is still a valid result.

Possible next improvement:

- Add multi-dimensional scoring, for example financial sentiment, investor confidence, perceived risk, leadership credibility, and uncertainty.
- Compare whether names have no effect on financial sentiment but possible effects on more subjective evaluation categories.

## Commands

Dry run:

```bash
python3 src/benchmark.py --dry-run
```

Run with Ollama:

```bash
python3 src/benchmark.py --model mistral
```

Run only the ambiguous stress scenarios:

```bash
python3 src/benchmark.py --model mistral --stress-only --prompt-mode open --verbose
```

Each run creates raw benchmark files and summary files in `results/`.

## Responsibility

Lukas Egger is responsible for the prototype implementation, prompt data, testing, and documentation updates.
