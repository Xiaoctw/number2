#插入排序算法
def insert_sort(lists):
    count=len(lists)
    for i in range(1,count):
        key=lists[i]
        j=i-1
        while j>=0:
            if lists[j]>key:
                lists[j+1]=lists[j]
                lists[j]=key
            j-=1
    return lists
#选择排序
def select_sort(lists):
    count=len(lists)
    for i in range(0,count):
        min=i
        for j in range(i+1,count):
            if(lists[j]<lists[min]):
                min=j#寻找最小的元素
        lists[min],lists[i]=lists[i],lists[min]
    return lists
#快速排序
def quick_sort(lists,left,right):
    if left>=right:
        return lists
    key=lists[left]
    low=left
    high=right
    while left<right:
        while left<right and lists[right]>=key:
            right-=1
        lists[left]=lists[right]
        while left<right and lists[left]<=key:
            left+=1
        lists[right]=lists[left]
    lists[right]=key
    quick_sort(lists,low,left-1)
    quick_sort(lists,left+1,high)
    return lists
#希尔排序
def shell_sort(lists):
    count=len(lists)
    step=2
    group=count//step #获得每次的步长值，
    while group>0:
        for i in range(0,group):
            j=i+group#按序递增
            while j<count:
                k=j-group
                key=lists[j]
                while k>=0:#循环终止条件
                    if lists[k]>key:
                        lists[k+group]=lists[k]
                        lists[k]=key
                    k-=group
                j+=group
        group=group//step
    return lists
