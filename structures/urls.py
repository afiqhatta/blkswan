import requests

from bs4 import BeautifulSoup


class Url:
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return str(self.url)

    def request(self):
        return requests.get(self.url)

    def parsed_request(self):
        return BeautifulSoup(self.request().text,
                             'html.parser')

    def request_all(self, span, class_=None):
        return self.parsed_request().find_all(span, class_=class_)

    def pull_text(self, span, class_):
        return [item.text for item
                in self.request_all(span, class_)]

    def pull_url(self, span, class_):
        return [item.a.get('href') for item
                in self.request_all(span, class_)]


class UrlGroup:
    def __init__(self, url_list):
        self.url_list = [Url(item) for item in url_list]

    def display_entries(self):
        for item in self.url_list:
            print(item.url)

    def slow_get(self, span, class_=None):
        result = []
        for item in self.url_list:
            result.append(item.pull_text(span, class_))
        return result
















