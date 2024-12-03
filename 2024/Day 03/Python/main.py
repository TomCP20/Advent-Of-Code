import re
input = "".join(open(0).read())

print(sum( int(a)*int(b) for (a, b) in re.findall(r"mul\((\d+),(\d+)\)", input)))

enabled = True
total = 0
for match in re.finditer(r"do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)", input):
    m = match.group(0)
    if (m == "do()"):
        enabled = True
    elif (m == "don't()"):
        enabled = False
    elif enabled:
        total += int(match.group(1))*int(match.group(2))
print(total)