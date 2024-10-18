# -*- coding: utf-8 -*-
# @Time    : {Date} {Time}
# @Author  : Lliaster
# @File    : {File}.py


"""

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数
是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。


示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。


提示：

-231 <= x <= 231 - 1


进阶：你能不将整数转为字符串来解决这个问题吗？

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x >= 0:
            x = str(x)
            if x == x[::-1]:
                print(x)
                return True
            else:
                return False
        else:
            return False


a = Solution()
b = a.isPalindrome(121)
print(b)


class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)


print('x' * 50)

"""
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        b = list()
        c = list()
        for item in s1:
            for item2 in s2:
                print(item, item2)
                if item == item2:
                    c.append(True)
                else:
                    c.append(False)
                # print(c)
            if True in c:
                b.append(True)
            else:
                b.append(False)
        print(b)
        if b == [True, True, True]:
            return True
        return False


str_test = Solution()
print(str_test.CheckPermutation("abc", "bac"))
print(str_test.CheckPermutation("abb", "aab"))
"""


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        a = bool()
        for item in s1:
            if s1.count(item) == s2.count(item):
                a = True
            else:
                a = False
            if a == False:
                return False
                break
        else:
            return True


str_test = Solution()
print(str_test.CheckPermutation("abc", "bac"))
print(str_test.CheckPermutation("abb", "aab"))


b = 'abcv'
print(b.count('a'))