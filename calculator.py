what = input ("Выберите операцию (+, -, *, /, **, //, %): ")

a = float ( input ("Введи первое число: "))
b = float ( input ("Введи второе число: "))
c=0;

if what == "+":
	c = a + b
	print("Результат: " + str(c))

elif what == "-":
	с = a - b
	print("Результат: " + str(c))

elif what == "*":
	с = a * b
	print("Результат: " + str(c))

elif what == "/":
	с = a / b
	print("Результат: " + str(c))

elif what == "**":
	с = a ** b
	print("Результат: " + str(c))

elif what == "//":
	с = a // b
	print("Результат: " + str(c))

elif what == "%":
	с = a % b
	print("Результат: " + str(c))

else: print("Такой операции в калькуляторе нет") 