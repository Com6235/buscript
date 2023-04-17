print("calculator")

num1 = input("first number:")

num2 = input("second number:")

sign = input("чё сделать: \n 1) +\n 2) -\n 3) *\n 4) /\nваш оивет:")

num1 = int(num1)
num2 = int(num2)

if sign == "1" :
    otvet = num1 + num2
    print("ответ: " + str(otvet))
elif sign == "2":
    otvet = num1 - num2
    print("ответ: " + str(otvet))
elif sign == "3":
    otvet = num1 * num2
    print("ответ: " + str(otvet))
elif sign == "4":
    otvet = num1 / num2
    print("ответ: " + str(otvet))
else:
    print("ты даун?")