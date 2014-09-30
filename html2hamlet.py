import os, re, sys, fileinput
from bs4 import BeautifulSoup as bs
from bs4 import Comment

# get the original html file, make a Soup object
with open(sys.argv[1]) as rawHtml:
  html = bs(rawHtml.read())

# Create an intermediate file manually for now
result = 'result.html'

# extract comments from html
comments = html.findAll(text=lambda text:isinstance(text, Comment))
[comment.extract() for comment in comments]

# write the prettified html to a new file
# This also puts all end tags on their own line
with open(result, 'w') as resultout:
    resultout.write(html.prettify('utf-8'))


# regex pattern to find end tags
pattern = re.compile(r"\s*</.*>")

# open prettified file for parsing
newHtml = open(result).readlines()

# create final target file
finalName = os.path.splitext(str(sys.argv[1]))[0]
final = finalName + '.hamlet'

# write all lines except end tags to target file
with open(final, 'w') as finalout:
  for line in newHtml:
    if pattern.match(line) is None:
      finalout.write(line)

# function far replace html with hamlet syntax for classes
def changeClasses(matched):
  matched = matched.split()
  newClasses = []
  for match in matched:
    newClasses.append( "." + match)
  return ' '.join(newClasses)

# replace html classes with hamlet syntax
classPattern = re.compile(r".*class=\".*\"")
for line in fileinput.input(final, inplace=True):
  if classPattern.match(line) or line.rstrip():
    line = re.sub(r"class=\"(.*?)\"", lambda m: changeClasses(m.group(1)), line.rstrip())
    print line

# cleanup intermediate file
os.remove(result)
