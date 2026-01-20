class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        last = len(digits) - 1

        for i in range(last, -1, -1):
            if digits[i] == 9:
                if i != 0:
                    digits[i] = 0
                    continue
                digits[i] = 1
                digits.append(0)
            else:
                digits[i] += 1
                return digits

        return digits
