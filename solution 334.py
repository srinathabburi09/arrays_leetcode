class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")   # we need to get triplets in an ascending order to get triplets in a sequential order we set first and second as infinty as there are min_numbers than the last or third element
        for num in nums:          #iterating over the loop 
            if num <= first:          
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False       

#example = nums = [2,1,5,0,4,6] # output = true
#so during the iteration of loop
#initially first and second are infinity.So we set first element in nums as first and if next element in an array nums is less than the first we update next element as first, if not we simply update second as the next element in an array
#we perform same as for second, if we didnt found the element is less than the both first and second it is the maximum element and we found the last element which is larger than both two
#so we return True and if not false
#lets dive into the example
#for 1st iteration over loop => num = 2 and 2 <= first, so first = 2
#2nd iteration => num = 1 and 1(num) < 2(first) =>so first = 1 we update to itd
#3rd iteration =>num = 5 and num > first it exits if loop and enter elif so num <= second,so second = num(5)
#4th iteration => num = 0 and num <= first = so we update it to 0,first = 0
#5th iteration => num = 4 and 4(num) is less than second(5) so we update it to second = 4
#6th iteration => num = 6 it larger than both first and second so we retur True
