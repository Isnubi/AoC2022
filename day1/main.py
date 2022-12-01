def get_sum_list(lines):
    sum_list = []
    current_sum = 0
    for line in lines:
        if line.rstrip() == '':
            sum_list.append(current_sum)
            current_sum = 0
            continue
        current_sum += int(line.rstrip())
    return sorted(sum_list, reverse=True)

with open('input') as f:
    lines = f.readlines()
print("Part one: ", get_sum_list(lines)[0])
print("Part two: ", get_sum_list(lines)[0] + get_sum_list(lines)[1] + get_sum_list(lines)[2])