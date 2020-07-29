from src.csv_loader import csv_loader as csv
from src.book import Book3


# sampling the records whose id is the multiple of 100
def data_stat():
    book3 = csv()
    books = Book3()
    book3_id = []
    for i in range(0, len(book3), 100):
        books = book3[i]
        book_id = books.get_id()
        book3_id.append(book_id)
    return book3_id


# Among the samples found, number of fields containing NULL
def null_fields():
    book3 = csv()
    books = Book3()

    book3_values = []
    count = 0
    for i in range(0, len(book3), 100):
        books = book3[i]
        book3_values.append(books.get_id())
        book3_values.append(books.get_title())
        book3_values.append(books.get_author1())
        book3_values.append(books.get_author2())
        book3_values.append(books.get_author3())
        book3_values.append(books.get_publisher())
        book3_values.append(books.get_isbn13())
        book3_values.append(books.get_date())
        book3_values.append(books.get_pages())
        book3_values.append(books.get_productdimension())
        book3_values.append(books.get_salesrank())
        book3_values.append(books.get_ratingscount())
        book3_values.append(books.get_ratingvalue())
        book3_values.append(books.get_paperbackprice())
        book3_values.append(books.get_hardcoverprice())
        book3_values.append(books.get_ebookprice())
        book3_values.append(books.get_audiobookprice())
    count = len([_ for _ in book3_values if _ is ' '])

    return count


# Empo (error per million opportunities) according to the samples (only NULL value is considered)
def defects():
    defect_opportunities = 17
    units = len(data_stat())
    defect = null_fields()

    return (defect * 1000000) / (units * defect_opportunities)


print(f"Book IDs: {data_stat()}")
print(f"\nRecords Count: {len(data_stat())}\n")
print(f'\nNull Fields: {null_fields()}\n')
print(f'\nEmpo: {defects()}\n')

"""
Records Count: 38

Null Fields: 316

Empo: 489164.0866873065
"""