# MCP PDF Parser

This project provides tools to extract text and metadata from PDF files, either from local files or URLs, using Python. It is designed to be used as part of the MCP (Modular Command Platform) framework, but can be adapted for other uses.

## Features
- Extracts text and metadata (title, author, language) from PDF files.
- Supports reading PDFs from local file paths or remote URLs.
- Provides MCP tool endpoints for integration.

## File Overview

### main.py
- Implements the core MCP tools:
  - `read_local_pdf(path: str)`: Reads and extracts text/metadata from a local PDF file.
  - `read_pdf_url(url: str)`: Reads and extracts text/metadata from a PDF at a given URL.
  - `read_root()`: Returns a welcome message.
- Uses `extract_text_and_metadata` from `pdf_parser.py` for PDF processing.
- Can be run as a script with `mcp.run(transport="stdio")`.

### api_main.py
- (Currently empty, but typically would be used to expose the same tools via a web API, e.g., using FastAPI.)
- You can implement a FastAPI app here to provide HTTP endpoints for PDF parsing.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/Chanchal-D/mcp-pdf-parser>
   cd mcp-pdf-parser
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Ensure you have the following packages (add to `requirements.txt` if missing):
   - PyMuPDF (fitz)
   - langdetect
   - requests
   - mcp (and its dependencies)

## Usage

### As MCP Tool
Run the main script:
```bash
python main.py
```

### Example: Read Local PDF
```python
from main import read_local_pdf
result = await read_local_pdf('path/to/file.pdf')
print(result)
```

### Example: Read PDF from URL
```python
from main import read_pdf_url
result = await read_pdf_url('https://example.com/file.pdf')
print(result)
```

### Extending with FastAPI (api_main.py)
You can implement a FastAPI app in `api_main.py` to provide HTTP endpoints for PDF parsing. Uncomment and adapt the FastAPI code in `main.py` as needed.

## License
MIT License