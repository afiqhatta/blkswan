import pandas as pd


class Frame:
    def __init__(self):
        self.df = pd.DataFrame()

    def write_cols(self, cols):
        self.df = pd.DataFrame(columns=cols)


class DateFrame(Frame):
    def __init__(self):
        super().__init__()

    def to_dates(self):
        self.df = pd.to_datetime(self.df.Date)

    def sort(self):
        self.df = self.df.sort(by='Date')

    def reindex(self):
        self.df.index = df['Date']

    def reverse(self):
        self.df = self.df.iloc[::-1]

    def drop_date_index(self):
        self.df = self.df.drop(['Date'], axis=1)