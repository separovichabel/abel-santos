# Transformer Tools

This directory contains tools for converting and translating documents.

## PDF to Markdown Converter

A simple command-line tool to convert PDF files to Markdown format using the docling library.

### Setup

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

### Usage

Basic usage:
```bash
python pdf2md.py input.pdf
```

Specify output file:
```bash
python pdf2md.py input.pdf -o output.md
```

## Markdown Translator

A tool that translates Markdown files from English to Portuguese using the OpenAI API.

### Prerequisites

- OpenAI API key (set as environment variable)
- Python 3.6 or higher
- Virtual environment (same as above)

### Setup

1. Set your OpenAI API key:
   ```bash
   # On Windows (Command Prompt):
   set OPENAI_API_KEY=your_api_key_here

   # On Windows (PowerShell):
   $env:OPENAI_API_KEY="your_api_key_here"

   # On Unix/MacOS:
   export OPENAI_API_KEY=your_api_key_here
   ```

2. Install dependencies (same as above):
   ```bash
   pip install -r requirements.txt
   ```

### Usage

```bash
python translate.py input.md
```

The script will:
1. Read the input Markdown file
2. Send it to OpenAI's GPT-4 for translation
3. Save the translated content to a new file with "_pt.md" suffix

Example:
```bash
# Input file: document.md
python translate.py document.md
# Output file: document_pt.md
```

## Features

### PDF to Markdown
- Converts PDF files to Markdown format
- Preserves text formatting and structure
- Handles errors gracefully
- Supports custom output file paths

### Markdown Translator
- Preserves Markdown formatting
- Maintains links and structure
- Uses GPT-4 for high-quality translation
- Automatic output file naming
- Comprehensive error handling

## Requirements

- Python 3.6 or higher
- docling library
- requests library
- OpenAI API key 