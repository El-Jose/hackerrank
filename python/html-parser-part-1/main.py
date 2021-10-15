from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        for a,b in attrs:
            print(f'-> {a} > {b}')
    def handle_endtag(self, tag):
        print(f'End   : {tag}')
    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        for a,b in attrs:
            print(f'-> {a} > {b}')

s = (''.join(input() for _ in range(int(input()))))
parser = MyHTMLParser()
parser.feed(s)

