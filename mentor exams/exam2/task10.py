def longest_consecutive_char(s):

    if not s:
        return 0

    maxl = 1
    currl = 1
    maxch = s[0]

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            currl +=1
            if currl > maxl:
                maxl = currl
                maxch = s[i]
        else:
            currl = 1
    print(maxl, maxch)

longest_consecutive_char("aaabbbaaac")

