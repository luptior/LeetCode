from sys import argv
import re

def reformat(name: str) -> str:
    return '_'.join(re.split('[: ]', name))

if __name__ == '__main__':
    print(reformat(argv[1]))