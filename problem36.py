#Problem 36: Write a program to find anagrams in a given list of words. 
#Two words are called anagrams if one word can be formed by rearranging letters of another.
# For example ‘eat’, ‘ate’ and ‘tea’ are anagrams.

def anagrams(word_list):
    anagrams = []
    d = []
    for i in range(len(word_list)):
        c = []
        for j in range(len(word_list)):
            if sorted(list(word_list[i])) == sorted(list(word_list[j])):
                c.append(word_list[j])
        d.append(c)
    for i in d:
        if i not in anagrams:
            anagrams.append(i)
    return anagrams

