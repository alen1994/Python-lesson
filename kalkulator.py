x = int(input("Vpišite x: "))
y = int(input("Vpišite y: "))

z = input("Izberi +, -, *, /: ")

if z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
elif z == "*":
    print(x * y)
elif z == "/":
    print(x / y)
else:
    print("Niste izbrali matematične operacije.")
