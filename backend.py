import requests
from itertools import repeat
from bs4 import BeautifulSoup
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool


# create a newspaper class with url metadata


class DataType:
    def __init__(self):
        self.name = ''
        self.type = ''
        self.description =''


class Newspaper:
    def __init__(self, name, kinds):
        self.home_url = Url(name)
        self.kinds = kinds
        self.available_types = []
        self.available_streams = []

    def set_stream(self):
        self.available_streams.append(Url())


class DataStream:
    def __init__(self, name):
        self.name = name
        self.data = None
        self.url = None
        self.url_group  = UrlGroup()
        self.url_list = self.url_group.url_list

    def pull(self, span, class_):
        self.data = [item.text for item in
                     BeautifulSoup(requests.get(self.url).text,
                                   'html.parser').find_all(span, class_=class_)]

    def pull_multi(self, pages):
        pass
        # self.data = [item for sublist in ThreadPool(pages).starmap(self.pull(span, class), zip(urls, repeat(info))) for item in sublist]


class DataStructureFrame:
    def __init__(self, data, description=None):
        self.data = data
        self.description = description
        self.df = pd.DataFrame(self.data)

    def __repr__(self):
        return 'Data frame object %s' % self.description

    def __str__(self):
        return self.df

    def can_date(self):
        if self.df['Date']:
            print('Can turn into a Date Frame')


class DateStructureFrame(DataStructureFrame):
    def __init__(self, data, description, date_range):
        super().__init__(data, description)
        self.date_range = date_range

    def to_datetime(self):
        self.df['Date'] = pd.to_datetime(self.df.Date)

    def sort(self):
        self.df = self.df.sort_values(by='Date')

    def reindex(self):
        self.df.index = self.df['Date']
        self.df = self.df.iloc[::-1]
        self.df = self.df.drop(['Date'], axis=1)


class UrlGroup:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description
        self.length = None
        self.base_url = Url(self.name)
        self.url_list = []

    def __repr__(self):
        return 'UrlGroup(%r)' % self.name

    def __str__(self):
        return '%s' % self.url_list

    def set_base(self):
        self.base_url = Url(self.name)  # after initialisation

    def gen_num_list(self, lim):
        for x in range(0, lim, 1):
            url = Url(str(self.base_url) + str(x))
            url.pieces = self.base_url.pieces
            url.set_num(str(x))
            self.url_list.append(url)


class Url:
    def __init__(self, name=None):
        self.name = name
        self.structure = None
        self.pieces = None
        self.url = None
        self._name = None

    def __repr__(self):
        return 'Url(%r)' % self.name

    def __str__(self):
        return '%s' % self.name

    def set_structure(self, structure):
        if type(structure) == str:
            self.structure = [item for item in structure.split(" + ")]

    def set_pieces(self, **kwargs):
        assert set(self.structure) == set(kwargs.keys()), 'Pieces and Structure not consistent'
        self.pieces = kwargs
        Url.set_url(self)

    def set_url(self):
        if self.pieces is not None:
            self.url = ''.join(self.pieces.values())
        else:
            print('User has not inputted pieces of url')

    def is_enumerable(self):
        if 'NUM' in self.pieces:
            print('Object is enumerable')
        else:
            print('Objects is not enumerable')

    def set_num(self, num):
        self.pieces['NUM'] = num
        Url.set_url(self)

    @property
    def name(self):
        return self._name

    @property
    def structure_elements(self):
        return ', '.join(self.structure.split(" + "))

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Url names are strings, label for convenience')
        self._name = value


class Searcher:
    def __init__(self, url):
        self.url = url


def generate_urls(pages, topic):
    return ['https://www.thestar.com.my/search/?q=' + topic +
            '&qsort=newest&qrec=10&qstockcode=&pgno=' + str(num) for num in range(1, pages, 1)]


def pull_search(url, info):
    if info == 'dates':
        return [item.text for item
                in BeautifulSoup(requests.get(url).text, 'html.parser').find_all('span', class_='date')]
    elif info == 'summaries':
        return [item.text for item
                in BeautifulSoup(requests.get(url).text, 'html.parser').find_all('p')]
    elif info == 'intro':
        return [item.p.text for item
                in BeautifulSoup(requests.get(url).text, 'html.parser').find_all('div', class_='row list-listing')]
    else:
        print('No specified data type')


def get_data(pages, topic, info):
    urls = generate_urls(pages, topic)
    return [item for sublist in ThreadPool(pages).starmap(pull_search, zip(urls, repeat(info))) for item in sublist]


def pull_dates(raw_dates):
    y = ([(item.split(' '))[0] + ' ' + (item.split(' '))[1] + ' '
          + (item.split(' '))[2] for item in raw_dates])
    return [[p, y.count(p)] for p in set(y)]


def pull_places(raw_locations):
    y = ([(item.split(': '))[0] for item in raw_locations])
    return [[p, y.count(p)] for p in set(y)]


def clean_locations(location_list):
    cleaned_list = []
    for item in location_list:
        if len(item[0].split(' ')) < 3:
            cleaned_list.append(item)
    return cleaned_list


def date_frame(pages, topic, info):
    df = pd.DataFrame(pull_dates(get_data(pages, topic, info)), columns=['Date', topic])
    df['Date'] = pd.to_datetime(df.Date)
    df = df.sort_values(by='Date')
    df.index = df['Date']
    df = df.iloc[::-1]
    return df.drop(['Date'], axis=1)


def parsed_date_frame(pages, topic, info):
    df = date_frame(pages, topic, info);
    return [item.strftime("%d/%m") for item in df['Date']], list(df['Count'])


def location_comparison(pages, topic_1, topic_2):
    df1 = pd.DataFrame(clean_locations(pull_places(get_data(pages, topic_1, 'intro'))),
                       columns=['Location', topic_1])
    df1.index = df1['Location']
    df1 = df1.drop('Location', axis=1)
    df2 = pd.DataFrame(clean_locations(pull_places(get_data(pages, topic_2, 'intro'))),
                       columns=['Location', topic_2])
    df2.index = df2['Location']
    df2 = df2.drop('Location', axis=1)
    return df1.merge(df2, left_index=True, right_index=True, how='inner')