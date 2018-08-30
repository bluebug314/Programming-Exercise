"""
PROGRAMMING EXERCISE, BASICS : Reversing Strings
Python 3.6
Author : Manuel Antony
"""

def rev_word(s):
    """ revere a single word"""
    s = list(s)
    l = len(s)
    last = l-1
    rs = s
    for i in range(int(l/2)):
        rs[last-i], rs[i] = s[i], s[last-i]
    return "".join(rs)

def rev_sentance(s):
    """ reverse a whole sentence"""
    r = []
    for w in s.split():
        r.insert(0, w)
    rs = ""
    for item in r:
        rs = f"{rs} {item}"
    return rs[1:]

def rev(s):
    if len(s.split()) > 1:
        s = rev_sentance(s)
    else:
        s = rev_word(s)
    print(s)

if __name__ == "__main__":
    rev ("reverseme")
    rev ("Im I reversed")