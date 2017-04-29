def remove_duplicate(s):
    new_s = ""
    for i in s:
        if i not in new_s:
            new_s += i
    return new_s

testcases = ['abc def ghi abc',
             'aaaabbbbcccc   dddeeccceeeffgg',
             'aaaabbbbccccddeeccceeeffgg',
             '123451234554312109189193028153767890',
             '',
             'aaaaaaaa',
             'aabbaaa']

for t in testcases:
    print("Input %s, Output %s" % (t, remove_duplicate(t)))

