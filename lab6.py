"""
Lab 6. for loop and range function
"""
#3.1 printing numbers 0 through 6 excluding 3 and 6
for each_num in range(6):
    if each_num != 3:
        print(each_num)

#3.2 Printing 5!
fact = 1
for factorial in range(1,6):
    fact = fact * factorial
print(fact)
    
#3.3 Printing sum of range(1,6)
num1=0
for num in range(1,6):
    num1 = num1 + num
print(num1)

#3.4 
result = 1
for code in range(3,9):
    result = result * code
print(result)

#3.5
product=1
for number in range(1,9):
    product=product*number
    
div=1
for div_num in range(1,4):
    div=div*div_num
final_ans=product/div
print(final_ans)

#3.6
'''my_str = 'this is my 6th string'
for str_item in my_str:
    x=len(my_str.split())
print(x)'''
y=0
 
for word in 'this is my 6th string'.split():
     y=y+1
print(y)
#3.7
my_tweet = {
    "favorite_count":1138,
    "lang":'en',
    "coordinates":(-75,40),
    "entities": {"hashtags":["Preds", "Pens", "SingintoSprint"]}
    }
z=0
for hash_tag in my_tweet ["entities"]["hashtags"]:
    z=z+1
print(z)