"""
두 수의 합
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
"""

class twoSum(object):

    def method1(self, nums, target):

        sum_dict = {}

        for i, num in enumerate(nums):
            sum_dict[num]=i
        
            if target-num in sum_dict:
                return [sum_dict[target-num], i]

    def method2(self, nums, target):
        """
        투포인터로 접근 불가
        이유1. 정렬
        이유2. 값이 아니라 인덱스 찾기라서 정렬하면 또 문제 발생
        """

        left, right = 0, len(nums)-1

        while not left == right:
            if nums[left] + nums[right] < target :
                left += 1
            elif nums[left] + nums[right] > target :
                right -= 1
            else : 
                return left, right

if __name__ == '__main__':

    nums = [2,7,11,15]
    target = 9
    print(twoSum().method1(nums, target))
    
