def words(text):
    # takes in a series of string and return a dictionary of format {word: count}
    result = {}

    for word in text.split():
        try:
            result[int(word)] = result.get(word, 0) + 1
        except ValueError:
            result[word] = result.get(word, 0) + 1
    # print(result)
    return result

words('hello world')