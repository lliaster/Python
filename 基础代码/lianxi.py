# -*- coding: utf-8 -*-
# @Time     : 2024/10/20 22:31
# @Author   : Lliaster
# @File     : lianxi.py


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
from copy import deepcopy
from itertools import count

from setuptools.command.rotate import rotate


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
        for item in s1:
            c = list()
            for item2 in s2:

                print(f'循环1值{item},循环2值{item2}')
                if item == item2:
                    c.append(True)
                else:
                    c.append(False)

            print(f'循环2结果{c}')
            if True in c:
                b.append(True)
            else:
                b.append(False)
                break
        print(f'结果{b}')
        if b == [True, True, True]:
            return True
        else:
            return False


str_test = Solution()
print(str_test.CheckPermutation("abc", "bac"))
print(str_test.CheckPermutation("abb", "aab"))
"""
"""
面试题 01.02. 判定是否互为字符重排
尝试过
简单
相关标签
相关企业
提示
给定两个由小写字母组成的字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true 
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false
说明：

0 <= len(s1) <= 100 
0 <= len(s2) <= 100 """
"""
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        repeat = bool()
        if len(s1) == len(s2):
            for item in s1:
                if s1.count(item) == s2.count(item):
                    repeat = True
                else:
                    repeat = False
                if not repeat:
                    return False

            else:
                return True
        else:
            return False


str_test = Solution()
print(str_test.CheckPermutation("abc", "bac"))
print(str_test.CheckPermutation("abb", "aab"))
print(str_test.CheckPermutation("a", "ab"))

"""


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        list1 = list(s1)
        list2 = list(s2)
        if len(list1) == len(list2):
            for item in list1:
                if item in list2:
                    list2.remove(item)
                else:
                    return False
            else:
                return True
        else:
            return False


str_test = Solution()
print(str_test.CheckPermutation("abc", "bac"))
print(str_test.CheckPermutation("abb", "aab"))
print(str_test.CheckPermutation("a", "ab"))

print('X' * 55)


class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        S = S[:length]
        print(S)
        return S.replace(' ', '%20')


class Solution2:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(' ', '%20')


str1 = Solution2()
print(str1.replaceSpaces("Mr John Smith    ", 13))


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        a = 0
        for i in set(s):
            if s.count(i) % 2 != 0:
                a += 1
        if a > 1:
            return False
        else:
            return True


s = Solution()
print(s.canPermutePalindrome("code"))
print(s.canPermutePalindrome("aab"))
print(s.canPermutePalindrome("a"))

print('一次编辑', 'X' * 55)


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        lf, ls = len(first), len(second)
        if first == second:
            return True
        if lf < ls:
            return self.oneEditAway(second, first)
        elif lf - ls > 1:
            return False

        num = 0
        fnum = 0
        if lf == ls:
            for item in first:
                if item == second[num:num + 1]:
                    num += 1
                elif item != second[num:num + 1]:
                    fnum += 1
                    num += 1
            if fnum <= 1:
                return True
            return False
        else:
            num = 0
            fnum = 0
            while num < ls:
                if second[num] != first[num + fnum]:
                    fnum += 1
                    if fnum > 1:
                        return False
                else:
                    num += 1
            return True


s = Solution()
print(s.oneEditAway("spartan", "part"))
print(s.oneEditAway("teacher", "treacher"))
print(s.oneEditAway("islander", "slander"))
print(s.oneEditAway("teacher", "teache"))
# "teacher"
# "treacher"

print('字符串压缩', 'X' * 55)


class Solution2:
    def compressString(self, S: str) -> str:
        x, y, l_s = 0, 0, len(S)
        res = []
        while x < l_s:
            while y < l_s and S[x] == S[y]:
                y += 1
            res.append(S[x])
            res.append(str(y - x))
            x += 1
            x = y
        return ''.join(res) if len(res) < l_s else S


S = Solution2()
print(S.compressString("aabcccccaaa"))

print('旋转矩阵', 'X' * 55)


class Solution:
    def rotate(self, matrix) -> None:
        new_lst = deepcopy(matrix)
        i = 0
        lo = len(matrix)
        while i < lo:
            j = 0
            while j < lo:
                temp = new_lst[lo - i - 1][j]
                matrix[j][i] = temp
                j += 1
            i += 1

        print(matrix)


s = Solution()
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(s.rotate(lst))

print('旋转矩阵2', 'X' * 55)


class Solution:
    def rotate(self, matrix) -> None:
        x, y = 0, 0
        n = len(matrix)
        while x < n//2:
            while y < (n+1)//2 :
                temp = matrix[x][y]
                matrix[x][y] = matrix[n - y- 1][x]
                matrix[n - y - 1][x] = matrix[n -y-1][n-x-1]
                matrix[n - y - 1][n - x - 1] = matrix[y][n - x - 1]
                matrix[y][n - x - 1] = temp
                y += 1
            x +=1
        print(matrix)
truelst=[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
s = Solution()
lst = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]

s.rotate(lst)
