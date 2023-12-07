"""
   Description: Finding the GCD of two numbers using recursion
   Output: See Below
   Known bugs: none
"""


def gcd(m, n):
    if (m % n) == 0:
        return n
    else:
       return gcd(n, m % n)


try:
    numbers = input("Enter the two numbers separated by space: ")
    m, n = map(int, numbers.split())
    result = gcd(m, n)
    print("The GCD of the two numbers is:", result)
except ValueError:
    print("Value Entry Occurred")
except Exception as e:
    print(f"An Error Occurred: {e}")

"""
Output
Enter the two numbers separated by space: 18 48
The GCD of the two numbers is: 6

Enter the two numbers separated by space: 18, 48
Value Entry Occurred
"""
