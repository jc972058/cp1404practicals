"""
Word Occurrences
Estimate : 30 min
Actual : 25 min
"""
text = str(input("Text: "))
text = text.split()
WORDS_TO_COUNT = {}
for word in text:
    WORDS_TO_COUNT[word] = WORDS_TO_COUNT.get(word, 0) + 1
WORDS_TO_COUNT = sorted(WORDS_TO_COUNT.items())
width = max(len(key) for key, count in WORDS_TO_COUNT)
for word, count in WORDS_TO_COUNT:
    print(f"{word:{width}} : {count}")
