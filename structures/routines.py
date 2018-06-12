from sources import papers
from . import news
import pandas as pd


def get_papers():
    print(papers.SEARCH_URLS.keys())


class HeadlineScrape:
    def __init__(self):
        pass


class SearchRoutine:
    def __init__(self, topic, paper, pages, element):
        """
        A general search routine to get text data from a list of urls
        :param topic: the topic
        :param paper: the paper
        """
        self.topic = topic
        self.pages = pages
        self.paper = news.Paper(paper)
        self.search_urls = self.paper.get_url_list(topic=self.topic,
                                                   pages=self.pages).url_list
        self.element = element
        self.tag = papers.ELEMENTS[self.paper.name][self.element]
        self.raw_data = []
        self.raw_data_list = []
        self.raw_dict = {}
        self.text_data = []
        self.date_data = []

    def scrape_page(self, page):
        search_page = news.Page(self.search_urls[page], name=self.paper.name)
        return search_page.pull_general(tag=self.tag)

    def scrape_text(self, page):
        search_page = news.Page(self.search_urls[page], name=self.paper.name)
        return search_page.pull_text(tag=self.tag)

    def fill_data(self):
        """
        Fill data with the parameters you enter
        :return:
        """
        for i in range(0, self.pages, 1):
            print("Filling " + str(i) + " of " + str(self.pages))
            self.raw_data.append(self.scrape_page(i))

    def unravel_raw(self):
        for item in self.raw_data:
            for piece in item:
                self.raw_data_list.append(piece)

    def sort_data(self):
        """
        THE STAR:
            Summary text in SEARCH:
                - date: .span.text KEY
                - heading: .h2.text
                - summary: .p.text
        THE SUN:

        :return: the text element you want
        """
        for item in self.raw_data_list:
            self.raw_dict[item.span.text] = [item.h2.text, item.p.text]

    def to_frame(self):
        """
        parse the dictionary as a pandas dataframe with the correct orientation
        :return: a pandas dataframe with date indexing
        """
        df = pd.DataFrame.from_dict(self.raw_dict, orient='index')
        df.columns = ['Date', 'Text']
        return df

    def write_csv(self):
        y = self.to_frame()
        y.to_csv()














     
        



    









