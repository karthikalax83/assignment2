program

list1=[1,2,3,4,5,6,7,8,9,10]
print("list of numbers 1to 10:",list1)
for i in list1:
    if(i%2==0):
        list1.remove(i)
print("list after even numbers removed:",list1)


output:
list of numbers 1to 10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list after even numbers removed: [1, 3, 5, 7, 9]
