# PDF to Markdown Converter

A simple command-line tool to convert PDF files to Markdown format using the docling library.

## Setup

1. Create and activate a virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv

   # On Windows:
   .\venv\Scripts\activate

   # On Unix or MacOS:
   source venv/bin/activate
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Basic usage:
```bash
python pdf2md.py input.pdf
```

Specify output file:
```bash
python pdf2md.py input.pdf -o output.md
```

## Features

- Converts PDF files to Markdown format
- Preserves text formatting and structure
- Handles errors gracefully
- Supports custom output file paths

## Requirements

- Python 3.6 or higher
- docling library 