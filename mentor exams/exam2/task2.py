def decode_rle(s):
    res = ""
    i = 0
    while i < len(s):
        gb = s[i]
        i += 1
        num = ""
        while i < len(s) and s[i].isdigit():
            num +=s[i]
            i +=1
        res += gb * int(num) if num else gb
    print(res)


decode_rle("a3b2c1g7")
