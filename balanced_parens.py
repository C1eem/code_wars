'''

НЕ РЕШЕНО

Write a function which makes a list of strings representing
all of the ways you can balance n pairs of parentheses

EXAMPLES:
    balanced_parens(0) => [""]
    balanced_parens(1) => ["()"]
    balanced_parens(2) => ["()()","(())"]
    balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]

    !!!Решение с помощью рекурсии!!!
'''

# ИСПОЛЬЗУЙ РЕКУРСИЮ

def balanced_parens(n):
    l = []

    def rec(s, sym):
        s += sym
        if len(s) == n * 2:
            l.append(s)
        else:
            rec(s, '(')
            rec(s, ')')
    rec("", "(")
    answer = []
    for i in l:
        if i.count("(") == i.count(")"):
            answer.append(i)
    return answer

def main():
    print(balanced_parens(1))
    print(balanced_parens(2))
    print(balanced_parens(3))
    print(balanced_parens(4))

if __name__ == "__main__":
    main()