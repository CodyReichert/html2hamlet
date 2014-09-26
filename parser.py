import re
# from bs4 import BeautifulSoup as bs

rawHtml = open('homepage.html').readlines()
html = bs(rawHtml)

pattern = re.compile(r"\s*</.*>")

for line in rawHtml:
  if pattern.match(line) is None:
    print line

# print(html.prettify())
