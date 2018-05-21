HOME_PAGES = {
    'THE_STAR': 'https://www.thestar.com.my/',
    'THE_SUN': 'http://www.thesundaily.my/',
    'THE_NST': 'https://www.nst.com.my/',
    'THE EDGE': 'http://www.theedgemarkets.com/',
    'M_KINI': 'https://www.malaysiakini.com/',
    'MALAY_MAIL': 'https://www.malaymail.com/'
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

TEXT_TAGS = {
    'THE_STAR': {
        'body': {'span': 'div', 'class': 'story'},
        'urls': {'span': 'h2', 'class': 'f18'}
    },
    'THE_SUN': {
        'body': {'span': '', 'urls': ''},
        'urls': {'span': '', 'urls': ''}
    }
}
