# 🧠 AI Document Generator

An AI-powered app that generates **summaries, reports, and notes** using Hugging Face Transformers, spaCy NLP, and Gradio for an interactive web interface.

---

## 🚀 Features
- Summarization using `facebook/bart-large-cnn`
- Keyword extraction with spaCy
- Adjustable word limits
- Export-ready structured document output
- Deployed easily on Hugging Face Spaces

---

## 🧩 Tech Stack
- Python
- Hugging Face Transformers
- spaCy
- Gradio (UI)
- Hugging Face Spaces (deployment)

---

## 🛠️ Setup Instructions

1. Clone the repo  
   ```bash
   git clone https://github.com/<your-username>/ai-document-generator.git
   cd ai-document-generator
2. python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
python app.py
git remote add origin https://huggingface.co/spaces/<username>/ai-doc
git push origin main



