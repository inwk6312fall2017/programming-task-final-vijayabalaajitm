from collections import Counter

def find_words(file1):
    file1 = Counter(file1)

    with open('file1', 'r') as handle:
        for word in handle:
            letters = Counter(word.strip())

            if file1 >= letters:
                yield word

longest_word = max(find_words('qugteroda'), key=len)
