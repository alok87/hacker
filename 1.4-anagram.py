def is_anagram(a, b):
    if len(a) != len(b):
        return False
    for i in a:
        if i not in b:
            return False
    return True


testcases = [ ['alok', 'kola'], ['aaaaaa', 'bbbbbb'], ['', 'a'], ['', ''], ['a', 'a'], ['goli', 'logi'] ]
for t in testcases:
    print("%s is anagram of %s: %s" % (t[0], t[1], is_anagram(t[0], t[1])))
