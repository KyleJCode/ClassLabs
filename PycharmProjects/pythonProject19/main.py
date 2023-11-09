def moveZeroes(nums):
    mylist = [(nums.pop(nums.index(i))) for i in range(len(nums)) if nums[i] == 0]

def main():
    nums = [0, 0, 1, 4, 5, 6]
    moveZeroes(nums)


main()

