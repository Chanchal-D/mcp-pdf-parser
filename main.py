from fastapi import FastAPI, File, UploadFile, HTTPException
from parser import extract_text_and_metadata

app = FastAPI(title="mcp-pdf-parser")

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    pdf_bytes = await file.read()
    try:
        chunks, metadata = extract_text_and_metadata(pdf_bytes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"chunks": chunks, "metadata": metadata}

@app.get("/")
def read_root():
    return {"message": "Welcome to the MCP PDF Parser API!"}