print("you have ten feet of pvc pipe. Youcan cut it twice to make a triangle shaped banner. Where will you cut?")

side1 = int(input("cut one: "))
side2 = int(input("cut two: "))
side3 = 10 - side1 - side2
number1 = side1
number2 = (10 - side1)/2
number3 = number2
hp = (number1 + number2 + number3)/2
area = hp * (hp - number1)*(hp - number2)*(hp - number3) ** 0.5

print("your pieces are " + str(number1) + ", " + str(number2) + ", and " + str(number3) + " feet. " " Your area is " + str(area) + " inches.")