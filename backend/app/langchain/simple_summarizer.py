import tensorflow as tf
from langchain.prompts import ChatPromptTemplate
from transformers import pipeline, TFAutoModelForSeq2SeqLM, AutoTokenizer


class SimpleSummarizer:
    """
    I use pipeline from HuggingFace, which summarize text
    maybe this is way to simple, so I would update
    """
    model_name = "t5-small"
    
    def __init__(self) -> None:
        
        self.pipeline = pipeline("summarization", model=self.model_name)
        
    def summarize(self, text) -> str:
        summary = self.pipeline(text)
        return summary[0]['summary_text']
    
    
class SimpleSummarizerV2:
    model_name = "t5-small"
    
    def __init__(self):
        self.model = TFAutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.prompt = ChatPromptTemplate.from_template('Summarize a subject saving main idea {subject}')

    def summarize(self, text: str) -> str:
        input_ids = self.tokenizer.encode("summarize this text saving main idea: " + text, return_tensors="tf", max_length=512, truncation=True)
        summary_ids = self.model.generate(input_ids, max_length=150, num_beams=4, length_penalty=2.0, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary