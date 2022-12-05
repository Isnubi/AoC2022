data,boxes,boxes2,result1,result2=open('input').read().split('\n\n'),[[] for i in range(9)],[[] for j in range(9)],[],[]
for string in data[0].split('\n'):
    for i, char in enumerate(string):
        if 65 <= ord(char) <= 90:index=i//4;boxes[index].insert(0,char),boxes2[index].insert(0,char)
for move in data[1][:-1].split('\n'):
    temp = move.replace('move ', '').replace(' from ', ',').replace(' to ', ',')
    nums1,nums2 = list(map(int, temp.split(','))),list(map(int, temp.split(',')))
    indexfrom1,indexfrom2 = nums1[1] - 1,nums2[1] - 1
    indexto1,indexto2 = nums1[2] - 1,nums2[2] - 1
    for i in range(nums1[0]):box = boxes[indexfrom1].pop();boxes[indexto1].append(box)
    stack = boxes2[indexfrom2][-nums2[0]:]
    boxes2[indexfrom2] = boxes2[indexfrom2][:-nums2[0]]
    boxes2[indexto2].extend(stack)
for string in boxes:result1.append(string[-1])
for string in boxes2:result2.append(string[-1])
print(f"Part one: {''.join(result1)}\nPart two: {''.join(result2)}")