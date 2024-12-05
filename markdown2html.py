#!/usr/bin/python3
import sys
import os

def main():
    """Convert a Markdown file to HTML.

    Usage:
        ./markdown2html.py README.md README.html

    Exits with status code 1 if there are errors, or 0 if the operation
    is successful.
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
