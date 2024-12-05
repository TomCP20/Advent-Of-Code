import re

input = open(0).read()
row = len(input.splitlines()[0]) + 6
padded_input = "".join("..." + line + "..." for line in input.splitlines())

count1 = 0
for o in map(str, [0, row, row-1, row-2]):
    pattern1 = r"(?=(X.{" + o + r"}M.{" + o + r"}A.{" + o + r"}S|S.{" + o + r"}A.{" + o + r"}M.{" + o + r"}X))"
    count1 += len(re.findall(pattern1, padded_input))
print(count1)

count2 = 0
n = str(row-2)
for perm in ["MMSS", "MSMS", "SMSM", "SSMM"]:
    pattern2 = r"(?=(" + perm[0] + r"." + perm[1] + r".{" + n + r"}A.{" + n + r"}" + perm[2] + r"." + perm[3] + r"))"
    count2 += len(re.findall(pattern2, padded_input))
print(count2)