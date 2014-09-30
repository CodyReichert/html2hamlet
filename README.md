html2hamlet
===========

A simple python script that takes an html file and outputs a hamlet file for use with Yesod

#### Usage

Run:
    python parser.py "filename.html"
    
This will output filename.hamlet into the current directory

#### TODO

- cleanup
- Preserver HTML comments
  - Currently it's stripping all comments because comments that end on the same
    line as a closing tag (e.g. <code></ close> --></code>) get removed and the comment would never end.
- Two space indent in target file instead of 1 space.
- Keep BS from putting html and body tags at the top of every file.
