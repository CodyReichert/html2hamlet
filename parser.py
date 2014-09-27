import re
from bs4 import BeautifulSoup as bs

# read the original html file, get a Soup object
rawHtml = open('homepage.html').read()
html = bs(rawHtml)

# Just creating a new file manually for now
result = 'result.html'

# write the prettified html to a new file
# This also puts all end tags on their own line
with open(result, 'w') as resultout:
    resultout.write(html.prettify('utf-8'))


# regex pattern to find end tags
pattern = re.compile(r"\s*</.*>")

# open prettified file for parsing
newHtml = open(result).readlines()

# create final target file
new = 'homepage.hamlet'

# write all lines except end tags to target file
for line in newHtml:
  if pattern.match(line) is None:
    print line
    with open(new, 'a') as newout:
      newout.write(line)
