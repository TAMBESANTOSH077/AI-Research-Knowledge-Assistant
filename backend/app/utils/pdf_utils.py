import fitz


def get_pdf_pages(file_path: str) -> int:
    document = fitz.open(file_path)
    total_pages = len(document)
    document.close()
    return total_pages