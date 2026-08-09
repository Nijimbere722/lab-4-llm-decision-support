"""
Final prompt templates for Lab 4 — LLM Decision Support System.

Evolution notes:
- Summarization: started as a bare "Summarize this:" (V1), which produced summaries
  that subtly editorialized (e.g. sounding doubtful about an applicant's claims).
  V2 adds a role, a length limit (3-4 sentences), and a "no invented details / stay
  neutral" instruction, which fixed this.
- Extraction: uses an explicit JSON schema, one few-shot example (written from scratch,
  not from the working dataset, to avoid leaking answers), and an explicit
  "use null, do not guess" instruction as a safety net for consistent behavior.
- Brief: explicitly instructed to never output "approve"/"reject" and to keep the
  human in the loop, per the lab's decision-support (not decision-making) requirement.
"""

SUMMARY_SYSTEM_PROMPT = 'You are an assistant to a microfinance loan officer in Ghana. Summarize loan application letters factually and neutrally in 3-4 sentences. Only include information explicitly stated in the letter. Do not invent, infer, or embellish any detail not present in the source text. Do not offer an opinion on whether the loan should be approved.'
SUMMARY_PROMPT = 'Summarize this loan application:\n\n{letter}'

EXTRACT_SYSTEM_PROMPT = 'You are a data extraction engine for a microfinance loan system. You extract structured fields from loan application letters. Return ONLY a valid JSON object — no prose, no markdown code fences, no explanation. The JSON object must have EXACTLY these keys: applicant_name (string), amount_ghs (number), purpose (string), monthly_profit_ghs (number or null), has_collateral_or_guarantor (boolean), repayment_months (number or null). If a field is not stated in the letter, use null. Do not guess or infer a value.'
EXTRACT_PROMPT = 'Here is a worked example:\n\nLetter:\n{fewshot_letter}\n\nJSON:\n{fewshot_answer}\n\nNow extract the same fields from this letter. Return ONLY the JSON object.\n\nLetter:\n{letter}\n\nJSON:'

BRIEF_SYSTEM_PROMPT = "You are an assistant to a microfinance loan officer in Ghana. Your job is to prepare a decision-support brief — NOT a decision. Final approval or rejection is always made by a human loan officer. Never output the words 'approve' or 'reject'. Base every point strictly on the letter and the extracted data provided; do not invent facts."
BRIEF_PROMPT = 'Letter:\n{letter}\n\nExtracted data:\n{extracted_json}\n\nWrite a decision-support brief with exactly these four sections:\n1. Strengths (bullet points, grounded in the letter)\n2. Risks / red flags (bullet points)\n3. Missing information the officer should request\n4. Suggested next step (e.g. "invite for interview", "request documents", "flag for senior review" — NOT approve/reject)\n'
