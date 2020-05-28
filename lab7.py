"""
Lab 7. While Loop
"""

#3.1
current_number =-1
while current_number <6:
    current_number +=1
    if (current_number==3 or current_number==6):
        continue
    print(current_number)
    
#3.2
num = 5
factorial = 1
while num > 1:
    factorial = factorial * num
    num = num -1
print(factorial)

#3.3
n = 5
numb1=0
i=1

while i <=n:
    numb1 = numb1 + i
    i = i+1
print(numb1)

#3.4
x=3
product = 1
while x in range(3,9):
    product=product*x
    x=x+1
print(product)


#3.5
z=4
result=1

while z <=8:
    result = result *z
    z= z+1
print(result)

#3.6
num_list = [12, 32, 43, 35]
print(num_list)
while num_list:
    num_list.pop(0)
    print(num_list)
