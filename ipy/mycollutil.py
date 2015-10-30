def mergesorted(old, new, mergekey):
    newl = list(new)
    res = []
    n = 0
    l = mergekey(newl[0])
    r = mergekey(newl[-1])
    for d in old:
        mk = mergekey(d)
        if mk < l or mk > r:
            res.append(d)
        else:
            res.extend(newl)
    return res

def last_index(lst, pred):
    ix = len(lst) - 1
    while ix >= 0:
        if pred(lst[ix]):
            return ix
        ix -= 1
    return -1

def first_index(lst, pred):
    ix = 0
    while ix < len(lst):
        if pred(lst[ix]):
            return ix
        ix += 1
    return -1
