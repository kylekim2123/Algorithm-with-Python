# 1302. 베스트 셀러 (실버4)

books = {}
for _ in range(int(input())):
    book = input()
    books[book] = books.get(book, 0) + 1

max_selling = max(books.values())
print(sorted([book for book in books if books[book] == max_selling])[0])

# from collections import Counter
#
# books = Counter([input() for _ in range(int(input()))])
# max_selling = max(books.values())
# print(sorted([book for book in books if books[book] == max_selling])[0])
