# 📚 AI Research Knowledge Assistant

An AI-powered Research & Knowledge Assistant that enables users to upload PDF documents and ask natural language questions. The system uses Retrieval-Augmented Generation (RAG), Hybrid Search, and Large Language Models (LLMs) to provide accurate, context-aware answers with document citations.



---
## 🚀 Features
- 📄 Upload and process PDF documents
- 🤖 Ask questions in natural language
- 🔍 Hybrid Search (Semantic Search + BM25)
- 🧠 Retrieval-Augmented Generation (RAG)
- 📑 Automatic document chunking
- 🗂️ ChromaDB Vector Database
- 📌 Answer with page citations
- 📊 Analytics Dashboard
- 📋 Document Summary
- 🌙 Modern React UI with Dark Mode
- ⚡ FastAPI REST API Backend

---



## 🏗️ System Architecture

```
                React Frontend
                      │
                      ▼
               FastAPI Backend
                      │
      ┌───────────────┴───────────────┐
      │                               │
      ▼                               ▼
  PDF Upload                    User Question
      │                               │
      ▼                               ▼
   PyMuPDF                     Hybrid Search
      │                  (Semantic + BM25)
      ▼                               │
Text Chunking                        ▼
      │                      Relevant Context
      ▼                               │
HuggingFace Embeddings                ▼
      │                          LLM (Gemini/Groq)
      ▼                               │
    ChromaDB                     AI Response
      │                               │
      └──────────────► Citations ◄────┘
```

---

## 🛠️ Tech Stack

### Frontend

- React.js
- Vite
- CSS3
- Axios

### Backend

- FastAPI
- Python

### AI & LLM

- LangChain
- Google Gemini API / Groq API
- HuggingFace Embeddings

### Vector Database

- ChromaDB

### Search

- Semantic Search
- BM25 Ranking

### PDF Processing

- PyMuPDF (fitz)

---

## 📂 Project Structure

```
AI-Research-Knowledge-Assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── rag/
│   │   ├── models/
│   │   ├── database/
│   │   ├── middleware/
│   │   └── main.py
│   │
│   ├── data/
│   │   ├── uploads/
│   │   └── chroma_db/
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Research-Knowledge-Assistant.git

cd AI-Research-Knowledge-Assistant
```

---

## Backend Setup

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file inside the backend folder.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

DATABASE_URL=sqlite:///./data/metadata.db

CHROMA_DB=./data/chroma_db

UPLOAD_DIR=./data/uploads
```

---

## Start Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# API Endpoints

## Upload PDF

```
POST /api/upload/
```

---

## Ask Question

```
POST /api/chat/
```

Example

```json
{
  "question": "What AI technologies does Santosh know?"
}
```

---

## Search Documents

```
GET /api/search/
```

---

## Analytics

```
GET /api/analytics/
```

---

## Summary

```
GET /api/summary/
```

---

## Uploaded Files

```
GET /api/upload/files
```

---

# Demo

### Upload Resume

```
RESUME.pdf
```

### Ask

```
What AI technologies does Santosh know?
```

### Response

```
• LangChain
• LangGraph
• Google Gemini API
• OpenAI API
• ChromaDB
• RAG
• Prompt Engineering

Page: 1
```

---

# Future Improvements

- OCR support for scanned PDFs
- Multi-document comparison
- Voice-based document chat
- Chat history
- Authentication
- Cloud deployment
- Streaming responses
- Multi-language support

---

# Skills Demonstrated

- Generative AI
- Retrieval-Augmented Generation (RAG)
- LangChain
- ChromaDB
- HuggingFace Embeddings
- FastAPI
- React.js
- REST APIs
- Vector Search
- Prompt Engineering
- Semantic Search
- BM25
- Python

---

# Author

**Santosh Tambe**

- LinkedIn
- GitHub
- Portfolio

---

# License

This project is licensed under the MIT License.

⭐ If you found this project useful, consider giving it a Star on GitHub.
