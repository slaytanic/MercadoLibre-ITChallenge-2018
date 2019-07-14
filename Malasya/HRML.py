# This Python file uses the following encoding: utf-8
from HTMLParser import HTMLParser

class HRMLParser(HTMLParser):
    dictionary = {}
    tag_stack = []

    def update(self,dictionary, tag_stack2, attr):
        if tag_stack2[0] == self.tag_stack[-1]:
            if tag_stack2[0] not in dictionary:
                dictionary[tag_stack2[0]] = {}
            if len(attr) == 0:
                return
            dictionary[tag_stack2[0]][attr[0]] = attr[1]
            return
        tmp = tag_stack2[0]
        tag_stack2.pop(0)
        self.update(dictionary[tmp], tag_stack2, attr)

    def get_value(self, dictionary, tag_stack2):
        if len(tag_stack2) == 1:
            try:
                val,key = map(str,tag_stack2[0].split('~'))
                print dictionary[val][key]
            except KeyError:
                # pass
                print '¡No encontrado!'
            return
        tmp = tag_stack2[0]
        tag_stack2.pop(0)
        self.get_value(dictionary[tmp], tag_stack2)

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        tag_stack2 = list(self.tag_stack)
        self.update(self.dictionary, tag_stack2, [])
        for attr in attrs:
            tag_stack2 = list(self.tag_stack)
            self.update(self.dictionary, tag_stack2, attr)
    def handle_endtag(self, tag):
        self.tag_stack.pop(self.tag_stack.index(tag))

def main():
    parser = HRMLParser()
    n,q = map(int,raw_input().split())
    data = ''
    for i in range(n):
        data += raw_input()
    parser.feed(data)
    while q > 0:
        q -= 1
        string = raw_input()
        if '~' not in string:
            print '¡No encontrado!'
            continue
        query = map(str,string.split('.'))
        try:
            parser.get_value(parser.dictionary, query)
        except KeyError:
            # pass
            print '¡No encontrado!'
main()
