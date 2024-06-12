# 1)

# While loop

num = 0

while num != 10:
    print(num)
    num = num + 1

num1 = 5
num2 = 13

while num1 != num2:
    num1 = num1 + 1
    print(num1)

number = 20

while number < 25:
    number = number + 1
    print(number)

number = 10
while number > 0:
    number = number - 1
    print(number)

# მოცემული while loop-ი უსასრულოა რადგან num-ის მნიშვნელობა არასდროს არ იქნება 10

# num = 0

# while num != 10:
#     print(num)

# For loop

for i in range(1,10 + 1):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(0, 20 + 1, 2):
    print(i)

for i in range(1, 20 + 1, 2):
    print(i)

word = "Saba"
for i in word:
    print(i)

# if/elif/else

num1 = 15
num2 = 20

if num1 > num2:
    print(num1, ">" ,num2)
elif num1 < num2:
    print(num1, "<" ,num2)
else:
    print(num1, "=" ,num2)

if num1 > num2 == False:
    print(num1, "<" ,num2)
elif num1 < num2 == False:
    print(num1, ">" ,num2)
else:
    print(num1, "=" ,num2)

word1 = "Saba"
word2 = "motoGp"

if len(word1) > len(word2):
    print(word1, ">" ,word2)
elif len(word1) < len(word2):
    print(word1, "<" ,word2)
else:
    print(word1, "=" ,word2)

num = 5

if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

word = "Saba"

if "a" in word:
    print(True)
else:
    print(False)