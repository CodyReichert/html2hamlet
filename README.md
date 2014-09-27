html2hamlet
===========

A simple python script that takes an html file and outputs a hamlet file for use with Yesod

## Usage

Run:
    python parser.py <filename.html>

# TODO

- cleanup
- name target file based on input file name
- Preserver HTML comments
  - Currently it's stripping all comments because comments that end on the same
    line as a closing tag (e.g. "</div> -->") get removed and the comment never ends.
- Change class and id names to Shakespearean format (e.g. class="foo" -> .foo)
- Two space indent in target file instead of 1 space.
