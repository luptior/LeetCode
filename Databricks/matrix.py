"""
1. 给一个int[], 让你return一个boolean array 来indicate是否满足以下一个条件：
a[i]*a[i]+a[i+1]*a[i+1]=a[i+2]*a[i+2]
a[i+1]*a[i+1]+a[i+2]*a[i+2]=a[i]*a[i]
a[i]*a[i]+a[i+2]*a[i+2]=a[i+1]*a[i+1]

"""

"""
2. 给一个int[][] matrix，高度一定是3，长度不一定。再给一个sliding window，3x3的。问你用这个window slide over matrix，有几个window里面9个数是123456789不多也不少
return的应该是一个boolean array，来表示是否这个window里面刚好9个数
boolean array的长度应该是matrix的宽-2
"""

"""
4, 给两个int array a[] b[], 和两个数upper和lower，问你有几个i和j的组合such that lower<=a[i]*a[i]+b[j]*b[j]<=upper
这道题有time limit，不能brute force做
"""