import spacy
from schemas.mindmap import MindMapResponse

nlp = spacy.load("en_core_web_sm")

def extract_with_spacy(text: str) -> MindMapResponse:
    doc = nlp(text)

    concepts = set(chunk.text.strip() for chunk in doc.noun_chunks)
    relations = []

    for token in doc:
        # Subject-verb-object structure
        if token.dep_ in ("nsubj", "dobj") and token.head.pos_ == "VERB":
            verb = token.head.lemma_
            subject_or_obj = token.text.strip()
            relations.append((verb, subject_or_obj))

    # Convert to node-edge structure
    nodes = [{"id": c} for c in concepts]
    edges = [{"source": rel[0], "target": rel[1], "label": "related_to"} for rel in relations]

    return MindMapResponse(nodes=nodes, edges=edges)
