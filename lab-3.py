# Problem 1
def first(x):
    if x==5:
        print("x equals 5")
    elif x==9:
        print("x equals 9")
    elif x==10:
        print("x equals 10")
    else:
        print("x does not equal 5, 9, nor 10")

first(3)

# Problem 2
def second(y):
    if y > 10:
        print("y is greater than 10")
    else:
        if y==5:
            print("y is 5")
        else:
            print("y is 10 or less but is not 5")

second(10)