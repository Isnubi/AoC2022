ord_list1,ord_list2,lines = [], [], open('input').readlines()
for line in lines:
    for char in line[0:len(line)//2]:
        if char in line[len(line)//2:]:
            if 97 <= ord(char) <= 122: ord_list1.append(ord(char) - 96);break
            elif 65 <= ord(char) <= 90: ord_list1.append(ord(char) - 38);break
for i in range(0, len(lines), 3):
    for char in lines[i]:
        if char in lines[i+1] and char in lines[i+2]:
            if 97 <= ord(char) <= 122: ord_list2.append(ord(char) - 96);break
            elif 65 <= ord(char) <= 90: ord_list2.append(ord(char) - 38);break
print(f"Part one: {sum(ord_list1)}\nPart two: {sum(ord_list2)}")