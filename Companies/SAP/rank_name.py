from collections import Counter

input = [
    "kylan charles",
    "raymond strickland",
    "julissa shepard",
    "andrea meza",
    "destiny alvarado"
]

result = 0

ans = input[0]

for key in input:

    d = Counter(key)

    if " " in d:
        count = len(d)-1
    else:
        count = len(d)

    if result < count:
        ans = key
        result = count
    elif result > count:
        continue
    else:
        ans = sorted([ans, key])[0]

print(ans)


