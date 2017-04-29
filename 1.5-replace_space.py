def replace_space(s):
    j = 0
    for i in s:
        if i == " ":
            s = s[:j] + "%20" + s[j+1:]
        j += 1
    return s

testcases = ['ssssss  sssssss  ss  ss', '', ' ', ' s']
for t in testcases:
    print("s=%s, result=%s", (t, replace_space(t)))
