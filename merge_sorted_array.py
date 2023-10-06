class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n -1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
                
        # nums1 can be empty
        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1


nums1 = [1,2,3,0,0,0]
nums2 = [4,5,6]
"""
space complexity O(1)
time complexity O(m + n)

we are supposed to merge the two arrays into one without creating a new holder array,
we will put two pointers at the end of each arrays and decreament the pointer towards the
index zero. In each index we compare the value and then append the value at the end of one 
array which will contain all other array inside it.
we will iterate through until the first block of while loop is complete.
There might be a case where nums1 array might have an empty array and only nums2 has elements
therefore we will iterate through the nums2 array and append to it that's why we have the second while
loop.
"""