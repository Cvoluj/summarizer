from typing import Any, List, Mapping, Optional
from langchain.llms.base import LLM

class HuggingFaceLLM(LLM):
    model: Any
    tokenizer: Any
    
    def __init__(self, model, tokenizer):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return text

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"model_name": self.model.name_or_path}

    @property
    def _llm_type(self) -> str:
        return "huggingface"
