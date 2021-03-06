'''
If you are pasting this code from github, add the following files:
- diff.html
- html.txt
- renderhtml.txt
'''

import difflib
from requests_html import HTMLSession

user_input = input("Enter a URL to generate the diff: ")

session = HTMLSession()

#grab the raw html
r = session.get(user_input)
reg_html = r.text

#write it to file
with open('html.txt', 'w') as f:
  for line in reg_html:
      f.write(line)

#grab the rendered HTML
try:
  r.html.render(timeout=40)
  render_html = r.html.html
except TimeoutError:
  print("Try increasing the timeout value")
  # "timeout=___"

#write it to file
with open('renderhtml.txt', 'w') as f:
  for line in render_html:
    f.write(line)

#gather both HTML files to create the diff
fromfile = 'html.txt'
tofile = 'renderhtml.txt'
fromlines = open(fromfile, 'r').readlines()
tolines = open(tofile, 'r').readlines()

#creates the diff file
diff = difflib.HtmlDiff().make_file(fromlines,tolines,fromfile,tofile)

#write the diff file
with open('diff.html', 'w') as f:
    f.write(diff)

#confirmation message
print("Done!")
