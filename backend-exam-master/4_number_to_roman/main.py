"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""

roman_value = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


class Solution:

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        elif number == 0:
            return "number can not equal 0"
        elif number > 3999:
            return "number can not more than 3999"
        else:
            roman_text = ""
            while number > 0:
                for roman, value in roman_value.items():
                    if number >= value:
                        roman_text += roman
                        number -= value
                        break

            return roman_text


# test_number_list = [
#     0,
#     1,
#     10,
#     11,
#     20,
#     100,
#     111,
#     121,
#     999,
#     1000,
#     1001,
#     1011,
#     1021,
#     2555,
#     3999,
# ]
# solution = Solution()
# for number in test_number_list:
#     print(f"{number}:{solution.number_to_roman(number)}")
