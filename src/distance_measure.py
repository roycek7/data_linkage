from functools import lru_cache


@lru_cache(maxsize=None)
def calc_jaccard(str1, str2, q):
    str1_tokens = tokenize(str1, q)
    str2_tokens = tokenize(str2, q)
    total_tokens = str1_tokens + str2_tokens
    total_tokens = list(set(total_tokens))
    return (len(str1_tokens) + len(str2_tokens) - len(total_tokens)) / len(total_tokens)


@lru_cache(maxsize=None)
def tokenize(string, q):
    if q != 0:
        if len(string) < q:
            str_tokens = [string]
        else:
            str_tokens = [string[i:i + q] for i in range(0, len(string) - q + 1, 1)]
        return list(set(str_tokens))
    else:
        str_tokens = string.split(" ")
        return list(set(str_tokens))


def calc_ed_sim(str1, str2):
    if str1 == str2:
        return 1
    ed = calc_ed(str1, str2)

    return 1 - (ed / max(len(str1), len(str2)))


@lru_cache(maxsize=None)
def calc_ed(str1, str2):
    ed = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if i is 0:
                ed[i][j] = j
            elif j is 0:
                ed[i][j] = i
            elif str1[i - 1] == str2[j - 1]:
                ed[i][j] = ed[i - 1][j - 1]
            else:
                ed[i][j] = min(
                    ed[i][j - 1] + 1,
                    ed[i - 1][j] + 1,
                    ed[i - 1][j - 1] + 1
                )

    return ed[len(str1)][len(str2)]


author1 = 'Richmond Shee, Kirtikumar Deshpande and K. Gopalakrishnan;'
author2 = 'K. Gopalakrishnan, Kirtikumar Deshpande, and Richmond Shee'
sim_jd = calc_jaccard(author1, author2, 3)
sim_ed = calc_ed_sim(author1, author2)

print(f'\t\nsimilarity \nJaccard Co-efficient: {sim_jd}\nEdit Distance: {sim_ed}'
      f'\ndissimilarity \nJaccard Distance: {1 - sim_jd}\nEdit Distance: {1 - sim_ed}')

"""
similarity 
Jaccard Co-efficient: 0.8
Edit Distance: 0.4137931034482759
dissimilarity 
Jaccard Distance: 0.19999999999999996
Edit Distance: 0.5862068965517241
"""
