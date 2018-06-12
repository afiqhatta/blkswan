import pandas as pd


class Frame:
    def __init__(self):
        self.df = pd.DataFrame()

    def write_cols(self, cols):
        self.df = pd.DataFrame(columns=cols)


class DateFrame(Frame):
    def __init__(self, column_list, csv_file=None):
        """
        Initialise the DataFrame with the columns that match the csv file
        :param column_list: a list of columns
        """
        super().__init__()
        self.df = pd.read_csv(csv_file)
        self.df.columns = column_list
        self.name = csv_file

    def read(self, csv_name):
        self.df = pd.read_csv(csv_name)

    def parse_cols(self, column_list):
        self.df.columns = column_list

    def splice_column(self, n):
        """
        Formatting function for THE STAR newspaper only
        This chooses the first n values of row entries of a specific column
        :return: A new data frame with parsed dates we can play with.
        """
        dates = self.df[self.df.columns[0]]
        parsed_dates = []
        for i in dates:
            parsed_dates.append(' '.join(i.split()[0:n]))
        self.df[self.df.columns[0]] = parsed_dates

    def to_dates(self):
        self.df = pd.to_datetime(self.df.Date)

    def sort(self):
        self.df = self.df.sort(by='Date')

    def reindex(self):
        self.df.index = self.df['Date']

    def reverse(self):
        self.df = self.df.iloc[::-1]

    def drop_date_index(self):
        self.df = self.df.drop(['Date'], axis=1)

    def save_csv(self):
        self.df.to_csv(str(self.name))

# ringgit = DateFrame('output187.csv', ['Date', 'Head', 'Text'])
# ringgit.splice_column(3)
# ringgit.save_csv()
# print(ringgit.df)



