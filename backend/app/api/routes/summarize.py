from fastapi import APIRouter, Depends, HTTPException, Request

from backend.app.schemas import SummarizeSchema
from backend.app.langchain import SimpleSummarizer, SimpleSummarizerV2


router = APIRouter()

@router.post("/summarize")
async def summarize(request: SummarizeSchema, summarizer: SimpleSummarizer = Depends(SimpleSummarizer)):
    """
    request class is SummarizeSchema, also we have summarizer created with Dependency Injection, which is good practice
    """
    return {"summary": summarizer.summarize(request.text)}

@router.post("/summarize_v2")
async def summarize(request: SummarizeSchema, summarizer: SimpleSummarizerV2 = Depends(SimpleSummarizerV2)): 
    return {"summary": summarizer.summarize(request.text)}