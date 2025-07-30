from pydantic import BaseModel
from typing import List

class TextRequest(BaseModel):
    text: str

class Node(BaseModel):
    id: str

class Edge(BaseModel):
    source: str
    target: str
    label: str

class MindMapResponse(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

class ComparisonResponse(BaseModel):
    groq_output: MindMapResponse
    spacy_output: MindMapResponse