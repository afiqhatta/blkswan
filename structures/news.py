from .urls import Url, UrlGroup
from sources import papers

"""
This module stores necessary newspaper classes so you can access what you need in terms of data. 
"""


class Paper:
    def __init__(self, name):
        """
        Create an instance of a class of a newspaper from your available newspapers.
        Allows access to the home url and search url data.
        :param name: the newspaper name from the sources.papers database.
        """
        self.name = name
        self.s_url = papers.SEARCH_URLS[self.name]
        self.h_url = papers.HOME_PAGES[self.name]

    def paper_search_url(self):
        """
        Outputs base search urls from the newspaper class
        :return: a url string
        """
        print(papers.SEARCH_URLS[self.name])

    def paper_homepage(self):
        """
        Outputs the homepage url from your selected newspaper
        :return: a url string of the homepage
        """
        print(papers.HOME_PAGES[self.name])

    def get_search_page(self, page, topic):
        """
        Find a particular search url string
        :param page: what page of search you require
        :param topic: the search entry
        :return: the full url for searching
        """
        return ''.join([self.s_url[0], str(topic),
                        self.s_url[2], str(page)])

    def get_search_url(self, pages, topic):
        """
        Get the url class for a particular search query
        :param pages: what page of search you require
        :param topic: the search entry
        :return: a Url class for the search link
        """
        return Url(self.get_search_page(pages, topic))

    def get_url_list(self, pages, topic):
        """
        Get a url list class for multiple pages of search
        :param pages: the range of pages of search from 0 to pages
        :param topic: the search entry
        :return: a UrlGroup class of search urls
        """
        url_list = []
        for x in range(0, pages, 1):
            url_list.append(self.get_search_page(x, topic))
        return UrlGroup(url_list)


class Page(Paper):
    def __init__(self, url, name):
        """
        a class representation of a certain page of your newspaper. It contains properties including urls and text.
        You don't need to instance this class; only use the child classes for search and home
        :param url: the url of the page
        :param name: the name of the underlying paper, so you can access its properties
        """
        super().__init__(name=name)
        self.url = Url(url)
        self.text = ''
        self.urls = []
        self.text_tags = None  # a span and class dict for what you want

    def text_tags(self):
        """
        :return: the tags in question
        """
        print(self.text_tags)

    def list_elements(self):
        """
        :return: the possible things to search for in a page
        """
        print(self.text_tags.keys())

    def get_links(self, attr):
        """
        :param attr: the element you want to search for
        :return: the relevant tag
        """
        return self.text_tags[str(attr)]

    def pull_text(self, tag):
        """
        Function to pull from raw body tags
        :param tag: tags specific to the newspaper and page
        :return: the text data from the newspaper
        """
        return self.url.pull_text(tag['span'], tag['class'])

    def pull_general(self, tag):
        """
        Find all the html elements of a div
        :param tag:
        :return: BeautifulSoup html list
        """
        return self.url.request_all(tag['span'], tag['class'])


class Home(Page):
    def __init__(self, name):
        super().__init__(url=self.s_url, name=name)


class Search(Page):
    def __init__(self, url, name):
        """
        The class specific to search pages of newspapers
        :param url: this is the url of the search page, can generate this via the urls module
        :param name: the name of the underlying newspaper
        """
        super().__init__(url=url, name=name)
        self.text_tags = papers.ELEMENTS[self.name]

    def get_body_links(self):
        """
        Finds the tags for the body summary text in a page
        :return: a dictionary for span and class tags for the body content
        """
        return self.text_tags['body']

    def get_url_links(self):
        """
        Finds the url links for the results of a search query
        :return: a dict of span and class tags to get url content
        """
        return self.text_tags['urls']

    def pull_url_tags(self, tag):
        """
        Helper function to pull url elements
        :param tag: tags specific to the newspaper and page
        :return: the extension urls from the newspaper
        """
        return self.url.pull_url(tag['span'], tag['class'])

    def pull_urls(self):
        """
        :return: the extension urls from the search page
        """
        tag = self.get_url_links()
        return self.pull_url_tags(tag)

    def get_body_raw(self):
        """
        :return: all body text from the search page in a list
        """
        tag = self.get_body_links()
        return self.pull_text(tag)

    def get_urls_raw(self):
        """
        :return: get all extension urls from the search page in a list
        """
        tag = self.get_url_links()
        return self.pull_url_tags(tag)  # insert required tags for url links from each newspaper

    def get_full_urls(self):
        """
        :return: get a full url list of links in the search page
        """
        return [''.join([self.h_url[:-1], item])
                for item in self.get_urls_raw()]



