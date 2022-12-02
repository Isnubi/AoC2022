score1, score2, lines = 0, 0, open('input').readlines()
for line in lines:
    if line.rstrip().split(' ')[0] == 'A' and line.rstrip().split(' ')[1] == 'X':score1+=4;score2+=3
    elif line.rstrip().split(' ')[0] == 'A' and line.rstrip().split(' ')[1] == 'Y':score1+=8;score2+=4
    elif line.rstrip().split(' ')[0] == 'A' and line.rstrip().split(' ')[1] == 'Z':score1+=3;score2+=8
    elif line.rstrip().split(' ')[0] == 'B' and line.rstrip().split(' ')[1] == 'X':score1+=1;score2+=1
    elif line.rstrip().split(' ')[0] == 'B' and line.rstrip().split(' ')[1] == 'Y':score1+=5;score2+=5
    elif line.rstrip().split(' ')[0] == 'B' and line.rstrip().split(' ')[1] == 'Z':score1+=9;score2+=9
    elif line.rstrip().split(' ')[0] == 'C' and line.rstrip().split(' ')[1] == 'X':score1+=7;score2+=2
    elif line.rstrip().split(' ')[0] == 'C' and line.rstrip().split(' ')[1] == 'Y':score1+=2;score2+=6
    elif line.rstrip().split(' ')[0] == 'C' and line.rstrip().split(' ')[1] == 'Z':score1+=6;score2+=7
print(f"Part one: {score1} points\nPart two: {score2} points")