import os, ntpath, re, sys, fileinput
from bs4 import BeautifulSoup as bs
from bs4 import Comment

# get file from arg, make a Soup object
html = bs(open(sys.argv[1]),features="html.parser")

# extract comments from html
comments = html.findAll(text=lambda text:isinstance(text, Comment))
[comment.extract() for comment in comments]

# write prettified html to intermediate file
# This also puts all end tags on their own line
prettyHtml = 'result.html'
with open(prettyHtml, 'w') as resultout:
    resultout.write(html.prettify('utf-8').decode("utf-8"))

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
voidTagPattern = re.compile(r".*<(.*)/>")

# functions that change classes, id's, img src's to hamlet syntax
def changeClasses(matched):
  matched = matched.split()
  newClasses = []
  for match in matched:
    newClasses.append( "." + match)
  return ' '.join(newClasses)

def changeIds(matched):
  matched = matched.split()
  newIds= []
  for match in matched:
    newIds.append( "#" + match)
  return ' '.join(newIds)

def changeImgLinks(matched):
  fileExtension = os.path.splitext(matched[1])[1]
  fileName = os.path.splitext(ntpath.basename(matched[1]))[0]
  tagOpen = matched[0]
  tagSrc = '@{StaticR_img_' + fileName + '_' + fileExtension[1:] + '}'
  tagClose = matched[2][1:]
  newImgTag = tagOpen + tagSrc + tagClose
  return newImgTag

for line in fileinput.input(final, inplace=True):
  line = re.sub(r"class=\"(.*?)\"", lambda m: changeClasses(m.group(1)), line.rstrip())
  line = re.sub(r"id=\"(.*?)\"", lambda m: changeIds(m.group(1)), line.rstrip())
  line = re.sub(r'(.*<img.*src=)("(?!http).*?)(".*)', lambda m: changeImgLinks(m.groups()), line.rstrip())
  line = re.sub(r"(.*)<(.*)/>", r"\1<\2>", line.rstrip())
  print(line)

# cleanup intermediate file
os.remove(prettyHtml)
