import json
import urllib
import html2text
from bs4 import BeautifulSoup

bushfile = open('input_bush_execorders.txt', 'w')
json_content = json.loads(open('bushexecorders.json').read())
for orders in json_content['results']:
    urllib.request.urlretrieve(orders['body_html_url'], 'tmp.txt')
    html_content = open('tmp.txt').read()
    soup = BeautifulSoup(html_content)
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    #delete last 4 lines, unwanted info
    newline_index = text.rfind("\n")
    text = text[:newline_index]
    newline_index = text.rfind("\n")
    text = text[:newline_index]
    newline_index = text.rfind("\n")
    text = text[:newline_index]
    newline_index = text.rfind("\n")
    text = text[:newline_index]
    text += '\n'
    bushfile.write(text)
    print("Write complete")
print("All writing complete")