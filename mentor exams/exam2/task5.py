def remove_consecutive_duplicates(s):
    x = ""
    for i in s:
        if i not in x:
            x += i
    print(x)




remove_consecutive_duplicates("aaabbcddd")
