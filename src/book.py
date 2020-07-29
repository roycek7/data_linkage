class Book3:
    """
    Book3 (ID, Title, Author1, Author2, Author3, Publisher, ISBN13, Date, Pages, ProductDimensions, SalesRank,
    RatingsCount, RatingValue, PaperbackPrice, HardcoverPrice, EbookPrice, AudiobookPrice)
    """
    def __init__(self, id=None, title=None, author1=None, author2=None, author3=None, publisher=None, isbn13=None,
                 date=None, pages=None, productdimension=None, salesrank=None, ratingscount=None, ratingvalue=None,
                 paperbackprice=None, hardcoverprice=None, ebookprice=None, audiobookprice=None):
        self.id = id
        self.title = title
        self.author1 = author1
        self.author2 = author2
        self.author3 = author3
        self.publisher = publisher
        self.isbn13 = isbn13
        self.date = date
        self.pages = pages
        self.productdimension = productdimension
        self.salesrank = salesrank
        self.ratingscount = ratingscount
        self.ratingvalue = ratingvalue
        self.paperbackprice = paperbackprice
        self.hardcoverprice = hardcoverprice
        self.ebookprice = ebookprice
        self.audiobookprice = audiobookprice

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_author1(self):
        return self.__author1

    def get_author2(self):
        return self.__author2

    def get_author3(self):
        return self.__author3

    def get_publisher(self):
        return self.__publisher

    def get_isbn13(self):
        return self.__isbn13

    def get_date(self):
        return self.__date

    def get_pages(self):
        return self.__pages

    def get_productdimension(self):
        return self.__productdimension

    def get_salesrank(self):
        return self.__salesrank

    def get_ratingscount(self):
        return self.__ratingscount

    def get_ratingvalue(self):
        return self.__ratingvalue

    def get_paperbackprice(self):
        return self.__paperbackprice

    def get_hardcoverprice(self):
        return self.__hardcoverprice

    def get_ebookprice(self):
        return self.__ebookprice

    def get_audiobookprice(self):
        return self.__audiobookprice

    def set_id(self, value):
        self.__id = value

    def set_title(self, value):
        self.__title = value

    def set_author1(self, value):
        self.__author1 = value

    def set_author2(self, value):
        self.__author2 = value

    def set_author3(self, value):
        self.__author3 = value

    def set_publisher(self, value):
        self.__publisher = value

    def set_isbn13(self, value):
        self.__isbn13 = value

    def set_date(self, value):
        self.__date = value

    def set_pages(self, value):
        self.__pages = value

    def set_productdimension(self, value):
        self.__productdimension = value

    def set_salesrank(self, value):
        self.__salesrank = value

    def set_ratingscount(self, value):
        self.__ratingscount = value

    def set_ratingvalue(self, value):
        self.__ratingvalue = value

    def set_paperbackprice(self, value):
        self.__paperbackprice = value

    def set_hardcoverprice(self, value):
        self.__hardcoverprice = value

    def set_ebookprice(self, value):
        self.__ebookprice = value

    def set_audiobookprice(self, value):
        self.__audiobookprice = value


class Book1:
    """
    Book1 (id, title, authors, pubyear, pubmonth, pubday, edition, publisher, isbn13, language, series, pages)
    """
    def __init__(self, id=None, title=None, authors=None, pubyear=None, pubmonth=None,
                 pubday=None, edition=None, publisher=None, isbn13=None, language=None, series=None,
                 pages=None):
        self.id = id
        self.title = title
        self.authors = authors
        self.pubyear = pubyear
        self.pubmonth = pubmonth
        self.isbn13 = isbn13
        self.edition = edition
        self.publisher = publisher
        self.pubday = pubday
        self.language = language
        self.series = series
        self.pages = pages

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_authors(self):
        return self.__authors

    def get_publisher(self):
        return self.__publisher

    def get_isbn13(self):
        return self.__isbn13

    def get_pubyear(self):
        return self.__pubyear

    def get_pages(self):
        return self.__pages

    def get_pubmonth(self):
        return self.__pubmonth

    def get_edition(self):
        return self.__edition

    def get_pubday(self):
        return self.__pubday

    def get_language(self):
        return self.__language

    def get_series(self):
        return self.__series

    def set_id(self, value):
        self.__id = value

    def set_title(self, value):
        self.__title = value

    def set_authors(self, value):
        self.__authors = value

    def set_publisher(self, value):
        self.__publisher = value

    def set_isbn13(self, value):
        self.__isbn13 = value

    def set_pubyear(self, value):
        self.__pubyear = value

    def set_pages(self, value):
        self.__pages = value

    def set_pubmonth(self, value):
        self.__pubmonth = value

    def set_edition(self, value):
        self.__edition = value

    def set_pubday(self, value):
        self.__pubday = value

    def set_language(self, value):
        self.__language = value

    def set_series(self, value):
        self.__series = value


class Book2:
    """
    Book2 (id, book_title, authors, publication_year, publication_month, publication_day, edition, publisher_name,
    isbn13, language, series, pages)
    """
    def __init__(self, id=None, book_title=None, authors=None, publication_year=None, publication_month=None,
                 publication_day=None, edition=None, publisher_name=None, isbn13=None, language=None, series=None,
                 pages=None):
        self.id = id
        self.title = book_title
        self.authors = authors
        self.pubyear = publication_year
        self.pubmonth = publication_month
        self.isbn13 = isbn13
        self.edition = edition
        self.publisher = publication_day
        self.pubday = publisher_name
        self.language = language
        self.series = series
        self.pages = pages

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_authors(self):
        return self.__authors

    def get_publisher(self):
        return self.__publisher

    def get_isbn13(self):
        return self.__isbn13

    def get_pubyear(self):
        return self.__pubyear

    def get_pages(self):
        return self.__pages

    def get_pubmonth(self):
        return self.__pubmonth

    def get_edition(self):
        return self.__edition

    def get_pubday(self):
        return self.__pubday

    def get_language(self):
        return self.__language

    def get_series(self):
        return self.__series

    def set_id(self, value):
        self.__id = value

    def set_title(self, value):
        self.__title = value

    def set_authors(self, value):
        self.__authors = value

    def set_publisher(self, value):
        self.__publisher = value

    def set_isbn13(self, value):
        self.__isbn13 = value

    def set_pubyear(self, value):
        self.__pubyear = value

    def set_pages(self, value):
        self.__pages = value

    def set_pubmonth(self, value):
        self.__pubmonth = value

    def set_edition(self, value):
        self.__edition = value

    def set_pubday(self, value):
        self.__pubday = value

    def set_language(self, value):
        self.__language = value

    def set_series(self, value):
        self.__series = value