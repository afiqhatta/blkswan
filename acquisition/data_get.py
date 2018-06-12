#!/usr/bin/env python3.5


import requests
from bs4 import BeautifulSoup


class Chunk:
    def __init__(self, url):
        self.url = url
        self.text = self.test()
        self.content = self.get()
        self.raw = None

    def test(self):
        return requests.get(self.url).text

    def get(self):
        return BeautifulSoup(self.text, 'html.parser')

    def find(self, span, class_):
        self.raw = self.content.find_all(span, class_)
        return self.content.find_all(span, class_)

    def attr(self, element):
        return self.raw.get(element)


if __name__ == "__main__":
    pass
