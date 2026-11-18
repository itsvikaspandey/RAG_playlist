import sys, os
import warnings

warnings.filterwarnings("ignore")
os.environ["USER_AGENT"] = "BlueprintAI/1.0"

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    Docx2txtLoader,
    WebBaseLoader,
    DirectoryLoader,
)

# 1. Load a simple Text file (.txt)
text_loader = TextLoader("sample_docs/notes.txt", encoding="utf-8")
text_docs = text_loader.load()
# print("Content Preview:\n", text_docs[0].page_content[:150], "...\n")
# print("Metadata:\n", text_docs[0].metadata)

# 2. Load a PDF file (.pdf)
pdf_loader = PyPDFLoader("sample_docs/annual_report.pdf")
pdf_docs = pdf_loader.load()  # Returns 1 Document per page

# print(f"\n[2] PyPDFLoader: Loaded {len(pdf_docs)} page(s)")
# print("Content Preview (Page 1):\n", pdf_docs[0].page_content[:200], "...\n")
# print("Metadata (Page 1):\n", pdf_docs[0].metadata)

# 3. Load a CSV spreadsheet (.csv)
csv_loader = CSVLoader(file_path="sample_docs/metrics.csv", source_column="metric_name")
csv_docs = csv_loader.load()  # Returns 1 Document per row

# print(f"\n[3] CSVLoader: Loaded {len(csv_docs)} row(s)")
# print("Content Preview (Row 1):\n", csv_docs[0].page_content, "\n")
# print("Metadata (Row 1):\n", csv_docs[0].metadata)

# 4. Load a Microsoft Word Document (.docx)
docx_loader = Docx2txtLoader("sample_docs/company_handbook.docx")
docx_docs = docx_loader.load()

# print(f"\n[4] Docx2txtLoader: Loaded {len(docx_docs)} document")
# print("Content Preview:\n", docx_docs[0].page_content[:180], "...\n")
# print("Metadata:\n", docx_docs[0].metadata)

# 5. Load a live Web Page (URL)
web_loader = WebBaseLoader("https://reference.langchain.com/python/langchain-community/document-loaders")
web_docs = web_loader.load()

# print(f"\n[5] WebBaseLoader: Loaded {len(web_docs)} web document")
# print("Content Preview:\n", web_docs[0].page_content[:160].strip(), "...\n")
# print("Metadata:\n", web_docs[0].metadata)


# 6. Batch load an entire folder of files
dir_loader = DirectoryLoader(
    path="./sample_docs",
    glob="**/*.txt",
    loader_cls=TextLoader,
    use_multithreading=True,
)
folder_docs = dir_loader.load()

print(f"\n[6] DirectoryLoader: Batch loaded {len(folder_docs)} file(s) from folder")
print("First Loaded Doc Metadata:\n", folder_docs[0].metadata)
