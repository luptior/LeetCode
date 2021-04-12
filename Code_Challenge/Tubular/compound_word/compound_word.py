import sys

# read in stdin data
data = sys.stdin.readlines()

# preprocess by strip()
data = [datum.strip() for datum in data]

for line in data:
    print(line)