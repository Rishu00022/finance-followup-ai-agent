# Finance Credit Follow-Up Email Agent

AI-powered finance collection assistant that automates overdue invoice reminder emails.

---

## Features

- CSV invoice ingestion
- Overdue detection
- Tone escalation
- Email generation
- Audit logging

---

## Tech Stack

- Python
- Pandas
- dotenv
- LangChain
- OpenAI

---

## Run Project

```bash
python3 src/main.py
```

---

## Security

- `.env` for API keys
- `.gitignore` protection
- Audit trail logging
- No hardcoded credentials# finance-followup-ai-agent
---

# Technical Stack & Decision Log

## LLM Chosen

Currently using rule-based email generation.
Future integration planned with:
- OpenAI GPT-4o
- Claude 3.5 Sonnet

Reason:
- Strong text generation
- Professional email formatting
- Good prompt handling

---

## Agent Framework

Current workflow uses modular Python architecture.

Future framework:
- LangChain
- LangGraph

Architecture Type:
- Sequential workflow pipeline

Flow:
CSV Input → Escalation Engine → Email Generator → Audit Logger

---

## Prompt Design

Prompts are designed to:
- Maintain professional tone
- Escalate politely
- Include invoice details dynamically
- Avoid generic email responses

Guardrails:
- No missing invoice fields
- Controlled escalation wording
- Structured email templates

---

## Security Mitigations

| Risk | Mitigation |
|---|---|
| Prompt Injection | Input sanitization |
| API Key Exposure | `.env` usage |
| PII Leakage | No sensitive logs |
| Hallucination | Structured templates |
| Unauthorized Access | Local execution only |
| Email Spoofing | Dry-run mode |
