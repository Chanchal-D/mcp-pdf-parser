# MCP PDF Parser

A FastAPI microservice for extracting and chunking text from PDF files, with automatic metadata and language detection.

## Features

- **POST `/extract-text/`**: Upload a PDF and receive extracted text chunks and metadata (title, author, language).
- **Automatic language detection** using `langdetect`.
- **Metadata extraction** (title, author) from PDF.
- **Simple text chunking** for easier downstream processing.
- **Swagger UI** for easy testing.

## Project Structure

```
mcp-pdf-parser/
├── main.py         # FastAPI entry point
├── parser.py       # PDF parsing and logic
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.8+
- [PyMuPDF (`pymupdf`)](https://pymupdf.readthedocs.io/)
- [langdetect](https://pypi.org/project/langdetect/)
- fastapi
- uvicorn
- python-multipart

Install dependencies:

```bash
pip install fastapi uvicorn pymupdf langdetect python-multipart
```

## Usage

### 1. Start the server

```bash
uvicorn main:app --reload
```

### 2. Test the API

- Open [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.
- Use the `/extract-text/` endpoint to upload a PDF and view the response.

#### Example cURL

```bash
curl -X POST "http://localhost:8000/extract-text/" -F "file=@yourfile.pdf"
```

### 3. Example Response

```json
{
  "chunks": [
    "First chunk of text...",
    "Second chunk of text..."
  ],
  "metadata": {
    "title": "Sample PDF",
    "author": "John Doe",
    "language": "en"
  }
}
```

## Endpoints

- `POST /extract-text/`  
  Upload a PDF file. Returns extracted text chunks and metadata.

- `GET /`  
  Welcome message.

## Notes

- Only PDF files are supported.
- Language detection may not be accurate for very short or non-text PDFs.
- Text chunking is basic (by double newlines or every 1000 characters).

---

**MIT License**