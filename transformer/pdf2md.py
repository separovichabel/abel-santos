#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path
from docling.document_converter import DocumentConverter

def convert_pdf_to_markdown(pdf_path, output_path=None):
    """
    Convert a PDF file to Markdown using docling.
    
    Args:
        pdf_path (str): Path to the input PDF file
        output_path (str, optional): Path to save the output Markdown file
    """
    try:
        # Create a Document object from the PDF
        converter = DocumentConverter()
        result = converter.convert(pdf_path)
                
        # Determine output path
        if output_path is None:
            output_path = Path(pdf_path).with_suffix('.md')
        
        # Write the Markdown content to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.document.export_to_markdown())
            
        print(f"Successfully converted {pdf_path} to {output_path}")
        
    except Exception as e:
        print(f"Error converting PDF: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Convert PDF files to Markdown using docling')
    parser.add_argument('pdf_file', help='Path to the input PDF file')
    parser.add_argument('-o', '--output', help='Path to save the output Markdown file (optional)')
    
    args = parser.parse_args()
    convert_pdf_to_markdown(args.pdf_file, args.output)

if __name__ == '__main__':
    main() 