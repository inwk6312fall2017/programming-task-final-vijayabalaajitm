from collections import Counter

def find_words(file1):
    file1 = Counter(file1)

    with open('file1', 'r') as handle:
        for word in handle:
            letters = Counter(word.strip())

            if file1 >= letters:
                yield word

longest_word = max(find_words('qugteroda'), key=len)


def find_words2(file2):
   file2 = Counter(file2)

    with open('file2', 'r') as handle:
        for word in handle:
            letters = Counter(word.strip())

            if file2 >= letters:
                yield word

longest_word = max(find_words('qugteroda'), key=len)


def find_words3(file3):
    file3 = Counter(book3)

    with open('file3', 'r') as handle:
        for word in handle:
            letters = Counter(word.strip())

            if file3 >= letters:
                yield word

longest_word = max(find_words('qugteroda'), key=len)

find_words(book1.txt)
find_words2(book2.txt)
find_words3(book3.txt)
