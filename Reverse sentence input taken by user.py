def rev_sentence(sentence):
    # first split string in two words
    words = sentence.split(' ')
    # reverse split string list
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence

if __name__ == "__main__":
    a = input("Enter a string: \n")
    print(rev_sentence(a))