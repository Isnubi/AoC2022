sum_list, current_sum, lines = [], 0, open('input').readlines()
[exec("sum_list.append(current_sum)\ncurrent_sum = 0") if line.rstrip() == '' else exec("current_sum += int(line.rstrip())") for line in lines]
print(f"Part one: {sorted(sum_list)[-1]}\nPart two: {sum(sorted(sum_list, reverse=True)[:3])}")