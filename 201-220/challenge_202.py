'''
Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
Do not convert the integer into a string.
'''

def intIsPalindrome(num: int):
    def rIntIsPalindrome(num, digits):
        # End case: 1 or 0 digits left.
        if digits <= 1:
            return True

        # Check that the first and last digits are the same.
        # First digit in num is equal to the integer quotient of num divided by 10 to the power of the number of digits in num minus 1.
        # Last digit in num is equal to num modulo 10.
        digit_factor = 10 ** (digits-1)
        if num // digit_factor == num % 10:
            # Recur with the first and last digits removed from num, and subtract 2 from the 'digits' variable.
            return rIntIsPalindrome(num % digit_factor // 10, digits - 2)
        else:
            # First and last digits are not equal.
            return False 

    num = abs(num) # Including negative integers.
    digits = 0
    pow10 = 1
    while pow10 <= num:
        digits += 1
        pow10 *= 10

    return rIntIsPalindrome(num, digits)

print(intIsPalindrome(121))
print(intIsPalindrome(888))
print(intIsPalindrome(678))
print(intIsPalindrome(123454321))
print(intIsPalindrome(1234554321))