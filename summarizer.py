from transformers import pipeline
def load_model():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer

def generate_summary(text, summarizer, mode = "Summary", word_limit = 150):
    if mode == "Report":
        prompt = f"Write a professional report (around {word_limit} words) about the following content:\n\n{text}"
    
    elif mode == "Notes":
        prompt = f"Generate concise notes (around {word_limit} words) from the following content:\n\n{text}"
    
    else:  # Default to Summary
        prompt = f"Summarize the following content in around {word_limit} words:\n\n{text}"

    summary = summarizer(prompt, max_length = word_limit + 50, min_length=max(30, word_limit -50), do_sample=False)
    return summary[0]['summary_text']