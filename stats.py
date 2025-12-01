def get_num_words(str):
    return len((str.split()))

def get_dict(str):
    d = {}
    strlw = str.lower()
    splt = list(strlw)
    sorted_splt = sorted(splt)
    for s in sorted_splt:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    return d 

def sort_on(items):
    return items["num"]

def get_list_of_dicts(d):
    l = []
    for k, v in d.items():
        l.append({"name": k, "num": v})
    l.sort(reverse=True, key= sort_on)
    return l




