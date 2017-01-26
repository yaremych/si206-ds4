# function to return the factorial of a number
import unittest
# Add comments
def factorial(num):
    ans = 1
    if num < 0:
        return None
    elif num < 2:
        return ans
    else:
        for i in range(1, num + 1):
            ans = ans * i
        return ans


# function to check if the input year is a leap year or not
def check_leap_year(year):
    isLeap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                isLeap = True
        else:
            isLeap = True
    return isLeap

print("factorial(0): {}".format(factorial(0)))
print("factorial(1): {}".format(factorial(1)))
print("factorial(5): {}".format(factorial(5)))
print("factorial(-3): {}".format(factorial(-3)))

print("check_leap_year(2000): {}".format(check_leap_year(2000)))
print("check_leap_year(1990): {}".format(check_leap_year(1990)))
print("check_leap_year(2012): {}".format(check_leap_year(2012)))
print("check_leap_year(2100): {}".format(check_leap_year(2100)))

print("\n\n***Starting Tests***\n\n")

class LeapYearTests(unittest.TestCase):
    def test_leap_year(self):
        t1 = check_leap_year(2001)
        self.assertEqual(t1, False)

    def test_leap_year2(self):
        t1 = check_leap_year(2016)
        self.assertEqual(t1, True)

    def test_leap_year3(self):
        t1 = check_leap_year(0)
        self.assertEqual(t1, True)


class FactorialTests(unittest.TestCase):
    def test_factorial1(self):
        f1 = factorial(3)
        self.assertEqual(f1, 6)

    def test_factorial2(self):
        f1 = factorial(2)
        self.assertEqual(f1, 2)

    def test_factorial3(self):
        f1 = factorial(-100)
        self.assertEqual(f1, None)


unittest.main(verbosity=2)
