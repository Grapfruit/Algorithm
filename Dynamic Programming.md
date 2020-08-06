&copy; renyb

# Dynamic Programming（动态规划）

解决重复子问题

### 问题1：0/1背包问题

#### 题目

有N件物品和一个容量为V的背包。第i件物品的重量是w[i]，价值是v[i]。求解将哪些物品装入背包可使这些物品的重量总和不超过背包容量，且价值总和最大

```
N = 5
V = 10
w = [2, 2, 6, 5, 4]
v = [6, 3, 5, 4, 6]
```







### 问题2：斐波那契数列

#### 题目

求第n个斐波那契数



#### python

```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/31
# @Author  : renyb
# @File    : dp.py

import numpy as np


## 递归
def rec_opt(n):
    return 1 if n <= 2 else rec_opt(n-1) + rec_opt(n-2)

## 非递归
def dp_opt(n):
    if n <= 1:
        return 1
    else:
        opt = np.zeros(n, dtype=int)
        opt[0], opt[1] = 1, 1

        for i in range(2, n):
            opt[i] = opt[i-1] + opt[i-2]

        return opt[n-1]


if __name__ == "__main__":
    for i in range(1, 10):
        print('=====第%s个数=====' % (i))
        print('递归结果： %s' % (rec_opt(i)))
        print('非递归结果： %s' % (dp_opt(i)))
        print('')
```



### 问题3：求最大和

#### 题目

Array内，隔一个选一个，求最大和

```
arr = [1, 4, 6, 1, 9, 2, 2, 3]
```



#### python

```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/31
# @Author  : renyb
# @File    : dp.py

import numpy as np


## 递归
def rec_opt(arr, i):
    if i == 0:
        return arr[0]

    if i == 1:
        return max(arr[0], arr[1])
    
    if i > 1:
        A = rec_opt(arr, i-1)
        B = rec_opt(arr, i-2) + arr[i]
        return max(A, B)


## 非递归
def dp_opt(arr, i):
    if i == 0:
        return arr[0]

    if i == 1:
        return max(arr[0], arr[1])

    if i > 1:
        opt = np.zeros(i+1, dtype=int)
        opt[0] = arr[0]
        opt[1] = max(arr[0], arr[1])

        for n in range(2, i+1):
            A = opt[n-1]
            B = opt[n-2] + arr[n]
            opt[n] = max(A, B)
        return opt[i]


if __name__ == "__main__":
    arr = [1, 4, 6, 1, 9, 2, 2, 3]
    print(rec_opt(arr, 7))
    print(dp_opt(arr, 7))
```



### 问题4：是否可组成指定和

#### 题目

数组Array（全是正整数），是否可以组成指定和S

```
arr = [3, 34, 4, 12, 5, 2]
S = 9
```



#### python

```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/31
# @Author  : renyb
# @File    : dp.py

import numpy as np


## 递归
def rec_subset(arr, i, S):
    if S == 0:
        return True

    elif i == 0:
        return arr[0] == S

    # 剪枝
    elif arr[i] > S:
        return rec_subset(arr, i-1, S)
    
    else:
        A = rec_subset(arr, i-1, S-arr[i])
        B = rec_subset(arr, i-1, S)
        return A or B


# 非递归
## 动态规划表：构造一个len(arr)行，S+1列的二维数组
def dp_subset(arr, S):
    subset = np.zeros((len(arr), S + 1), dtype=bool)
    subset[:, 0] = True
    subset[0, :] = False
    subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for s in range(1, S + 1):

            # 剪枝
            if arr[i] > s:
                subset[i, s] = subset[i-1, s]
            
            else:
                A = subset[i-1, s-arr[i]]
                B = subset[i-1, s]
                subset[i, s] = A or B
    return subset[-1, -1]


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    print(dp_subset(arr, 9))
    print(dp_subset(arr, 10))
    print(dp_subset(arr, 11))
    print(dp_subset(arr, 12))
    print(dp_subset(arr, 13))
```

