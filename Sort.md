&copy; renyb

# Sort

### 算法1：冒泡排序

#### 思想

> 1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
> 2. 对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
> 3. 针对所有的元素重复以上的步骤，除了最后一个。
> 4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
>
> 
>
> 参考资料：
>
> 吕新平、刘宏铭．二级公共基础知识实战训练教程：西安交通大学出版社，2006.02：30页



#### python

```
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/08/01
# @Author  : renyb
# @File    : sort.py


def bubble_sort(arr):

    # 这个循环负责设置冒泡排序进行的次数
    for i in range(len(arr) - 1):

        # j为列表下标
        for j in range(len(arr) - i - 1):  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
 

if __name__ == "__main__":
    array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
    print(bubble_sort(array))
```



### 算法2：快速排序

#### 思想

> 设要排序的数组是A[0]……A[N-1]，首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它左边，所有比它大的数都放到它右边，这个过程称为一趟快速排序。值得注意的是，快速排序不是一种稳定的排序算法，也就是说，多个相同的值的相对位置也许会在算法结束时产生变动。
>
> ![快排图](C:\Users\renyb2\Desktop\Algorithm\img\快速排序.gif)
>
> 一趟快速排序的算法是：
>
> 1）设置两个变量i、j，排序开始的时候：i=0，j=N-1；
>
> 2）以第一个数组元素作为关键数据，赋值给**key**，即**key**=A[0]；
>
> 3）从j开始向前搜索，即由后开始向前搜索(j--)，找到第一个小于**key**的值A[j]，将A[j]和A[i]的值交换；
>
> 4）从i开始向后搜索，即由前开始向后搜索(i++)，找到第一个大于**key**的A[i]，将A[i]和A[j]的值交换；
>
> 5）重复第3、4步，直到i=j； (3,4步中，没找到符合条件的值，即3中A[j]不小于**key**,4中A[i]不大于**key**的时候改变j、i的值，使得j=j-1，i=i+1，直至找到为止。找到符合条件的值，进行交换的时候i， j指针位置不变。另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束）。
>
> 
>
> 参考资料：
>
> 陈雄达，关晓飞，殷俊锋，张华隆编．数学实验：同济大学出版社，2016.08：第135页



#### python

```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/08/01
# @Author  : renyb
# @File    : sort.py


# 递归 + 分而治之
def quick_sort(arr):

    # 递归入口及出口
    if len(arr) >= 2:

        # 选取基准值，也可以选取最后一个元素
        mid = arr[0]

        # 定义基准值左右两侧的列表
        left, right = [], []
        
        # 从原始数组中移除基准值
        arr.remove(mid)

        for num in arr:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return arr


if __name__ == "__main__":
    array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
    print(quick_sort(array))
```

