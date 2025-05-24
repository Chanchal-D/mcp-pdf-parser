# from fastapi import FastAPI, File, UploadFile, HTTPException
from pdf_parser import extract_text_and_metadata
import logging
import requests
import io
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-pdf-parser")
def get_logger(name: str):
    logger = logging.getLogger(name)
    return logger

logger = get_logger(__name__)

# app = FastAPI(title="mcp-pdf-parser")

# @mcp.tool()
# async def extract_text(file: UploadFile = File(...)):
#     if file.content_type != "application/pdf":
#         raise HTTPException(status_code=400, detail="Only PDF files are supported.")
#     pdf_bytes = await file.read()
#     try:
#         chunks, metadata = extract_text_and_metadata(pdf_bytes)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#     return {"chunks": chunks, "metadata": metadata}


@mcp.tool()
async def read_local_pdf(path: str) -> Dict[str, Any]:
    """Read text content from a local PDF file.
        Args-> path: local file path of the PDF File
    """
    try:
        with open(path, 'rb') as file:
            pdf_bytes = file.read()
            chunks, metadata = extract_text_and_metadata(pdf_bytes)
            return {
                "success": True,
                "data": {
                    "chunks": chunks,
                    "metadata": metadata
                }
            }
    except FileNotFoundError:
        logger.error(f"PDF file not found: {path}")
        return {
            "success": False,
            "error": f"PDF file not found: {path}"
        }
    except Exception as e:
        logger.error(str(e))
        return {
            "success": False,
            "error": str(e)
        }


@mcp.tool()
async def read_pdf_url(url: str) -> Dict[str, Any]:
    """Read text content from a PDF URL.
        Args-> url: Valid URL of the PDF.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        pdf_file = io.BytesIO(response.content)
        pdf_bytes = response.content
        chunks, metadata = extract_text_and_metadata(pdf_bytes)
        return {
            "success": True,
            "data": {
                "chunks": chunks,
                "metadata": metadata
            }
        }
    except requests.RequestException as e:
        logger.error(f"Failed to fetch PDF from URL: {str(e)}")
        return {
            "success": False,
            "error": f"Failed to fetch PDF from URL: {str(e)}"
        }
    except Exception as e:
        logger.error(str(e))
        return {
            "success": False,
            "error": str(e)
        }



@mcp.tool()
def read_root():
    return {"message": "Welcome to the MCP PDF Parser API!"}


if __name__ == "__main__":
    mcp.run(transport="stdio")