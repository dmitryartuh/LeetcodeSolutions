class Solution:
    def try_i(self, nums: [], m_i: int) -> bool:
        for i in range(1, m_i):
            if nums[i-1] > nums[i]:
                print(i, nums[i-1], '>', nums[i])
                return False
        for i in range(m_i + 1, len(nums)):
            if nums[i-1] > nums[i]:
                print(i, nums[i-1], '>', nums[i])
                return False
        if m_i != 0 and nums[0] < nums[-1]:
            return False

        return True

    def check(self, nums: List[int]) -> bool:
        m_is = set([0])
        m = nums[0]
        for i in range(len(nums)):
            if nums[i] < m:
                m = nums[i]
                m_is.clear()
                m_is.add(i)
            elif nums[i] == m:
                m_is.add(i)
        for m_i in m_is:
            if self.try_i(nums, m_i):
                return True

        return False