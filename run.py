from src.runner import process_statement
import argparse

def main():
    parser = argparse.ArgumentParser(description="Run HDFC Statement Parser")
    parser.add_argument("--file", required=True, help="Path to PDF file")
    args = parser.parse_args()

    process_statement(args.file)

if __name__ == "__main__":
    main()
