"""
第二题： roman name： 第一步写一个helper，看LC 13，将roman转化成数字。第二步就是处理string，array中保存的是"first roman"的形式，
我的做法是先遍历一遍array，将里面string split以后提取出first name, last roman，然后把数字加进去，将array的元素替换成“first number
roman”的形式，然后sort；最后再把中间的number去掉好了。注意number变成了string，所以6要变成06。

"""

def romanToInt(s: str) -> int:
    d = {"I": 1,
         "V": 5,
         "X": 10,
         "L": 50,
         "C": 100,
         "D": 500,
         "M": 1000}

    result = 0
    skip = False

    for i in range(len(s) - 1):

        if skip:
            skip = False
            continue

        if d[s[i]] >= d[s[i + 1]]:
            result += d[s[i]]
        else:
            skip = True
            result += d[s[i + 1]] - d[s[i]]
        print(i, result)

    if not skip:
        result += d[s[-1]]

    return result

