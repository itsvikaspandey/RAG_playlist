from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

# Locate and load the PDF
pdf_path = Path("data/tsla-20251231-gen.pdf")
if not pdf_path.exists():
    pdf_path = Path("RAG-SERIES/data/tsla-20251231-gen.pdf")

loader = PyPDFLoader(str(pdf_path))
pages = loader.load()

# Extract Page 5 (Item 1: Business Overview)
text = pages[4].page_content.replace("\t", " ")
# print(f"Total characters on Page 5: {len(text)}")
# print(text[:250].strip())


### Basic Chunking (Fixed-Size Character Slicing) in Pure Python
def basic_chunk(text: str, chunk_size: int = 400, overlap: int = 0) -> list[str]:
    """
    Slices raw text by a fixed character window with optional overlap.
    
    Args:
        text: The raw input string to split.
        chunk_size: Maximum character length for each chunk.
        overlap: Number of characters to repeat across adjacent chunks.
        
    Returns:
        List of chunk strings.
    """
    step = chunk_size - overlap
    if step <= 0:
        raise ValueError("chunk_size must be strictly greater than overlap")
    return [text[i : i + chunk_size] for i in range(0, len(text), step)]

naive_chunk = basic_chunk

# Test 1: Slicing a sample sentence with 25 characters
sample = "We are focused on bringing artificial intelligence into the real world."
sample_chunks = basic_chunk(sample, chunk_size=25, overlap=0)
print("--- Test 1: Basic Chunking on Sample Sentence (chunk_size=25) ---")
for i, chunk in enumerate(sample_chunks):
    print(f"Chunk {i}: {repr(chunk)}")
    
from langchain_text_splitters import CharacterTextSplitter

splitter_overlap = CharacterTextSplitter(
    separator=" ",
    chunk_size=400,
    chunk_overlap=50
)

chunks_overlap = splitter_overlap.split_text(text)
print(f"Total chunks with overlap: {len(chunks_overlap)}")
print("Chunk 1 ends:  ", chunks_overlap[0][-60:].strip())
print("Chunk 2 starts:", chunks_overlap[1][:60].strip())