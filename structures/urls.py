import requests

from bs4 import BeautifulSoup
from sources import papers


def get_papers():
    print(papers.SEARCH_URLS.keys())


class HeadlineScrape:
    def __init__(self):
        pass


class SearchRoutine:
    def __init__(self):
        pass


class Paper:
    def __init__(self, name):
        self.name = name
        self.s_url = papers.SEARCH_URLS[self.name]
        self.h_url = papers.HOME_PAGES[self.name]

    def paper_search_url(self):
        print(papers.SEARCH_URLS[self.name])

    def paper_homepage(self):
        print(papers.HOME_PAGES[self.name])

    def get_search_page(self, page, topic):
        return ''.join([self.s_url[0], str(topic),
                        self.s_url[2], str(page)])

    def get_search_url(self, pages, topic):
        return Url(self.get_search_page(pages, topic))

    def get_url_list(self, pages, topic):
        url_list = []
        for x in range(0, pages, 1):
            url_list.append(self.get_search_page(x, topic))
        return UrlGroup(url_list)


class Page(Paper):
    def __init__(self, url, name):
        super().__init__(name=name)
        self.url = Url(url)
        self.text = ''
        self.urls = []
        self.text_tags = papers.TEXT_TAGS[self.name]

    def text_tags(self):
        print(self.text_tags)

    def list_elements(self):
        print(self.text_tags.keys())

    def get_links(self, attr):
        return self.text_tags[str(attr)]

    def get_body_links(self):
        return self.text_tags['body']

    def get_url_links(self):
        return self.text_tags['urls']

    def pull_text_tags(self, tag):
        return self.url.pull_text(tag['span'], tag['class'])

    def pull_url_tags(self, tag):
        return self.url.pull_url(tag['span'], tag['class'])

    def pull_urls(self):
        tag = self.get_url_links()
        return self.pull_url_tags(tag)

    def get_body_raw(self):
        tag = self.get_body_links()
        return self.pull_text_tags(tag)  # insert required tags for body

    def get_urls_raw(self):
        tag = self.get_url_links()
        return self.pull_url_tags(tag)  # insert required tags for url links from each newspaper

    def get_full_urls(self):
        return [''.join([self.h_url[:-1], item])
                for item in self.get_urls_raw()]


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














