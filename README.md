html2hamlet
===========

Convert html files to hamlet files


## Usage

Run:
    python parser.py

# TODO

- remove hardcoded html file and allow for command line argument
- create target file name based on input file
- Preserver HTML comments
  - Comments that end on the same line as a closing tag are the problem
  - E.g. '</div>-->'
