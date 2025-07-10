import os, sys
from html.parser import HTMLParser

data_path = "data/messages2.html"
f = open(data_path)
# print(f.read())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed(f.read())

if __name__ == '__main__':
    sys.exit(MyHTMLParser())