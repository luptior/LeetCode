"""
https://www.1point3acres.com/bbs/thread-670003-1-1.html
"""

initial = list("00000")
target = list("01011")

flips = 0
status = '0'
for c in target:
    if c != status:
        flips += 1
        status = '0' if status == '1' else '1'
print(flips)
