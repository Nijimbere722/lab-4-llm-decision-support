# Lab 4: LLMs and Prompt Engineering for Decision Support

A decision-support system for a microfinance loan officer, built using the Groq API
(Llama 3.3 70B). The system summarizes loan application letters, extracts structured
data as JSON, and generates a decision-support brief — without making the final
approve/reject call itself.


## Contents
lab-4-llm-decision-support: This is main notebook with all sections
Prompts.py: This is a final prompt templates, with notes on how they evolved
requirements.txt: dependencies

## Key results
- Extraction accuracy: 5/6 fields matched gold labels exactly across all 3 test
  letters; the sixth (`purpose`) was correct in meaning but scored lower under
  exact-text matching since it's free text.
- Reliability: extraction was fully consistent (same output every run) at both
  temperature 0.0 and 1.0 on the tested letter.
- Hallucination testing: system passed both adversarial tests — it did not invent
  missing details or fabricate data from irrelevant text.

## Note
This system is designed to support, not replace, a human loan officer. It never
outputs "approve" or "reject" — every letter should be reviewed by a person before
any decision is made.
