import fitz  # PyMuPDF 1
from langdetect import detect, LangDetectException

def extract_text_and_metadata(pdf_bytes: bytes):
    """
    Extracts text, metadata, and language from a PDF file given as bytes.
    Returns: (chunks, metadata_dict)
    """
    text = ""
    metadata = {"title": None, "author": None, "language": None}
    try:
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            # Extract metadata
            doc_meta = doc.metadata or {}
            metadata["title"] = doc_meta.get("title")
            metadata["author"] = doc_meta.get("author")
            # Extract text from all pages
            for page in doc:
                text += page.get_text()
    except Exception as e:
        raise RuntimeError(f"Failed to parse PDF: {e}")

    # Detect language
    try:
        metadata["language"] = detect(text) if text.strip() else None
    except LangDetectException:
        metadata["language"] = None

    # Chunk text (simple split by double newlines or every 1000 chars)
    chunks = [chunk.strip() for chunk in text.split('\n\n') if chunk.strip()]
    if not chunks:
        # fallback: chunk every 1000 chars
        chunks = [text[i:i+1000] for i in range(0, len(text), 1000)] if text else []

    return chunks, metadata