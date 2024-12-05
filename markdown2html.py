#!/usr/bin/python3
"""Convert Markdown files to HTML format."""

import sys
import os


def convert_headings(markdown_text):
    """Convert markdown headings to HTML format."""
    html_lines = []
    for line in markdown_text.split('\n'):
        heading_level = 0
        for char in line:
            if char == '#':
                heading_level += 1
            else:
                break
        
        if 0 < heading_level <= 6:
            content = line[heading_level:].strip()
            html_lines.append(f'<h{heading_level}>{content}</h{heading_level}>')
        else:
            html_lines.append(line)
    
    return '\n'.join(html_lines)


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