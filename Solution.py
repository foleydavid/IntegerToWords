class Solution(object):
    key_str = ["", "Thousand", "Million", "Billion", "Trillion"]
        
    eng_num = ["Zero", "One", "Two",
                   "Three", "Four", "Five",
                   "Six", "Seven", "Eight", "Nine"]
        
    tenths_place = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
    teens_num = ["Ten", "Eleven", "Twelve",
                     "Thirteen", "Fourteen", "Fifteen",
                     "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        num_list = []
        num_str = str(num)
        digits = len(num_str)
        
        #handle case of Zero
        if num == 0:
            return "Zero"

        #fill in list of values, out to 5th triplet
        for index in range(1, 5):
            value = num % pow(10, 3 * index) // pow(10, 3 * (index - 1))
            num_list.append(value)
    
        #where to begin key identifier
        max_key = len(num_list) - 1
                
        #describes each triplet found in number
        for triplet in reversed(num_list):
            
            #append string value of next triplet from 0 - 999
            ans = Solution.assignTripletString(triplet, ans)

            #assigns each triplet a suffix
            if triplet != 0:
                ans += Solution.key_str[max_key] + " "
            if max_key > 0:
                max_key -= 1
        
        return ans.strip()
    
    @staticmethod
    def assignTripletString(triplet, ans_str):
        
        #assign digits to each num in triplet
        if triplet > 99:
            first_digit = int(str(triplet)[0])
            second_digit = int(str(triplet)[1])
            third_digit = int(str(triplet)[2])
        elif triplet > 9:
            first_digit = 0
            second_digit = int(str(triplet)[0])
            third_digit = int(str(triplet)[1])
        else:
            first_digit = 0
            second_digit = 0
            third_digit = int(str(triplet)[0])
        #identifies final two digits (could be teen)
        final_two = (second_digit * 10) + third_digit

        #decribes each 'hundred'
        if first_digit > 0:
            ans_str += Solution.eng_num[first_digit] + " Hundred "
        if second_digit >= 2:
            ans_str += Solution.tenths_place[second_digit - 2] + " "
            if third_digit > 0:
                ans_str += Solution.eng_num[third_digit] + " "
        elif second_digit == 0 and triplet != 0:
            if third_digit != 0:
                ans_str += eng_num[third_digit] + " "
        elif triplet != 0:
            ans_str += teens_num[final_two - 10] + " "
            
        return ans_str
