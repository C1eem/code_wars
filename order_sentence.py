'''
Your task is to sort a given string.
Each word in the string will contain a single number.
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.

EXAMPLE:
    "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
    "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
    ""  -->  ""
'''

def order(sentence):
    if not sentence:
        return ""
    sentence = sentence.split()
    d = {}
    for word in sentence:
        for i in word:
            try:
                num = int(i)
                d[word] = num
                break
            except Exception:
                continue
    d = dict(sorted(d.items(), key=lambda item: item[1]))
    return " ".join(d.keys())


def main():
    print(order("is2 Thi1s T4est 3a"))
    print(order("4of Fo1r pe6ople g3ood th5e the2"))
    print(order(""))

if __name__ == "__main__":
    main()