#! usr/bin/python3
strs = [""]
cmps = strs[0]

for i in range(len(cmps)):
    count = 0
    for s in strs:
        if i >= len(s) or s[i] != cmps[i]:
            break
        else:
            print('s[i]:', s[i])
            count += 1
    if count < len(strs):
        print(cmps[:i])
    if i == len(cmps)-1:
        print(cmps[:i+1])
