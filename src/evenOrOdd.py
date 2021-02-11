inputList = list(map(int, input().split()))

a = inputList[0]
b = inputList[1]

if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd")