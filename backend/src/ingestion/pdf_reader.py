from pypdf import PdfReader
from pathlib import Path


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract all text from a PDF file.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def save_text_to_file(text: str, output_path: str):
    """
    Save extracted text to a file.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


def main():

    pdf_path = Path("backend/data/rag_survey.pdf")
    output_path = Path("backend/data/extracted_text.txt")

    extracted_text = extract_text_from_pdf(pdf_path)

    print(extracted_text[:1000])

    save_text_to_file(extracted_text, output_path)

    print(f"\nText saved to {output_path}")


if __name__ == "__main__":
    main()