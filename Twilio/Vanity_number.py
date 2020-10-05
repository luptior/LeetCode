"""
第一题python暴力解能直接过，我用sliding window看phone number chunk和code有没有match
https://www.1point3acres.com/bbs/thread-670298-1-1.html
"""

d = {2: "abc",
     3: "def",
     4: "ghi",
     5: "jkl",
     6: "mno",
     7: "pqrs",
     8: "tuv",
     9: "wxyz"}

d2 = {}

for k, v in d.items():
    for c in v.upper():
        d2[c] = str(k)

code = ["TWLO", "CODE", "HTCH"]
nums = ["+17474824380",
        "14157088956",
        "+919810155555",
        "+15109926333",
        "+1415123456"
        ]

def match(vanities:[str], numbers: [str]) -> [str]:
    result = []
    solutions = []
    l = []
    for x in vanities:
        if len(x) not in l:
            l.append(len(x))

        new_code = "".join([d2[c] for c in x])
        solutions.append(new_code)

    print(solutions)

    for num in numbers:
        for solution in solutions:
            if num.find(solution) > 0:
                print(num)

    return sorted(result)


print(match(code, nums))

