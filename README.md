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
Sample Input for summary:
<img width="939" height="780" alt="image" src="https://github.com/user-attachments/assets/2943a747-b1e1-4645-bdff-8553168c766b" />
Sample Ouptut for summary:
<img width="908" height="625" alt="image" src="https://github.com/user-attachments/assets/236b78e9-8fb8-4b5c-b9c5-0532e30a40ae" />

Sample Input for notes:
<img width="857" height="744" alt="image" src="https://github.com/user-attachments/assets/eef277c9-8a35-4f49-814d-8da249c9dcc6" />
Sample Output for notes:
<img width="893" height="728" alt="image" src="https://github.com/user-attachments/assets/e05db7bc-cf89-461c-a3b5-4e0682ed32cb" />

Sample Input for report:
<img width="864" height="660" alt="image" src="https://github.com/user-attachments/assets/d7f08664-6f41-4ca4-8b93-1e915318a5cd" />
Sample Output for report:
<img width="794" height="691" alt="image" src="https://github.com/user-attachments/assets/a1d054c3-2185-42b8-9cc2-92c0d401d58d" />








