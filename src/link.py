import datetime

import src.measurement as measure
from src.book import Book1, Book2
from src.csv_loader import csv_loader_book1 as csv1
from src.csv_loader import csv_loader_book2 as csv2
from src.question_7_1 import calc_jaccard


# linking results, Jaccard coefficient with 3-gram tokenization as the similarity measure
# performing comparison only on the “book title” field.
def nested_loop_by_title_jaccard():
    threshold = 0.75
    q = 3

    book_1_title = csv1()
    book_2_title = csv2()
    results = []
    book_title_1 = Book1()
    book_title_2 = Book2()
    id_1 = 0
    id_2 = 0
    title_1 = None
    title_2 = None
    start_time = datetime.datetime.now()
    for i in range(0, len(book_1_title)):
        book_title_1 = book_1_title[i]
        id_1 = book_title_1.get_id()
        title_1 = book_title_1.get_title()
        for j in range(0, len(book_2_title)):
            book_title_2 = book_2_title[j]
            id_2 = book_title_2.get_id()
            title_2 = book_title_2.get_title()

            sim = calc_jaccard(title_1, title_2, q)
            # Book pairs whose similarity is higher than 0.75 are regarded as matched pairs
            if sim > threshold:
                results.append(str(id_1) + ',' + str(id_2))

    endtime = datetime.datetime.now()
    time = endtime - start_time

    print("Total Time: ", round(time.total_seconds() * 1000, 3), 'milliseconds')

    # Comparing output with the gold-standard dataset
    measure.load_benchmark()
    measure.calc_measure(results)


nested_loop_by_title_jaccard()

"""
Total Time:  138984.807 milliseconds
TP: 210 
FP: 912 
FN: 22
Precision = 0.18716577540106952 , Recall = 0.9051724137931034 , Fmeasure = 0.310192023633678
"""