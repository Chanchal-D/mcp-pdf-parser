from fastapi import FastAPI, File, UploadFile, HTTPException
from parser import extract_text_from_pdf

app = FastAPI()

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    pdf_bytes = await file.read()
    try:
        text = extract_text_from_pdf(pdf_bytes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing PDF: {str(e)}")
    return {"text": text}

@app.get("/")
def read_root():
    return {"message": "Welcome to the MCP PDF Parser API!"}