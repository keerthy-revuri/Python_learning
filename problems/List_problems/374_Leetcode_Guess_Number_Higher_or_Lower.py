#We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
#
# You call a pre-defined API int guess(int num), which returns three possible results:
#
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.


# Example 1:
#
# Input: n = 10, pick = 6
# Output: 6

def guessNumber(n):
    left, right = 1, n

    while left <= right:
        mid = left + (right - left) // 2
        result = guess(mid)

        if result == 0:
            return mid
        elif result == 1:
            left = mid + 1
        else:
            right = mid - 1

def guess(num):
    # guess function which is predefined as api function in leet code
    if pick < num:
        return -1
    elif pick > num:
        return 1
    else:
        pick == num
        return 0
    pass

n = 10
pick = 2
result = guessNumber(n)
print(result)
