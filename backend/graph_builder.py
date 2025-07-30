def build_graph(entities: dict) -> dict:
    nodes = [{"id": concept} for concept in set(entities["concepts"])]
    edges = [
        {
            "source": source,
            "target": target,
            "label": relation
        }
        for source, relation, target in entities["relations"]
    ]
    return {"nodes": nodes, "edges": edges}
