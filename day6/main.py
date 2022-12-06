for n in [4,14]:
    for i in range(n, len(list(open('input').read().strip()))):
        if len(list(open('input').read().strip())[i - n:i]) == len(set(list(open('input').read().strip())[i - n:i])): print(i);break