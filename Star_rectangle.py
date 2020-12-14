n = int(input())
space = " "
print(n*"*")

for i in range(n-2):
    if n >3:
        print("*", space * (n - 4), "*")
    else:
        print("*", "*")
print(n*"*")

