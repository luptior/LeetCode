"""


Input is a string of characters that represents a text message. You need to segment this message into chunks of messages
each of length 160 characters and add suffix "(1/5)" (representing pagination) at the end of each segmented message
(Length of "(1/5)" is included in 160 length limit).

Input: "njdksjfn jdfnds kjfdklsjf jsdofjsd f jdslkjfgdslkngdslkjg fljksdjflsfdsjfdslkfjdslkfmdsklmfgn ljsdglkdsfg d \
lkjgdslkgjdsljgdslkjgdsfjngds lkjsdlkgjdsgkldsjgsdlkg lkjdslkgjdslkgjdslgmnds glkjgdslkjgdslkjfgodsjfds g,mdsgkjdsngdl\
sknfgldsjfglkdsjfglkdsjglkdsjglkdsgjdsklgjdslk lkgjdslkgfjdslkgjdslkgjdsljfgdslkgjmdslkg kljghjdslkjgdslkjfg"

Output: ['njdksjfn jdfnds kjfdklsjf jsdofjsd f jdslkjfgdslkngdslkjg fljksdjflsfdsjfdslkfjdslkfmdsklmfgn ljsdglkdsfg \
d lkjgdslkgjdsljgdslkjgdsfjngds (1/3)',
'lkjsdlkgjdsgkldsjgsdlkg lkjdslkgjdslkgjdslgmnds glkjgdslkjgdslkjfgodsjfds g,mdsgkjdsngdlsknfgldsjfglkdsjfglkdsjglkdsj\
glkdsgjdsklgjdslk (2/3)',
'lkgjdslkgfjdslkgjdslkgjdsljfgdslkgjmdslkg kljghjdslkjgdslkjfg(3/3)']

Bonus Points: Pass the large test cases of question 3 without using split() function.

看了半天没懂什么意思，有没有人解释一下或者发下solution，最好用python

"""

s = "njdksjfn jdfnds kjfdklsjf jsdofjsd f jdslkjfgdslkngdslkjg fljksdjflsfdsjfdslkfjdslkfmdsklmfgn ljsdglkdsfg d lkjgdslkgjdsljgdslkjgdsfjngds lkjsdlkgjdsgkldsjgsdlkg lkjdslkgjdslkgjdslgmnds glkjgdslkjgdslkjfgodsjfds g,mdsgkjdsngdlsknfgldsjfglkdsjfglkdsjglkdsjglkdsgjdsklgjdslk lkgjdslkgfjdslkgjdslkgjdsljfgdslkgjmdslkg kljghjdslkjgdslkjfg"


def split(s : str) -> [str]:
    chunks = len(s) // 155 +1
    result = []
    for i in range(chunks):
        result.append(s[i*155:(i+1)*155]+f"({i}/{chunks})")

    return result


print(split(s))