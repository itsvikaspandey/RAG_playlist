# 🧠 RAG from Scratch — YouTube Series

> **Build Retrieval-Augmented Generation (RAG) systems step by step, from raw documents to semantic search.**

[![YouTube Playlist](https://img.shields.io/badge/YouTube-Playlist-red?logo=youtube&logoColor=white)](https://youtube.com/playlist?list=PLMBF-fASLD4I&si=iO5P-epRzdVBnuDV)
[![GitHub](https://img.shields.io/badge/GitHub-RAG__playlist-black?logo=github)](https://github.com/itsvikaspandey/RAG_playlist)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Community-green)](https://python.langchain.com/)

---

## 📺 Playlist

🎬 **[Watch Full Playlist →](https://youtube.com/playlist?list=PLMBF-fASLD4I&si=iO5P-epRzdVBnuDV)**

| # | Episode | Topics Covered | Code |
|---|---------|---------------|------|
| 1 | [**RAG Intro — What & Why**](https://youtu.be/s51cefXFOWM?si=1Ck33oTH9vtD6JYG) | What is RAG, how it works, use cases, architecture overview | — |
| 2 | [**Document Processing**](https://youtu.be/Sl_-jfnbn0I?si=GN0TILDcMu96BVMq) | Loading TXT, PDF, CSV, DOCX, HTML & web pages with LangChain loaders | [`01_data_ingestion.py`](01_data_ingestion.py) |
| 3 | [**Chunking Strategies**](https://youtu.be/9N_vXv29znc?si=CG-Sq4uSksjJrLre) | Fixed-size, recursive, semantic chunking; chunk size & overlap tuning | [`02_chunking_strategies.py`](02_chunking_strategies.py) |
| 🔜 | *Embeddings* *(coming soon)* | Sentence Transformers, vector math, cosine similarity | [`03_embedding.py`](03_embedding.py) |

---

## 🗂️ Repo Structure

```
yt-rag-course/
│
├── 01_data_ingestion.py        # Ep 2 — Load TXT, PDF, CSV, DOCX, Web
├── 02_chunking_strategies.py   # Ep 3 — Chunking strategies & overlap
├── 03_embedding.py             # Ep 4 — Embeddings & vector search (WIP)
│
├── data/                       # Sample documents used in the series
│   ├── notes.txt
│   ├── annual_report.pdf
│   ├── metrics.csv
│   ├── handbook.docx
│   └── tsla-20251231-gen.pdf   # Tesla 10-K used for chunking/embedding demos
│
├── tesla_index/                # Pre-built FAISS-style index from Ep 4
│   ├── chunks.json
│   ├── vectors.npy
│   └── model.txt
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/itsvikaspandey/RAG_playlist.git
cd RAG_playlist

# 2. Create a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Run the Code

```bash
# Episode 2 — Document Ingestion
python 01_data_ingestion.py

# Episode 3 — Chunking Strategies
python 02_chunking_strategies.py

# Episode 4 — Embeddings & Vector Search
pip install sentence-transformers numpy faiss-cpu
python 03_embedding.py
```

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `langchain-core` / `langchain-community` | Document loaders, text splitters |
| `pypdf` / `pymupdf` | PDF parsing |
| `docx2txt` | Word document loading |
| `pandas` / `tabulate` | CSV handling |
| `beautifulsoup4` / `requests` | Web page loading |
| `sentence-transformers` | Text embeddings |
| `numpy` | Vector math |
| `faiss-cpu` | Vector similarity search |

---

## 🔔 Stay Updated

New episodes drop regularly. Subscribe so you don't miss them!

[![Subscribe](https://img.shields.io/badge/Subscribe-YouTube-red?logo=youtube&logoColor=white)](https://youtube.com/playlist?list=PLMBF-fASLD4I&si=iO5P-epRzdVBnuDV)

---

> Made with ❤️ by [Vikas Pandey](https://github.com/itsvikaspandey)
