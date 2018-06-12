import spacy
import pandas as pd
import matplotlib.pyplot as plt

nlp = spacy.load('en')
file = pd.read_csv('test_input.csv')


class Document:
    def __init__(self, text):
        self.text = text
        self.entities = []
        self.doc = nlp(text)

    def print_entities(self):
        for ent in self.doc.ents:
            print(ent.text)

    def get_entities(self):
        for ent in self.doc.ents:
            self.entities.append(ent)


class Frame:
    def __init__(self, df):
        self.df = df

    def get_entities(self, column):
        """
        Extracts a list of entities from the news articles
        :param column:
        :return:
        """
        temp_series = pd.Series(self.df[column])
        entities = []
        for text in temp_series:
            doc = nlp(text)
            local_entities = []
            for ent in doc.ents:
                local_entities.append(ent.text)
            entities.append(local_entities)
        self.df['Entities'] = entities

    def clean(self):
        self.df.index = self.df.Date

    def remove_junk_cols(self, index):
        """
        Remove some useless columns for whatever reason
        :param index: columns you wish to extract
        :return:
        """
        self.df = self.df.iloc[:, index:]

    def to_dates(self):
        """
        Re-parse dates to datetime format
        :return: The new loaded data frame
        """
        self.df.Date = pd.to_datetime(self.df.Date)

    def sort(self):
        """
        Sort the dates into the order you want them
        :return: the new data frame
        """
        self.df = self.df.sort(by='Date')

    def reindex(self):
        self.df.index = self.df['Date']

    def reverse(self):
        """
        Reverse the date order
        :return:
        """
        self.df = self.df.iloc[::-1]

    def drop_date_index(self):
        self.df = self.df.drop(['Date'], axis=1)

    def save_csv(self):
        self.df.to_csv(str(self.name))

    def quick_clean(self):
        """
        Shortcut to quickly trim the fat of data frames
        :return:
        """
        self.to_dates()
        self.reindex()
        self.clean()
        self.remove_junk_cols(2)

    def count(self):
        """
        Group entries in the dataframe by day and aggregate
        :return:
        """
        return self.df.groupby(self.df.index.date).count()

    def filter(self):
        """
        Filtering function here
        :return:
        """
        pass


x = Frame(file)
x.quick_clean()
y = x.count()


