input = "hello, world!"

source = ['i','e','o','l','h']

words = input.split(" ")

count = 0

for word in words:
    if sum([ 0 if x in source or not x.isalpha() else 1 for x in word]) == 0:
        count += 1


print(count)