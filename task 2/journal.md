# Journal

**Project:** Bias in LLM financial sentiment analysis  
**Student:** Lukas Egger

## Project Log

### Topic Choice

I chose finance and algorithmic trading as the project domain. The reason is that LLM sentiment analysis can have real effects when it is used for financial decisions.

### Research Question

The research question is:

Do large language models give lower or riskier financial sentiment scores when the same company statement is connected to female or specific non-dominant origin markers?

### Decisions Made

- I will use names as demographic markers.
- I will test gender and specific origin markers as the main dimensions.
- I will compare named prompts against a neutral baseline.
- I will use a 1 to 100 sentiment score as the main output.
- I will keep the financial statement identical in all variants.
- I will use local models through Ollama if possible.

### Alternatives Considered

- I considered using explicit labels like "female CEO" or "Asian CEO", but this is too direct and too broad. The prototype now uses narrower origin markers.
- I considered using API models, but local models are easier to reproduce for this course project.
- I considered building a bigger app, but a smaller tool is enough for the assignment.

### Open Questions

- How stable are the scores if the same prompt is run multiple times?
- Does the model explanation show stereotypes even when the score is similar?
- Does a diversity-aware prompt reduce bias or make the model focus too much on identity?

### Current Status

The project concept is defined. A Python prototype is implemented. It can run 15 scenarios with neutral and named CEO variants, compare scores against the neutral baseline, and export CSV and Markdown results.

### Prototype Notes

- The implementation follows the Task 2 design.
- The first real prototype run uses `mistral` through Ollama. `llama3` remains an optional second model from the original plan.
- A dry-run mode was added to test the code before running a real local model.
- The output format is simple so it can be checked manually.
- After class feedback, broad groups like "Asian" and "Western" were replaced by narrower markers such as Chinese, German, White American, Mexican American, Indian, Nigerian, Emirati, and Italian.

### Final Reflection

- The benchmark often produced identical or very similar scores across CEO names.
- This is interpreted as low name sensitivity in the current strict financial prompt setup.
- Small deltas are not enough to claim bias.
- Repeated group-level deltas would be stronger evidence than isolated differences.
- Standard deviation was added to show whether deltas are stable or caused by outliers.
- The project does not prove that the tested models are unbiased; it only shows that this prototype did not confirm a stable repeated demographic scoring bias in the current runs.
- A future version should add subjective dimensions such as credibility, perceived risk, investor confidence, and uncertainty.

## Responsibility

Lukas Egger is responsible for all project tasks: concept, research, promptotyping documents, implementation, testing, and final submission.
