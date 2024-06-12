

# 1)

for i in range(0, 20 + 1):
    print(i)

# 2)

number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# 3)

for i in range(5, 20 + 1, 2):
    print(i)

# 4)

sum = 0

for i in range(50, 100 + 1):
    sum = sum + i
print(sum)

# 5)

for i in range(0, 50 + 1, 5):
    print(i)

# 6)

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please neter the second number: "))

if num1 > num2:
    for i in range(num1, num2):
        print(i)
elif num1 < num2:
    for i in range(num2, num1):
        print(i)
else:
    print(num1)

# 7)

result = 1

for i in range(5, 10 + 1):
    result = result * i
print(result)

# 8)

word = "motoGP"
reversed_word = ""
for i in word[::-1]:
    reversed_word = reversed_word + i
print(reversed_word)