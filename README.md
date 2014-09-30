html2hamlet
===========

A simple python script that takes an html file and outputs a hamlet file for use with Yesod

#### Usage

Run:
    python parser.py <filename.html>

#### TODO

- cleanup
- name target file based on input file name
- Preserver HTML comments
  - Currently it's stripping all comments because comments that end on the same
    line as a closing tag (e.g. <code></ close> --></code>) get removed and the comment would never end.
- Change class and id names to Shakespearean format (e.g. class="foo" -> .foo)
- Two space indent in target file instead of 1 space.
- Keep BS from putting html and body tags at the top of every file.
