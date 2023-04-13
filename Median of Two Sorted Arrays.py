class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        m1 = -1
        m2 = -1

        for count in (range((m+n)//2+1)):
            m2 = m1
            if(i != m and j != n):
                if nums1[i] <= nums2[j]:
                    m1 = nums1[i]
                    i+=1
                else:
                    m1 = nums2[j]
                    j+=1
            elif(i<m):
                m1 = nums1[i]
                i+=1
            else:
                m1 = nums2[j]
                j+=1
        return m1 if(m+n)% 2 == 1 else (m1+m2)/2
