def remove_punctuation(s):
    res = ""
    for i in s:
        if i .isalnum() or i.isspace():
            res += i
    print(res)

remove_punctuation("Hello, world!")