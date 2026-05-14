# AI Prompt Library

A Streamlit application for VBC healthcare teams to extract relevant information from PDF documents using AI.

## Features
- Six team tabs: Developer, QA, Scrum Master, Financial, Scorecard, Member
- PDF upload with keyword-based filtering
- Team-specific keyword extraction
- Markdown report download

## How to Run
1. Install dependencies: `pip3 install streamlit ollama pypdf`
2. Start Ollama: `ollama serve`
3. Run app: `streamlit run prompt_library.py`

## Teams and Keywords
- **Scorecard:** quality, scorecard, provider, numerator, denominator
- **Member:** member, eligibility, inclusion, exclusion
- **Financial:** CFF, savings, amounts, payments, provider