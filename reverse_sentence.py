def reverse_sentence(sentence):
    tokenized = sentence.split(' ')
    tokenized.reverse()
    thing = " ".join(tokenized)
    return thing
print reverse_sentence("blah happy things")
