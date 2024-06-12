

# 1)

num1 = 5
num2 = 10.7
num3 = "3"
word1 = "Saba"
word2 = "motoGP"

print(int(num1))
print(int(num2))
print(int(num3))
# ქვემოთ მოცემული ორი კონვერტაციის მაგალითი ამოგვიგდებს შეცდომას, რადგან სიტყვას ვერ გადავაქცევთ რიცხვად
# print(int(word1)) # Error
# print(int(word2)) # Error 

print(str(num1))
print(str(num2))
print(str(num3))
print(str(word1))
print(str(word2))

print(float(num1))
print(float(num2))
print(float(num3))
# ქვემოთ მოცემული ორი კონვერტაციის მაგალითი ამოგვიგდებს შეცდომას, რადგან სიტყვას ვერ გადავაქცევთ ათწილადად
# print(float(word1)) # Error
# print(float(word2)) # Error

# 2)

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))
num4 = int(input("Please enter the fourth number: "))
num5 = int(input("Please enter the fifth number: "))

print(num1 + num2)
print(num3 - num2)
print(num4 * num1)
print(num3 / num5)
print(num3 // num2)
print(num1 % num5)