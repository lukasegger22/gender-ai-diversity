# Journal

**Project:** Bias in LLM financial sentiment analysis  
**Student:** Lukas Egger

## Project Log

### Topic Choice

I chose finance and algorithmic trading as the project domain. The reason is that LLM sentiment analysis can have real effects when it is used for financial decisions.

### Research Question

The research question is:

Do large language models give lower or riskier financial sentiment scores when the same company statement is connected to female or non-Western executive names?

### Decisions Made

- I will use names as demographic markers.
- I will test gender and ethnicity as the main dimensions.
- I will compare named prompts against a neutral baseline.
- I will use a 1 to 100 sentiment score as the main output.
- I will keep the financial statement identical in all variants.
- I will use local models through Ollama if possible.

### Alternatives Considered

- I considered using explicit labels like "female CEO" or "Asian CEO", but this is too direct and may make the bias test less natural.
- I considered using API models, but local models are easier to reproduce for this course project.
- I considered building a bigger app, but a smaller tool is enough for the assignment.

### Open Questions

- How stable are the scores if the same prompt is run multiple times?
- Does the model explanation show stereotypes even when the score is similar?
- Does a diversity-aware prompt reduce bias or make the model focus too much on identity?

### Current Status

The project concept is defined. The next step is to build the small testing tool and run the prompt set with different demographic name variants.

## Responsibility

Lukas Egger is responsible for all project tasks: concept, research, promptotyping documents, implementation, testing, and final submission.
