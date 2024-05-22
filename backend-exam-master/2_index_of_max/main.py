"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        if len(numbers) > 0:
            index = 0
            max_value = numbers[index]
            for i in range(1, len(numbers)):
                if numbers[i] > max_value:
                    max_value = numbers[i]
                    index = i
            return index
        else:
            return "list can not blank"


# input = [-5, -7, -8, -9, 1, -1, -2]
# solution = Solution()
# print(solution.find_max_index(input))
