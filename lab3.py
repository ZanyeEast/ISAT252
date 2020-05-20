"""
Your module description
"""
# Creating Variable list
str_list = ['a', 'd', 'e', 'b', 'c']
print(str_list)

# Sorting the list using .sort method
str_list.sort()
print(str_list)

# Adding strings to list using the .append() method
str_list.append('f')
print(str_list)

# Removing string from list using the .remove() method
str_list.remove('d')
print(str_list)

# Printing one string from the list using print(str_list[]) method
print(str_list[2])

# Creating new list, my_list
my_list =['a',' 123', 123, 'b', 'B', 'False', False, 123, None, 'None']
print(my_list)
print(len(set(my_list)))
# There are 9 unique items in my_list

# Calculating the number of words in a sentence 
message = "This is my third python lab."
# The number of words in the sentence above.
print(len(message.split()))

# Creating a list of numbers
num_list = [12, 32, 43, 35]
"""
My method for printing max and min without using the max() or min() function. 
Instead I will sort the list in ascending order and print the first and last 
value in the list
"""
num_list.sort()
# Printing the minimum value and maximum value.
print(num_list[0], num_list[-1])

# Game board list
game_board =[[0,0,0,], [0,0,0], [0,0,0]]
game_board[1] = [0,1,0]
print(game_board)