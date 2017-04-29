def remove_duplicate(s):
    i = 0
    for c in s:
        j = i + 1
        while j < len(s):
            if s[j] == s[i]:
                s = s[:j] + s[j+1:]
                j = j - 1
            j += 1
        i += 1
    return s

testcases = ['abc def ghi abc',
             'aaaabbbbcccc   dddeeccceeeffgg',
             'aaaabbbbccccddeeccceeeffgg',
             '123451234554312109189193028153767890',
             '',
             'aaaaaaaa',
             'aabbaaa']

for t in testcases:
    print("Input %s, Output %s" % (t, remove_duplicate(t)))

