text = """
Got this panda plush toy for my daughter's birthday, 
who loves it and takes it everywhere. It's soft and 
super cute, and its face has a friendly look. It's 
a bit small for what I paid though. I think there 
might be other options that are bigger for the 
same price. It arrived a day earlier than expected, 
so I got to play with it myself before I gave it 
to her.
"""


def wordcount(text):
    # Remove punctuation and convert to lowercase
    text = text.lower()
    words = text.split()
    cleaned_words = []

    # Remove punctuation from words
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalnum())
        if cleaned_word:
            cleaned_words.append(cleaned_word)

    # Count the occurrences of each word
    word_counts = {}
    for word in cleaned_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


result = wordcount(text)

print(result)