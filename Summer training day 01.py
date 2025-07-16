# ************** python Basics  **************8

# Data Structures 
# (list, set, dictionaries)

# Data Types
# (Integer, string, float, boolean, complex number)

# Variables
# ((a-z), (A-Z), (_ in mid))

# operator
# (1) Arithmetic operator
# (+, -, *, /, %, //, **)
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# (2) Assignment operator
# (=, =+, +=, =-, -=, /=, //=, %=, *=)
x = 5
print("x:", x)
x += 2
print("x += 2:", x)
x -= 1
print("x -= 1:", x)
x *= 3
print("x *= 3:", x)
x /= 2
print("x /= 2:", x)
x **= 2
print("x **= 2:", x)
x //= 3
print("x //= 3:", x)
x %= 2
print("x %= 2:", x)

# (3) Comparison operator
# (<, >, <=, >=, !=, ==)
a=11
b=21
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# (4) Logical operator
# (and, or, not)
print((11<23) and (10>3))
print((11>23) or (11<44))
print(not (10>1))

# (5) Membership operator
# (in, not in)
x = [1, 2, 3, 4, 5]
for i in x:
    if i == 3:
        print("3 is found")

# (6) Bitwise operator
# (&, |, !)
x = 5      # 0101
y = 3      # 0011
print("x & y:", x & y)     # 0001 => 1
print("x | y:", x | y)     # 0111 => 7



# (7) Identity operator
# (is, is not)
a = 3
b = 2
print("a is b:", a is b)
print("a is not b:", a is not b)

#---------Calculator---------#

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /, %, //, **): ")
if operator == '+':
    print("Result:", first + second)
elif operator == '-':
    print("Result:", first - second)
elif operator == '*':
    print("Result:", first * second)
elif operator == '/':
    print("Result:", first / second)
elif operator == '%':
    print("Result:", first % second)
elif operator == '//':
    print("Result:", first // second)
elif operator == '**':
    print("Result:", first ** second)
else:
    print("Invalid operation!")
