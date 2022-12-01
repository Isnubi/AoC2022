def part1():
    with open("input") as f:
        lines = f.readlines()

    old_sum = 0
    sum = 0
    for line in lines:
        if line.rstrip() == '':
            if sum > old_sum:
                old_sum = sum
            sum = 0
            continue
        sum += int(line.rstrip())

    print(old_sum)


def part2():
    with open("input") as f:
        lines = f.readlines()

    old_sum = []
    sum = 0
    for line in lines:
        if line.rstrip() == '':
            old_sum.append(sum)
            sum = 0
            continue
        sum += int(line.rstrip())

    old_sum.sort(reverse=True)
    most = 0
    for i in range(3):
        most += old_sum[i]
    print(most)


#part1()
part2()