# Requirements

**Project:** Bias in LLM financial sentiment analysis  
**Student:** Lukas Egger

## Goal

The tool should test if an LLM gives different financial sentiment scores when the same company statement is connected to different CEO names.

## Users

The main user is the student working on the project. A second user could be a teacher or reviewer who wants to understand and reproduce the test.

## User Stories

- As a student, I want to enter or load financial test prompts, so I can run the same scenario many times.
- As a student, I want to compare neutral and named versions, so I can see if the score changes.
- As a student, I want to save model outputs, so I can review the results later.
- As a reviewer, I want the prompts and results to be transparent, so I can understand how the conclusion was made.

## Functional Requirements

- The tool stores several financial scenarios.
- Each scenario has a neutral version and named CEO versions.
- The tool sends each prompt to one or more LLMs.
- The tool records the numerical sentiment score from 1 to 100.
- The tool records a short explanation from the model.
- The tool calculates the difference between named versions and the neutral baseline.
- The tool exports results in a simple format, for example CSV or Markdown.

## Acceptance Criteria

- A user can run at least 10 financial scenarios.
- Each scenario can be tested with at least 3 prompt variants.
- The output includes model name, prompt, demographic marker, sentiment score, and score difference.
- The same financial content is used for all demographic variants.
- The result table makes possible bias visible without needing manual recalculation.

## Scope

In scope:

- Local LLM testing with Ollama.
- Prompt templates for earnings call style texts.
- Basic result comparison.
- Short written analysis of findings.

Out of scope:

- Real financial advice.
- Live stock market integration.
- Full statistical research paper.
- A large production web application.

## Responsibility

Lukas Egger is responsible for writing the requirements, creating the test prompts, running the experiments, and checking the results.
