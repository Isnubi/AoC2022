sum_list, current_sum, lines = [], 0, open('input').readlines()
for line in lines:
    if line.rstrip() == '':
        sum_list.append(current_sum)
        current_sum = 0
    else: current_sum += int(line.rstrip())
print(f"Part one: {sorted(sum_list)[-1]}\nPart two: {sum(sorted(sum_list, reverse=True)[:3])}")