# -*- coding: utf-8 -*-
"""summer training 14 july.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BwLdlPThIth9kEH1CPk0tU0MgtTrHX4t

print simple interest using function
"""

def si(p, r, t):
  simpleinterest = (p*r*t)/100
  print(simpleinterest)
si(1000, 10, 10)

"""create a function to find the sum of all natural number between 1 to 50"""

def sum_n(a, b):
  sum = 0
  for i in range(a, b):
    sum += i
    print(sum)
sum_n(1, 50)

"""sum of odd natural number"""

def sum_odd(a, b):
  sum = 0
  for i in range(a, b):
    if i % 2 != 0:
      sum += i
      print(sum , "+", i, "=", sum)
sum_odd(1, 51)

"""return"""

def add(a, b):
  c=a+b
  return c
add(10, 20)

"""lambda"""

add = lambda a, b:a+b
add(10,20)

try:
  num1 = int(input("enter numerator:"))
  num2 = int(input("enter denominator:"))
  result = num1 / num2
except ZeroDivisionError:
  print("Error: cannot divide by zero")

except ValueError:
  print("Error: please enter valid integers only")

else:
  print("Result is: ", result)
finally:
  print("Program ended, thank you")

def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n-1)
print(factorial(5))

def reve(srrg):
  if len(srrg) == 0:
    return srrg
  else:
    return reve(srrg[1:]) + srrg[0]
print(reve("hello"))

def Numsqr(n):
   sqr = n**2
   return sqr
print(Numsqr(2))

def add_numbers(a, b):
    result = a + b
    return result
sum = add_numbers(5, 3)
print("The sum is:", sum)

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
number = 10
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is not even.")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
factorial(5)
print("Factorial of", num, "is", factorial(num))

def find_largest(num):
    if not num:
        return None
    largest = num[0]
    for numb in num:
        if numb > largest:
            largest = numb
    return largest
find_largest([1,4,2])

def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
fibonacci_series(5)

def count_vowels(strg):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in strg:
        if char in vowels:
            count += 1
    return count
count_vowels("hello")

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
sum_all(1,2,3)

def is_palindrome(strg):
    cleaned = strg.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
is_palindrome("hello")

def password(pw, attempt):
  for i in range(attempt):
    num = input("enter password: ")
    if num == "forget":
       attempt -= 1
       print(f"{attempt} attempts left.")
       continue
    if num == password:
       print("Access granted")
       break
    else:
       attempt -= 1
       print(f"wrong password {attempt} attempts left.")
password("abc@123", 5)