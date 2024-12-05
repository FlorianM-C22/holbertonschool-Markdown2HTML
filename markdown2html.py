#!/usr/bin/python3
"""Convert Markdown files to HTML format."""

import sys
import os


def convert_headings(markdown_text):
    """Placeholder for future heading conversion."""
    return markdown_text


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)
    
    try:
        with open(markdown_file, 'r') as f:
            markdown_content = f.read()
        
        html_content = convert_headings(markdown_content)
        
        with open(output_file, 'w') as f:
            f.write(html_content)
            
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")
        sys.exit(1)