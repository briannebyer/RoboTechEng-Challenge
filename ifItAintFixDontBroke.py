# simple solution
for i in range(1,11):
    print(i)

# "optimised" solution no. 1
print(list(range(1, 11)))

# novel solution no. 1
print(', '.join(map(str, range(1, 11))))

# novel solution no. 2
print(*range(1, 11))

# novel solution no. 3
def numGenerator():
    yield from range(1, 11)

for num in numGenerator():
    print(num)

# inefficient solution no.1
def printNum(n):
    if n > 0:
        printNum(n - 1)
        print(n)

printNum(10)

# inefficient solution no.2
numberString = ""
for i in range(1, 11):
    numberString += str(i) + " "
print(numberString)

# inefficient solution no.3
for i in range(1, 11):
    eval(f"print({i})")

