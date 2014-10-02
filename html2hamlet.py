import os, re, sys, fileinput
from bs4 import BeautifulSoup as bs
from bs4 import Comment

# get file from arg, make a Soup object
html = bs(open(sys.argv[1]))

# extract comments from html
comments = html.findAll(text=lambda text:isinstance(text, Comment))
[comment.extract() for comment in comments]

# write prettified html to intermediate file
# This also puts all end tags on their own line
prettyHtml = 'result.html'
with open(prettyHtml, 'w') as resultout:
    resultout.write(html.prettify('utf-8'))

# regex pattern to find end tags
pattern = re.compile(r"\s*</.*>")

# create final target file
finalName = os.path.splitext(str(sys.argv[1]))[0]
final = finalName + '.hamlet'

# write all lines except end tags to target file
with open(final, 'w') as finalout:
  for line in open(prettyHtml).readlines():
    if pattern.match(line) is None:
      finalout.write(line)

# class and id regex pattern match
classPattern = re.compile(r".*class=\".*\"")
idPattern = re.compile(r".*id=\".*\"")
# function far replace html with hamlet syntax for classes
def changeClasses(matched):
  matched = matched.split()
  newClasses = []
  for match in matched:
    newClasses.append( "." + match)
  return ' '.join(newClasses)
def changeIds(matched):
  matched = matched.split()
  newClasses = []
  for match in matched:
    newClasses.append( "#" + match)
  return ' '.join(newClasses)

# replace html classes with hamlet syntax
# TODO: refactor, no need to open the file twice
for line in fileinput.input(final, inplace=True):
  if classPattern.match(line) or line.rstrip():
    line = re.sub(r"class=\"(.*?)\"", lambda m: changeClasses(m.group(1)), line.rstrip())
    print line
for line in fileinput.input(final, inplace=True):
  if idPattern.match(line) or line.rstrip():
    line = re.sub(r"id=\"(.*?)\"", lambda m: changeIds(m.group(1)), line.rstrip())
    print line

# cleanup intermediate file
os.remove(prettyHtml)
