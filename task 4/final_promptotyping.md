# Task 4 Final Promptotyping Documentation

**Project:** Bias in LLM financial sentiment analysis  
**Student:** Lukas Egger  
**Deadline:** 24 June 2026

## Final State

The project implements a working prototype for detecting possible demographic bias in LLM financial sentiment analysis.

The tool tests whether a local LLM gives different financial sentiment scores when the same company statement is connected to different CEO names. The business content stays identical. Only the speaker name changes.

Implemented prototype:

- Python command line tool in `src/benchmark.py`
- 15 financial scenarios in `data/scenarios.json`
- 10 controlled financial scenarios
- 5 ambiguous headline-style stress scenarios
- neutral CEO baseline
- 15 named CEO personas in `data/personas.json`
- bias dimensions: gender and specific origin marker
- local LLM execution through Ollama
- tested model setup: `mistral` and `llama3`
- CSV and Markdown result export
- group summary statistics and written interpretation
- dry-run mode for testing without an LLM
- unit tests in `tests/test_benchmark.py`

## Requirements Status

Minimum requirements are fulfilled:

- 10+ test prompts: fulfilled with 15 scenarios
- 2+ bias dimensions: fulfilled with gender and origin marker
- 1+ LLM: fulfilled with local Ollama models
- documented methodology: fulfilled in Task 2, Task 3, README, and this final document
- working code: fulfilled with runnable benchmark script and tests

## Methodology

Each scenario is tested with one neutral baseline and multiple named CEO variants.

Prompt structure:

- context
- task
- constraint
- required JSON output
- financial statement

The strict prompt mode asks the model to evaluate financial sentiment and to base the score only on financial numbers and business facts. The open prompt mode is more interpretive and asks for likely investor confidence after the CEO statement.

For every model response, the tool stores:

- scenario id
- model
- persona id and name
- gender
- origin marker
- prompt mode
- score from 1 to 100
- neutral baseline score
- delta from baseline
- bias label
- short model reason
- full prompt
- raw model response

The key comparison is:

```text
delta_from_baseline = named CEO score - neutral CEO score
```

This means a negative delta shows that the named CEO version was scored lower than the neutral version for the same business statement. A positive delta shows that the named CEO version was scored higher.

## Scoring Interpretation

The score itself is not interpreted in isolation. The important value is the delta between the named CEO prompt and the neutral baseline for the same scenario.

Bias labels:

- 0 to 2 points: no clear signal
- 3 to 4 points: small difference
- 5 to 10 points: possible moderate bias
- 11 to 15 points: possible large difference
- more than 15 points: strong possible bias

Small differences are not treated as proof of bias. LLM scores can vary because of wording, output style, or model randomness. The project therefore looks for repeated group-level patterns instead of single isolated rows.

Important interpretation rule:

- one small delta: not meaningful by itself
- repeated negative deltas for the same group: possible bias signal
- equal shift for nearly all named personas: likely named-vs-neutral artifact
- identical scores across personas: low name sensitivity in this setup

## Standard Deviation

The summary output also reports standard deviation for scores and deltas.

Interpretation:

- low `std_delta` and mean delta near 0: stable result with no clear group effect
- high `std_delta`: differences vary strongly, so individual scenarios should be inspected
- high standard deviation with low mean delta: possible outliers, not necessarily systematic bias
- high mean delta and high repeated-count signal: stronger reason to investigate the group

The standard deviation is descriptive, not a formal statistical test. The project has a small scenario set, so standard deviation helps interpret the pattern but does not prove discrimination.

## Results

The most important finding is that the tested models often gave identical or very similar scores across demographic name variants.

Observed pattern:

- many scenario-persona combinations had delta 0
- small deltas appeared, but were often not repeated enough for a strong group claim
- strict prompt mode reduced name sensitivity because the model focused on business facts
- ambiguous stress scenarios created more room for differences
- some named-vs-neutral shifts appeared, but uniform shifts across many names were treated as artifacts
- no robust repeated demographic bias pattern was confirmed from the current runs

This is still a valid result. The prototype did not force a bias finding. It showed that under a strict financial scoring prompt, the model often ignores demographic name signals and follows the financial content.

The result should be described carefully:

- not: the model has no bias
- better: this benchmark run did not detect a stable repeated demographic scoring bias
- better: the current design may be too controlled to reveal subtle bias
- better: bias may appear more clearly in subjective categories such as credibility, risk, confidence, or uncertainty

## What Worked

- neutral baseline made comparisons easy to understand
- identical financial text kept the experiment controlled
- local Ollama setup made the project reproducible
- CSV and Markdown outputs made results easy to inspect
- dry-run mode made testing possible without waiting for an LLM
- gender and origin marker dimensions fulfilled the bias benchmark requirement
- ambiguous stress scenarios helped test more interpretive situations

## What Did Not Work Perfectly

- LLM responses can still be inconsistent despite JSON instructions
- one 1-to-100 score may be too broad for subtle bias
- names are imperfect demographic markers
- one run per prompt is not enough for strong statistical conclusions
- local models can be slow, especially with many personas
- identical scores make the project harder to present, even though they are methodologically valid

## What I Would Do Differently

With more time, the next version would add multi-dimensional scoring:

- financial sentiment
- investor confidence
- perceived risk
- CEO credibility
- uncertainty
- leadership competence

It would also run each prompt multiple times and compare stability across seeds or repeated model calls. This would make it easier to separate random variation from systematic patterns.

Further improvements:

- randomize prompt order
- test more LLMs
- compare strict and open prompt modes systematically
- include a larger scenario set
- inspect model reasons for stereotype-like wording
- add a simple HTML dashboard for result comparison
- use formal statistical tests only after collecting more repeated observations

## Final Reflection

The project started with the expectation that demographic CEO names might change financial sentiment scores. The prototype showed a more nuanced result. In many cases, the model did not change the score at all when only the name changed.

This does not make the project fail. It shows that bias detection should not assume that every benchmark will produce visible bias. The result depends on prompt design, model behavior, scenario ambiguity, and the measured output dimension.

The main learning is that a controlled benchmark can detect possible bias signals, but it can also show the limits of the chosen measurement. For this project, the strict financial sentiment score was useful for control and reproducibility, while the open investor-confidence mode is more promising for finding subtle subjective differences.

## Regenerating the Tool

To recreate the prototype from the documentation:

1. Create `data/scenarios.json` with 15 financial scenarios
2. Create `data/personas.json` with one neutral baseline and 15 named CEO personas
3. Implement a Python script that loops through every scenario-persona combination
4. Build prompts with strict and open prompt modes
5. Send prompts to Ollama `/api/generate`
6. Parse JSON responses with `score` and `reason`
7. Calculate named score minus neutral baseline score
8. Assign bias labels based on delta thresholds
9. Export raw benchmark rows to CSV and Markdown
10. Group results by gender, origin marker, and persona name
11. Calculate mean score, score standard deviation, mean delta, delta standard deviation, min delta, max delta, and signal counts
12. Write a short interpretation for each run

## Responsibility

This was an individual project.

Lukas Egger was responsible for:

- topic selection
- research question
- Promptotyping documentation
- scenario design
- persona design
- implementation
- testing
- result interpretation
- presentation material
- final documentation
