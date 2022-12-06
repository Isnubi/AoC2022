for i in range(4, len(list(open('input').read().strip()))):
    if len(list(open('input').read().strip())[i - 4:i]) == len(set(list(open('input').read().strip())[i - 4:i])): print(i);break
for i in range(14, len(list(open('input').read().strip()))):
    if len(list(open('input').read().strip())[i - 14:i]) == len(set(list(open('input').read().strip())[i - 14:i])): print(i);break