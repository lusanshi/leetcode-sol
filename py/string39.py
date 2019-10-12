#! usr/bin/python3

s = "1"
for k in range(1000):
    var = s[0]
    count = 1
    aswlist = []
    for i in s[1:]:
        if i != var:
            aswlist.append(str(count))
            aswlist.append(var)
            var = i
            count = 1
        else:
            count += 1
    aswlist.append(str(count))
    aswlist.append(var)
    s = ''.join(aswlist)
print(''.join(aswlist))
