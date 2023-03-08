'''
Activity 1:
Spilt the sentence below into a list/array called sentence_words

Hello World morality is the futility of humanitys existence.
'''
sentence_words = ("Hello World morality is the futility of humanitys existence.".split(" "))
print(sentence_words)
'''
Activity 2:
Get me the length of the sentence_words
'''
print(len(sentence_words))
'''
Activity 3:
Print all the words of the sentence_words individually
'''
for i in range(len(sentence_words)):
    print(sentence_words[i])
'''
Activity 4:
Make all the individual sentence_words back into their original sentence
'''