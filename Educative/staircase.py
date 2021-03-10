mem = {}

def jump(n, m):

  if n == 0: return 1
  elif n in mem: return mem[n]
  else:
    result = 0
    for i in range(1, m+1):
      result += staircase(n-i, m) if n >= i else 0

    mem[n] = result

    return result

def staircase(n, m):
  # Your code goes here

    return jump(n,m)


if __name__ == '__main__':
    print(staircase(4,2))