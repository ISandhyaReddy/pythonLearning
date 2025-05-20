##6.binarysearch
a = [9, 11, 13, 14, 15, 18, 21, 25, 29, 31]
low = 0
high = len(a) - 1
mid = (low + high // 2)
print(mid)
target = 9
while low <= mid:
    # mid=(low+high//2)
    if a[mid] == target:
        print(mid)
        break
    elif a[mid] < target:
        low = mid + 1
    else:
        high = mid - 1