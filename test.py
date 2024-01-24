num1 , num2 = input("enter two number: ").split()

try:
    answer = int(num1) / int(num2)
except ZeroDivisionError:
    print("You divided by zero")
else:
    print("you didnt raise an error")
finally:
    print(answer)
    