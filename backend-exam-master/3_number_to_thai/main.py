"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""

digits = {
    "0": "ศูนย์",
    "1": "หนึ่ง",
    "2": "สอง",
    "3": "สาม",
    "4": "สี่",
    "5": "ห้า",
    "6": "หก",
    "7": "เจ็ด",
    "8": "แปด",
    "9": "เก้า",
}

units = {
    1: "",
    10: "สิบ",
    100: "ร้อย",
    1000: "พัน",
    10000: "หมื่น",
    100000: "แสน",
    1000000: "ล้าน",
}


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        elif 0 <= number < 10:
            num_str = str(number)
            return digits[num_str]
        else:
            num_text = ""
            num_str = str(number)
            for i in range(len(num_str)):
                if num_str[i] != "0":
                    if i == len(num_str) - 1 and num_str[i] == "1":
                        num_text += "เอ็ด"
                    elif i == len(num_str) - 2 and num_str[i] == "1":
                        num_text += "สิบ"
                    elif i == len(num_str) - 2 and num_str[i] == "2":
                        num_text += "ยี่สิบ"
                    else:
                        num_text += (
                            digits[num_str[i]] + units[10 ** (len(num_str) - i - 1)]
                        )
            return num_text


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
#     10000,
#     42679,
#     82624,
#     100000,
#     215421,
#     999999,
#     1000000,
#     5555555,
# ]
# solution = Solution()
# for number in test_number_list:
#     print(f"{number}:{solution.number_to_thai(number)}")
