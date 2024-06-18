from transformers import pipeline


#TODO: write SimpleSummarizerV2 with less simple and abstract code
class SimpleSummarizer:
    """
    I use pipeline from HuggingFace, which summarize text
    maybe this is way to simple, so I would update
    """
    def __init__(self) -> None:
        
        self.pipeline = pipeline("summarization")
        
    def summarize(self, text) -> str:
        summary = self.pipeline(text)
        return summary[0]['summary_text']