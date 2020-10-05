from collections import Counter

word = "abaasass"

k = 3

check = lambda x: True if len(Counter(x)) == 1 else False

while True:

    i = 0

    while i+k <= len(word) and not check(word[i:i+k]) :
        # print(i, i+k, word[i:i+k])
        i += 1
        continue

    if i + k <= len(word):
        word = word[:i] + word[i+k:]
        continue
    else:
        break

print(word)



