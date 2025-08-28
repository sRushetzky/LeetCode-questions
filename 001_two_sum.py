class Solution(object):
    def twoSum(self, nums, target):

        num_map = {}  # יצירת מילון ריק לאחסון מספרים שראינו והאינדקסים שלהם
        for i, num in enumerate(nums):  # מעבר על המערך עם אינדקסים
            complement = target - num  # חישוב המספר שחסר כדי להגיע ל-target
            if complement in num_map:  # אם המספר כבר קיים במילון
                return [num_map[complement], i]  # מחזיר את האינדקסים של שני המספרים
            num_map[num] = i  # מוסיף את המספר הנוכחי למילון עם האינדקס שלו