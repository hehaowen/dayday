class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list3 = []
        s1 = 0
        s2 = 0
        for i in range(len(l1)):
            s1 += (l1[i] * 10 ** i)
        for j in range(len(l2)):
            s1 += (l2[j] * 10 ** j)
        s3 = str(s1 + s2)
        for z in s3:
            list3.append(z)
        list3 = list3[::-1]
        l4 = []
        for l3 in list3:
            l4.append(int(l3))
        return l4


if __name__ == '__main__':
    l1 = [2, 4, 3,6]
    l2 = [5, 6, 4]
    s = Solution()
    l4 = s.addTwoNumbers(l1, l2)
    print(l4)
