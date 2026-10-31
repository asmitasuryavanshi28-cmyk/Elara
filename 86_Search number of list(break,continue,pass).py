numbers = [10, 20, 30, 40, 50]
search = int(input("Enter a number to search: "))

for i in numbers:
    if i == search:
        print("Number Found")
        break
else:
    print("Number Not Found")