def greet():
    print("Hello and welcome in arun guide.")

greet()  # isko function call  bolte hain.



### : *args----> multiple position arguments

def sum_total(*numbers):
    total = 0 
    for i in numbers:
        total += i
    return total

total = sum_total(1,2,3,4,5,6,76)
print(total)