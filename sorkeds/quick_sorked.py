# coding:utf-8


def quick_sorked(alist,start,end):

    if start >= end:
        return

    mid_value = alist[start]
    left = start
    right = end

    while left < right:
        while(left < right and alist[right] >= mid_value):
            right -= 1
        alist[left] = alist[right]
        while(left < right and alist[left] < mid_value):
            left += 1
        alist[right] = alist[left]

    alist[left] = mid_value
    quick_sorked(alist,start,left-1)
    quick_sorked(alist,left+1,end)


if __name__ == '__main__':
    alist = [45,2,65,787,45,23,98,36,52]
    print (alist)
    quick_sorked(alist,0,len(alist)-1)
    print (alist)
