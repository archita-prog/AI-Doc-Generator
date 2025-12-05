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

UI:
<img width="1855" height="732" alt="image" src="https://github.com/user-attachments/assets/322a2b2d-12c5-466d-be34-0be290aff741" />
Sample Input:
<img width="939" height="780" alt="image" src="https://github.com/user-attachments/assets/2943a747-b1e1-4645-bdff-8553168c766b" />
Sample Ouptut:
<img width="908" height="625" alt="image" src="https://github.com/user-attachments/assets/236b78e9-8fb8-4b5c-b9c5-0532e30a40ae" />



