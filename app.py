import os
import json
from utils.pdf_processor import process_pdf

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    
    print(f"Looking for PDFs in: {input_dir}")
    
    # Process all PDFs in input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.pdf'):
            print(f"Processing file: {filename}")
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.json")
            
            result = process_pdf(input_path)
            
            with open(output_path, 'w') as f:
                json.dump(result, f, indent=2)
            
            print(f"Created output: {output_path}")
    
    print("All files processed. Exiting.")

if __name__ == "__main__":
    main()