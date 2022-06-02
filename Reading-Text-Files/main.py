# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    f = open(filename)
    contents = f.read()

    print(contents)
    return(contents)
    f.close()


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    list_of_words = text.split(" ")

    counts = dict()

    for word in list_of_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
    # return {"as": 10, "would": 20}


count_words()
