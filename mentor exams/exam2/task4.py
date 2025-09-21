def dict_intersection(d1, d2):
    print({k: d1[k] + d2[k] for k in d1 if k in d2})

dict_intersection({"a":1,"b":2},{"b":3,"c":4})
