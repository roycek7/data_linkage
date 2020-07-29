import csv

from src.book import Book1, Book2, Book3

comma_required = 11


# csv loader of Book1
def csv_loader_book1():
    """
    Book1 (id, title, authors, pubyear, pubmonth, pubday, edition, publisher, isbn13, language, series, pages)
    """
    try:
        with open('../data/Book1.csv', 'r', encoding='latin') as f:
            lines_book1 = csv.reader(f, delimiter=',')

            if lines_book1  is None:
                print("no file.")
                return

            book1 = []
            for line in lines_book1:
                count_comma = line.count(',')
                if count_comma < comma_required:
                    for i in range(comma_required - count_comma):
                        line.append(',')
                book = Book1()
                book.set_id(line[0])
                book.set_title(line[1])
                book.set_authors(line[2])
                book.set_pubyear(line[3])
                book.set_pubmonth(line[4])
                book.set_pubday(line[5])
                book.set_edition(line[6])
                book.set_publisher(line[7])
                book.set_isbn13(line[8])
                book.set_language(line[9])
                book.set_series(line[10])
                book.set_pages(line[11])
                book1.append(book)
            f.close()
        return book1
    except Exception as e:
        print(f"Error occurred. Check if file exists: {e}")
        pass


# csv loader of Book2
def csv_loader_book2():
    """
    Book2 (id, book_title, authors, publication_year, publication_month, publication_day, edition, publisher_name,
    isbn13, language, series, pages)
    """
    try:
        with open('../data/Book2.csv', 'r', encoding='latin') as f:
            lines_book2 = csv.reader(f, delimiter=',')

            if lines_book2 is None:
                print("no file.")
                return

            book2 = []
            for line in lines_book2:
                count_comma = line.count(',')
                if count_comma < comma_required:
                    for i in range(comma_required - count_comma):
                        line.append(',')
                book = Book2()
                book.set_id(line[0])
                book.set_title(line[1])
                book.set_authors(line[2])
                book.set_pubyear(line[3])
                book.set_pubmonth(line[4])
                book.set_pubday(line[5])
                book.set_edition(line[6])
                book.set_publisher(line[7])
                book.set_isbn13(line[8])
                book.set_language(line[9])
                book.set_series(line[10])
                book.set_pages(line[11])
                book2.append(book)
            f.close()
        return book2
    except Exception as e:
        print(f"Error occurred. Check if file exists: {e}")
        pass


# csv loader of Book 3
def csv_loader():
    """
    Book3 (ID, Title, Author1, Author2, Author3, Publisher, ISBN13, Date, Pages, ProductDimensions, SalesRank,
    RatingsCount, RatingValue, PaperbackPrice, HardcoverPrice, EbookPrice, AudiobookPrice)
    """
    try:
        with open('../data/Book3.csv', 'r', encoding='cp1252') as f:
            lines = csv.reader(f, delimiter=',')
            if lines is None:
                print("no file.")
                return
            books = []

            for line in lines:
                count_comma = line.count(',')
                if count_comma < comma_required:
                    for i in range(comma_required - count_comma):
                        line.append(',')
                book = Book3()
                book.set_id(line[0])
                book.set_title(line[1])
                book.set_author1(line[2])
                book.set_author2(line[3])
                book.set_author3(line[4])
                book.set_publisher(line[5])
                book.set_isbn13(line[6])
                book.set_date(line[7])
                book.set_pages(line[8])
                book.set_productdimension(line[9])
                book.set_salesrank(line[10])
                book.set_ratingscount(line[11])
                book.set_ratingvalue(line[12])
                book.set_paperbackprice(line[13])
                book.set_hardcoverprice(line[14])
                book.set_ebookprice(line[15])
                book.set_audiobookprice(line[16])
                books.append(book)
            f.close()
        return books
    except Exception as e:
        print(e)
        print("Error occurred. Check if file exists.")
        pass
