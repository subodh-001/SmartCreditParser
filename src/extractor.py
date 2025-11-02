import pdfplumber
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(file_path):
    
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                content = page.extract_text()
                if content:
                    text += content + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")

    if not text.strip():
        print("[OCR] Using OCR fallback (image-based PDF detected)...")
        images = convert_from_path(file_path)
        for img in images:
            text += pytesseract.image_to_string(img)

    return text
