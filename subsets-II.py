s = [1, 2, 2]


def substring(s, li=set(), output=[]):
    if len(s) == 0:
        temp = tuple(sorted(output))
        li.add(temp)
        return
    output1 = output
    output2 = output + [s[0]]
    substring(s[1:], li, output1)
    substring(s[1:], li, output2)
    return li


print(substring(s))
