n = int(input())  # number of statements
x = 0

for i in range(n):
    statement = input()
    if "++" in statement:
        x = x + 1
    else:
        x = x - 1

print(x)
