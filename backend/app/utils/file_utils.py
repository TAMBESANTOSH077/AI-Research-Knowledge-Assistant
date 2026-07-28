import fitz


def get_pdf_pages(file_path: str) -> int:
    doc = fitz.open(file_path)
    pages = len(doc)
    doc.close()
    return pages