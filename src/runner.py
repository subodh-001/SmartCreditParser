from src.extractor import extract_text_from_pdf
from src.bank_parsers import parse_hdfc_statement
import argparse

def process_statement(file_path):
    print(f"Processing HDFC statement: {file_path}")
    text = extract_text_from_pdf(file_path)
    print("Text extraction successful.\n")

    data = parse_hdfc_statement(text)

    print("--- Extracted Data ---")
    for key, value in data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HDFC Credit Card Statement Parser")
    parser.add_argument("--file", required=True, help="Path to HDFC statement PDF")
    args = parser.parse_args()
    process_statement(args.file)
