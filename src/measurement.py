def load_benchmark():
    try:
        with open('../data/Book1and2_pair.csv', 'r', encoding='cp1252') as f:
            benchmark = f.read().splitlines()
        if benchmark is None:
            print("no file.")
        return benchmark
    except Exception as e:
        print("Error occurred. Check if file exists", e)


def calc_measure(results):
    benchmark = load_benchmark()
    if len(results) == 0:
        print('Precision = 0, Recall = 0, Fmeasure = 0')
        return
    count = 0
    for pair in results:
        if pair in benchmark:
            count = count + 1
    if count == 0:
        print('Precision=0, Recall=0, Fmeasure=0')
        return

    precision = count / len(results)
    recall = count / len(benchmark)
    f_measure = 2 * precision * recall / (precision + recall)
    FN = len(benchmark) - count
    print(' TP:', count, '\n', 'FP:', len(results) - count, '\n',
          'FN:', FN)
    print("Precision =", precision, ", Recall =", recall, ", Fmeasure =", f_measure)
    return
