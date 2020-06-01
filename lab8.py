
"""
Lab 8 Functions
"""
#3.1
def demo_str(str):
    words = str.split()
    
    return words
#3.2 testing 
print(len(demo_str('hello world!')))

#3.3
num_list = [1,2,3,4,5,6]

def find_min(inpu_list):
    min_item = num_list[0]
    for num in inpu_list:
        if type(num) is not str:
            if min_item >= num:
                 min_item=num
    return min_item
demo_list= [1,2,3,4,5,6]
print(find_min((demo_list)))

mix_list=[1,2,3,4,'a',6]
print(find_min(mix_list))