import gradio as gr
from summarizer import load_model, generate_summary
from nlp_utils import extract_keywords

summarizer = load_model()
def process_text(text, mode, word_limit):
    if not text:
        return "Please provide input text.", "",""
    keywords = extract_keywords(text)
    output = generate_summary(text, summarizer, mode, word_limit)

    title = f"{mode} (approx. {word_limit} words)"
    return ", ".join(keywords), title, output

iface = gr.Interface(
    fn = process_text,
    inputs = [
        gr.Textbox(lines=10, label="Input Text"),
        gr.Radio(["Summary", "Report", "Notes"], value = "Summary", label = "Select Output Type"),
        gr.Slider(50, 500, step=10, value=150, label="Word Limit")

    ],
    outputs = [
        gr.Textbox(label="Extracted Keywords"),
        gr.Textbox(label="Output Title"),
        gr.Textbox(lines=10, label="Generated Output")
    ],
    title = "AI Document Generator",
    description = "Generate summaries, reports, or notes from your text input using AI.",
    
)

if __name__ == "__main__":
    iface.launch()

