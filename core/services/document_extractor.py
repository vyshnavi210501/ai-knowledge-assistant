from pypdf import PdfReader
import os

def pdf_extractor(file_path):
    """
    Extracts text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF file.
    """
    try:
        with open(file_path, "rb") as file:
            pdf_reader = PdfReader(file)
            pages_text = []
            for page in pdf_reader.pages:
                line = page.extract_text()

                if line:
                    pages_text.append(line)

            return "\n".join(pages_text)
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {e}")

def txt_extractor(file_path):
    """
    Extracts text from a TXT file.

    Args:
        file_path (str): The path to the TXT file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        raise ValueError(f"Error extracting text from TXT: {e}")

def extract_text_from_file(file_path):
    """
    Extracts text from a file based on its extension.

    Args:
        file_path (str): The path to the file.
    """
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return pdf_extractor(file_path)
    elif extension == ".txt":
        return txt_extractor(file_path)
    else:
        raise ValueError("Unsupported file type. Only PDF and TXT files are supported.")

def add_file_content_to_database(file_path, document_instance):
    """
    Extracts text from a file and adds it to the database.

    Args:
        file_path (str): The path to the file.
        document_instance (Document): The Document model instance to update.
    """
    try:
        extracted_text = extract_text_from_file(file_path)
        document_instance.content = extracted_text
        document_instance.save()
    except Exception as e:
        raise ValueError(f"Error adding file content to database: {e}")