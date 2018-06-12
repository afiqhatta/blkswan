HOME_PAGES = {
    'THE_STAR': 'https://www.thestar.com.my/',
    'THE_SUN': 'http://www.thesundaily.my/',
    'THE_NST': 'https://www.nst.com.my/',
    'THE EDGE': 'http://www.theedgemarkets.com/',
    'M_KINI': 'https://www.malaysiakini.com/',
    'MALAY_MAIL': 'https://www.malaymail.com/'
}

HOME_TAGS = {
    'THE_STAR': {
        'main_headline': {'span': '', 'class': ''},
        'sub_headlines': {'span': '', 'class': ''}
    },
    'THE_SUN': {},
    'THE_NST': {},
    'THE EDGE': {},
    'M_KINI': {},
    'MALAY_MAIL': {}
}

SEARCH_URLS = {
    'THE_STAR': ['https://www.thestar.com.my/search/?q=',
                 'topic',
                 '&qsort=newest&qrec=10&qstockcode=&pgno=',
                 'page'],
    'THE_SUN': ['http://www.thesundaily.my/search/content/',
                'topic',
                '?page=',
                'page'],
    'THE_NST': ['https://www.nst.com.my/search?s=',
                'topic',
                '&page=',
                'page'],
    'THE EDGE': ['https://www.theedgemarkets.com/search-results?keywords=',
                 'topic'],
    'M_KINI': 'https://www.malaysiakini.com/',
    'MALAY_MAIL': 'https://www.malaymail.com/'
}

ELEMENTS = {
    'THE_STAR': {
        'body': {'span': 'div', 'class': 'story'},  # body of news in a news page
        'urls': {'span': 'h2', 'class': 'f18'},  # urls in search pages, write general structures
        'summary': {'span': 'div', 'class': 'row list-listing'}

    },
    'THE_SUN': {
        'body': {'span': '', 'urls': ''},
        'urls': {'span': '', 'urls': ''},
        'summary': {'span': 'div', 'class': 'row list-listing'},
    },
    'THE_NST': {
            'body': {'span': '', 'urls': ''},
            'urls': {'span': '', 'urls': ''},
            'summary': {'span': 'div', 'class': 'row list-listing'},
        },

}
