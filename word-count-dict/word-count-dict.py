from collections import defaultdict

def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    pass

    countWord = defaultdict(int);
    for sentence in sentences:
        for word in sentence:
            countWord[word] += 1

    return countWord
    