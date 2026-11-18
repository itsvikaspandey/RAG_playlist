# 📂 RAG Series Test Dataset Catalog

This folder contains real-world enterprise PDF documents used across the **Blueprint of AI — RAG Mastery Series** for live coding, benchmarks, and side-by-side retrieval proofs.

---

## 📑 Included Documents

### 1. `tsla-20251231-gen.pdf` (Tesla Form 10-K SEC Filing)
* **Pages:** 139 Pages
* **Type:** Official SEC Form 10-K Annual Report (FY 2025)
* **Domain:** Automotive, Clean Energy, Public Financial Filing
* **Best Used For:**
  - **Table extraction vs text chunking tests:** Financial tables (Revenue by segment, Gross margins, Automotive deliveries).
  - **Exact number retrieval:** *"What were Tesla's total automotive revenues in 2025?"*
  - **Risk factor Q&A:** *"What risks does Tesla list regarding battery supply chains?"*
* **Episodes:** Ep 03 (Ingestion/Tables), Ep 04 (Chunking), Ep 08 (Vector DBs), Ep 09 (First RAG App), Ep 13 (Hybrid Search for part numbers/SKUs).

---

### 2. `ICICI-Bank-AR2025-2026_narrative.pdf` (ICICI Bank Annual Report Narrative)
* **Pages:** 64 Pages
* **Type:** Banking & Financial Services Strategic Report (FY 2025-2026)
* **Domain:** Commercial Banking, Digital Transformation, Governance, ESG
* **Best Used For:**
  - **Semantic search & topic chunking:** Multi-topic paragraphs spanning tech infrastructure, digital loans, and risk management.
  - **Narrative RAG:** *"How is ICICI Bank using AI and technology to improve customer service?"*
  - **Policy & governance queries:** *"What are the bank's key ESG and sustainability commitments?"*
* **Episodes:** Ep 05 (Vector Embeddings), Ep 06 (Cosine Similarity), Ep 10 (Semantic Chunking & Parent-Child), Ep 11 (Conversational Memory).

---

### 3. `Annual_Report_FY_26_20260803165214.pdf` (NSE Integrated Annual Report)
* **Pages:** 217 Pages
* **Type:** National Stock Exchange of India (NSE) Integrated Annual Report 2025-26 ("One Exchange. A Billion Dreams.")
* **Domain:** Capital Markets, Exchange Technology, Financial Infrastructure, Multi-Column Design
* **Best Used For:**
  - **Heavy multi-page indexing:** Stress testing vector stores and retrieval latency over 200+ pages.
  - **Multi-column and visual layouts:** Comparing basic loaders vs structured extractors.
  - **Complex multi-hop queries:** *"What was the total turnover across equities and derivatives, and how did market surveillance tech evolve?"*
* **Episodes:** Ep 03 (Ingestion at scale), Ep 07 (Chroma vs FAISS vs Pinecone latency benchmark), Ep 14 (Cross-Encoder Reranking), Ep 19 (Agentic RAG).

---

## 🎯 Quick Access Snippet for Notebooks

```python
import os
from pathlib import Path

DATA_DIR = Path("../data") # or Path("./data") depending on notebook location

TSLA_PDF = DATA_DIR / "tsla-20251231-gen.pdf"
ICICI_PDF = DATA_DIR / "ICICI-Bank-AR2025-2026_narrative.pdf"
NSE_PDF = DATA_DIR / "Annual_Report_FY_26_20260803165214.pdf"

print("✅ Real-world datasets loaded:")
print(f" - Tesla 10-K: {TSLA_PDF.resolve()} (Exists: {TSLA_PDF.exists()})")
print(f" - ICICI Bank: {ICICI_PDF.resolve()} (Exists: {ICICI_PDF.exists()})")
print(f" - NSE Report: {NSE_PDF.resolve()} (Exists: {NSE_PDF.exists()})")
```
