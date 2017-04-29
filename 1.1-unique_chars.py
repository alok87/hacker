def unique_chars(r):
    found = {}
    for i in r:
        if i in found:
            return False
        found[i] = True
    return True


a = "Mynameisanthonygonjavis"
b = 'abcdefghijkl'
for r in [a, b]:
    print("r has unique chars = %s" % unique_chars(r))
