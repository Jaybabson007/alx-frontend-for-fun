#!/usr/bin/python3
"""
A Python script to convert a Markdown file to HTML.

Usage:
    ./markdown2html.py [input_file] [output_file]

Args:
    input_file: name of the Markdown file to be converted
    output_file: name of the output HTML file

Example:
    ./markdown2html.py README.md README.html
"""

import argparse
import pathlib
import re


def convert_md_to_html(input_file, output_file):
    '''
    This function Converts markdown file to HTML file
    '''
    # This Reads the contents of the input file
    with open(input_file, encoding='utf-8') as f:
        md_content = f.readlines()

    html_content = []
    for line in md_content:
        # This Checks if the line is a heading
        match = re.match(r'(#){1,6} (.*)', line)
        if match:
            # This Gets the level of the heading
            h_level = len(match.group(1))
            # This Gets the content of the heading
            h_content = match.group(2)
            # This Appends the HTML equivalent of the heading
            html_content.append(f'<h{h_level}>{h_content}</h{h_level}>\n')
        else:
            html_content.append(line)

    # This Writes the HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(html_content)


if __name__ == '__main__':
    #This Parses command-line arguments
    parser = argparse.ArgumentParser(description='Convert markdown to HTML')
    parser.add_argument('input_file', help='path to input markdown file')
    parser.add_argument('output_file', help='path to output HTML file')
    args = parser.parse_args()

    # This Checks if the input file exists
    input_path = pathlib.Path(args.input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    # This Converts the markdown file to HTML
    convert_md_to_html(args.input_file, args.output_file)