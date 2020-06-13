import re
fh = open('Jo_bhi_naam_hai_bc.txt')
lst = list()
sum = 0
for line in fh:
    line = line.rstrip()
    num = re.findall('[0-9]+',line)
    if len(num) == 0:
        continue
    else:
        for i in num:
            sum = sum + int(i)
print(sum)
