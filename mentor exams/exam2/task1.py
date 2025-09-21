def sort_by_frequency(lst):
    srit = sorted(lst, key=lambda x: (-lst.count(x), x))
    print(srit)


sort_by_frequency([4,4,1,2,2,3,3,3])