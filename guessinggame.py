from random import randint

r = randint(1, 100)
z = int(input("ENter the number of tries you have paid for"))
count = 1

while count <= z:
    n = int(input("Enter a number: "))

    if n == r:
        print("Congrats, you won the lottery")
        break
    elif n > r:
        print("The number is lower")
    else:
        print("The number is higher")

    count += 1
    
    
print("The lottery number is {}".format(r))