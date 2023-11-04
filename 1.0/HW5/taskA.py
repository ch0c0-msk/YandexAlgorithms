def findMinDiff(nums1, nums2):
    pnt1 = 0
    pnt2 = 0
    res1 = nums1[0]
    res2 = nums2[0]
    minDiff = abs(nums1[0] - nums2[0])
    while(pnt1 != len(nums1) and pnt2 != len(nums2)):
        nowDiff = abs(nums1[pnt1] - nums2[pnt2])
        if nowDiff < minDiff:
            res1 = nums1[pnt1]
            res2 = nums2[pnt2]
            minDiff = nowDiff
        if nums1[pnt1] < nums2[pnt2]:
            pnt1 += 1
        else:
            pnt2 += 1
    return res1, res2

def main():
    len1 = int(input())
    nums1 = [int(i) for i in input().split()]
    len2 = int(input())
    nums2 = [int(i) for i in input().split()]
    [print(i, end = " ") for i in findMinDiff(nums1, nums2)]

if __name__ == "__main__":
    main()