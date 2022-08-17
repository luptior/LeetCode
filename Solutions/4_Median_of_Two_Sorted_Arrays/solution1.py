class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:

        total_len = len(nums1) + len(nums2)

        if total_len % 2 == 1:
            mid = total_len // 2 + 1

            counter = 1

            while counter < mid + 1:
                if len(nums1) > 0 and len(nums2) > 0:
                    if nums1[0] <= nums2[0]:
                        tmp = nums1.pop(0)
                    else:
                        tmp = nums2.pop(0)
                elif len(nums1) > 0 and len(nums2) == 0:
                    tmp = nums1.pop(0)
                else:
                    tmp = nums2.pop(0)
                counter += 1

            return tmp


        else:
            mid = total_len // 2

            counter = 1

            median = []

            while counter < mid + 2:

                if len(nums1) > 0 and len(nums2) > 0:
                    if nums1[0] <= nums2[0]:
                        tmp = nums1.pop(0)
                    else:
                        tmp = nums2.pop(0)
                elif len(nums1) > 0 and len(nums2) == 0:
                    tmp = nums1.pop(0)
                else:
                    tmp = nums2.pop(0)

                if counter == mid:
                    median.append(tmp)
                elif counter == mid + 1:
                    median.append(tmp)
                    return sum(median) / 2

                counter += 1



