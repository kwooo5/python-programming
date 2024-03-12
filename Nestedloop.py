# is loop inside loop

adj = ['red', 'big', 'tasty']#3 elements 
fruits = ['apple', 'banana', 'cherry']

for x in adj:
    print('fruits')
    for y in fruits:
        print(x,y)# print statement is executed 3x3=9 times 

# pass statement 
for x in [0,1,2]:
    pass 