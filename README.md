# 🧠 MindMapr – Automatic Concept Mapper

## 🚀 Overview

MindMapr is a full-stack web app that converts any input text into an interactive **mind map** using NLP and graph visualization. It supports both **spaCy** and **Groq** outputs, rendered side-by-side using **Cytoscape.js** in React.

---

## 🛠 Features

- Text-to-MindMap API (`/auth/mindmap/`)
- Uses **spaCy** for extracting noun chunks and verbs
- Optionally uses **Groq LLM** for richer understanding
- Returns structured node–edge JSON
- Renders interactively with zoom/pan support in React using **Cytoscape.js**

---

## 🔧 Tech Stack

| Layer       | Tech                        |
|------------|-----------------------------|
| Frontend   | React, TailwindCSS, Cytoscape |
| Backend    | FastAPI, Python, spaCy, httpx |
| Deployment | Localhost / VPS-ready       |

---

## 🧪 Sample API Call
```bash
POST /auth/mindmap/
{
  "text": "Artificial Intelligence is a branch of computer science."
}

Output

{
  "spacy_output": {
    "nodes": [{"id": "Artificial Intelligence"}, {"id": "computer science"}],
    "edges": [{"source": "Artificial Intelligence", "target": "computer science", "label": "is a branch of"}]
  },
  "groq_output": {
    "nodes": [...],
    "edges": [...]
  }
}



🖥 How to Run Locally
Backend (FastAPI)
bash
Copy
Edit
cd backend
uvicorn main:app --reload
Frontend (React)
bash
Copy
Edit
cd frontend/mindmapr
npm install
npm start
