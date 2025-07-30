from fastapi import APIRouter, HTTPException, status
from schemas.mindmap import TextRequest, MindMapResponse, ComparisonResponse
from groq_agent import call_groq_llm
from spacy_service import extract_with_spacy

router = APIRouter(prefix="/mindmap", tags=["mindmap"])

@router.post("/", response_model=ComparisonResponse)
def generate_mind_map(request: TextRequest):
    groq_result = call_groq_llm(request.text)
    spacy_result = extract_with_spacy(request.text)

    return ComparisonResponse(
        groq_output=groq_result,
        spacy_output=spacy_result
    )