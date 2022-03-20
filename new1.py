def count_vowel(s):

        num_vowel =0
        for char in s:
            if char in 'AEIOUaeeiou':
                num_vowel+1
                
        return num_vowel

