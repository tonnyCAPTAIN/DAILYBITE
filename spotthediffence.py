#!/usr/bin/python3

def spotdiff():
    d = ""
    t = "foobar"
    s = "barfoozxt"
    if len(s) > len(t):
        for i in s: 
            if i not in t:
                d += i
        return d
    else:
        for i in t:
            if i not in s:
                d += i
        return d
print(spotdiff)
