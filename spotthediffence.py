#!/usr/bin/python3

def spotdiff():
    t = "foobar"
    s = "barfoot"
    if len(s) > len(t):
        for i in s: 
            if i not in t:
                return i
    else:
        for i in t:
            if i not in s:
                return i
