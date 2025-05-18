#!/usr/bin/env python3

import os
import sys
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv

def translate_markdown(input_file):
    """
    Translate a Markdown file from English to Portuguese using OpenAI API.
    
    Args:
        input_file (str): Path to the input Markdown file
    """
    # Check if file exists and is a .md file
    if not input_file.endswith('.md'):
        print("Error: Input file must be a .md file")
        sys.exit(1)
    
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)

    load_dotenv()
    client = OpenAI()

    # # load the source file
    # file = client.files.create(
    #     file=open(input_file, "rb"),
    #     purpose="user_data"
    # )

    # Load your original Markdown or plain text file
    with open(input_file, "r", encoding="utf-8") as f:
        file_content = f.read()

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "You are a translator. Translate this file to portuguese maintaining the file structure and formating. When translating a biblical reference abreviation in a old roman numeric format (ex. Prov. xxii. 19, 20, 21) actualize it to a comtemporary numeric format (ex. Prov. 22:19, 20, 21). Translate the next message.",
                    },
                    {
                        "type": "input_text",
                        "text": file_content
                    }
                ]
            }
        ]
    )

    # Create output filename
    output_file = str(Path(input_file).with_suffix('')) + '_pt.md'

    # Write translated content to file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(response.output_text)
        print(f"Translation complete! Output saved to: {output_file}")
    except Exception as e:
        print(f"Error writing output file: {str(e)}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python translate.py <input.md>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    translate_markdown(input_file)

if __name__ == '__main__':
    main() 