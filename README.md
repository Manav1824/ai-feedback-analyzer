# 🤖 Automated Customer Feedback Analyzer (Gemini API)

A Python-based AI processing utility that converts unstructured customer feedback into structured, machine-readable JSON data using Google's Gemini models.

## Features
- **Structured JSON Schema:** Enforces rigid schema formatting (`application/json`) for direct database ingestion.
- **Sentiment & Ticket Triage:** Extracts core summaries, determines sentiment polarity, and automatically flags support escalation triggers.
- **Secure Configuration:** Zero hardcoded credentials; authenticates via runtime environment variables.

## Tech Stack
- Python 3.14
- `google-genai` SDK (`gemini-3.8-flash`)
- Structured Output API Configuration

## Setup & Execution
1. Install dependencies:
   ```bash
   pip install google-genai