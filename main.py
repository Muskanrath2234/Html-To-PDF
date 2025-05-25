from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import pdfkit
import uuid

app = FastAPI()

config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")


@app.post("/html-to-pdf/")
async def html_to_pdf(html: str = Form(...)):
    # Unique filename to avoid overwrite
    filename = f"output_{uuid.uuid4().hex}.pdf"

    # Convert HTML string to PDF file
    pdfkit.from_string(html, filename, configuration=config)

    # Return PDF file as response
    return FileResponse(filename, media_type="application/pdf", filename=filename)
