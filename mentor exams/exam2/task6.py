def count_substring(text, sub):
    count = x = 0
    while True:
        x = text.find(sub, x)
        if x == -1:
            break
        count += 1
        x += 1
    print(count)

count_substring("aaaa", "aa")
