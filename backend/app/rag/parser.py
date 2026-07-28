import fitz


def extract_text(pdf_path: str):
    pages = []

    doc = fitz.open(pdf_path)

    for page_num, page in enumerate(doc):

        text = page.get_text()

        pages.append({
            "page": page_num + 1,
            "text": text
        })

    doc.close()

    return pages