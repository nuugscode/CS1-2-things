print("the computer science lab needs new carpet. Input the length and width and cost per square foot to find cost")
length = int(input("length: "))
Width = int(input("Width: "))
Cost = float(input("cost per square foot: "))

area = length * Width
perimeter = (length + Width) * 2
total = area * Cost

print("area = " + str(area))
print("perimeter = " + str(perimeter))
print("total cost = " + str(total) + "$")
