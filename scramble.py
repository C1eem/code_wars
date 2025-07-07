'''

РЕШЕНО, НО НЕ ОПТИМИЗИРОВАНО

Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:
    - Only lower case letters will be used (a-z). No punctuation or digits will be included.
    - Performance needs to be considered.

EXAMPLES:
    scramble('rkqodlw', 'world') ==> True
    scramble('cedewaraaossoqqyt', 'codewars') ==> True
    scramble('katas', 'steak') ==> False
'''

def scramble(s1, s2):

    for i in s2:
        l = len(s1)
        s1 = s1.replace(i, "", 1)
        #print(s1)
        #print(s2)
        #print()
        if len(s1) == l:
            return False

    return True

def main():
    #print(scramble('rkqodlw', 'world'))
    #print(scramble('cedewaraaossoqqyt', 'codewars'))
    #print(scramble('katas', 'steak'))
    print(scramble("scriptjava", "javascript"))

if __name__ == "__main__":
    main()