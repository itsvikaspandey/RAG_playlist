"""
Create and search text embeddings from Tesla's annual report.

Install the required packages:
    pip install pypdf sentence-transformers numpy

To also try the optional FAISS search:
    pip install faiss-cpu

Run:
    python 03_embedding.py

To search for a different question, change QUERY below and run the script again.
"""
import json
import re
from pathlib import Path

import numpy as np
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer


# Change this path if your PDF is stored somewhere else.
PDF_PATH = Path("data/tsla-20251231-gen.pdf")
if not PDF_PATH.exists():
    PDF_PATH = Path("RAG-SERIES/data/tsla-20251231-gen.pdf")

MODEL_NAME = "BAAI/bge-small-en-v1.5"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
CHUNK_SIZE = 900
CHUNK_OVERLAP = 150
INDEX_FOLDER = Path("tesla_index")
QUERY = "What are Tesla's main risk factors?"
NUMBER_OF_RESULTS = 3

# 1 Data load 
def load_pdf(pdf_path: Path) -> list[dict]:
    """Read the PDF and return the text from each non-empty page."""
    reader = PdfReader(str(pdf_path))
    pages = []

    for page_number, pdf_page in enumerate(reader.pages, start=1):
        page_text = pdf_page.extract_text() or ""
        page_text = re.sub(r"\s+", " ", page_text).strip()

        if page_text:
            pages.append({"page": page_number, "text": page_text})

    if not pages:
        raise SystemExit("No text found. This PDF may be scanned; run OCR first.")

    return pages

# 2 Text chunking
def split_into_chunks(
    pages: list[dict],
    chunk_size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP,
) -> list[dict]:
    """Split page text into smaller pieces, keeping some text between pieces."""
    chunks = []

    for page in pages:
        page_text = page["text"]
        start = 0

        while start < len(page_text):
            end = min(start + chunk_size, len(page_text))

            # Keep whole words together when choosing where a chunk ends.
            if end < len(page_text):
                word_boundary = page_text.rfind(" ", start, end)
                if word_boundary > start:
                    end = word_boundary

            chunks.append({
                "page": page["page"],
                "text": page_text[start:end].strip(),
            })

            if end >= len(page_text):
                break

            # Start the next piece before the previous one ended so they overlap.
            start = max(end - overlap, start + 1)

    return chunks

# 3 Create embeddings
def create_embeddings(
    model: SentenceTransformer, chunks: list[dict]
) -> np.ndarray:
    """Turn each text chunk into a vector that can be compared with other text."""
    chunk_texts = [chunk["text"] for chunk in chunks]

    return model.encode(
        chunk_texts,
        batch_size=32,
        normalize_embeddings=True,
        show_progress_bar=True,
    )
    
# 4 Search for relevant chunks
def search_chunks(
    model: SentenceTransformer,
    chunks: list[dict],
    vectors: np.ndarray,
    query: str,
    number_of_results: int = NUMBER_OF_RESULTS,
) -> list[tuple[float, dict]]:
    """Find the chunks whose embeddings are most similar to the query."""
    query_text = QUERY_PREFIX + query
    query_vector = model.encode([query_text], normalize_embeddings=True)[0]

    # Because the vectors are normalized, their dot product is cosine similarity.
    similarity_scores = vectors @ query_vector
    best_indices = np.argsort(-similarity_scores)[:number_of_results]

    results = []
    for index in best_indices:
        results.append((float(similarity_scores[index]), chunks[index]))

    return results

# helper 
def print_results(results: list[tuple[float, dict]]) -> None:
    """Print each matching passage with its score and PDF page number."""
    for rank, (score, chunk) in enumerate(results, start=1):
        passage = chunk["text"]
        if len(passage) > 400:
            passage = passage[:400] + "..."

        print(f"\n#{rank}  score={score:.3f}  page {chunk['page']}")
        print(passage)
        
# save text 
def save_index(
    folder: Path, chunks: list[dict], vectors: np.ndarray
) -> None:
    """Save vectors, their source text, and the model name for later use."""
    folder.mkdir(exist_ok=True)
    np.save(folder / "vectors.npy", vectors)
    (folder / "chunks.json").write_text(json.dumps(chunks), encoding="utf-8")
    (folder / "model.txt").write_text(MODEL_NAME, encoding="utf-8")
    
def search_with_faiss(
    model: SentenceTransformer,
    chunks: list[dict],
    vectors: np.ndarray,
    query: str,
    number_of_results: int = NUMBER_OF_RESULTS,
) -> list[tuple[float, dict]]:
    """Run the same similarity search using the optional FAISS library."""
    import faiss

    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors.astype("float32"))

    query_text = QUERY_PREFIX + query
    query_vector = model.encode(
        [query_text], normalize_embeddings=True
    ).astype("float32")
    scores, chunk_ids = index.search(query_vector, number_of_results)

    results = []
    for score, chunk_id in zip(scores[0], chunk_ids[0]):
        results.append((float(score), chunks[chunk_id]))

    return results


def main() -> None:
    if not PDF_PATH.exists():
        raise FileNotFoundError(f"Could not find the PDF: {PDF_PATH}")

    print(f"1-Reading PDF: {PDF_PATH}")
    pages = load_pdf(PDF_PATH)

    print("2-Splitting the PDF text into chunks...")
    chunks = split_into_chunks(pages)
    print(f"Found {len(pages)} pages and created {len(chunks)} chunks.")

    print(f"3-Loading embedding model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)

    print("4-Creating an embedding for each chunk...")
    vectors = create_embeddings(model, chunks)
    print(f"Embedding shape: {vectors.shape} (chunks x dimensions)")
    print("First chunk's first 8 numbers:", np.round(vectors[0][:8], 3))

    save_index(INDEX_FOLDER, chunks, vectors)
    print(f"5- Saved the index in: {INDEX_FOLDER}")

    print(f"\nSearching for: {QUERY}")
    results = search_chunks(model, chunks, vectors, QUERY)
    print_results(results)

    try:
        print("\n--- The same search using FAISS ---")
        faiss_results = search_with_faiss(model, chunks, vectors, QUERY)
        print_results(faiss_results)
    except ImportError:
        print("\nInstall faiss-cpu to try the optional FAISS search.")


if __name__ == "__main__":
    main()
