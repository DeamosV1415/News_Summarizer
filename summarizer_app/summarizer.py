from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    return summarizer_pipeline(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']