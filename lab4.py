"""
Your module description
"""
# creating  
my_dict = {
    'name': 'Tom',
    'id': 123
}
print(my_dict)

# changing id
my_dict['id'] = 321
print(my_dict)

# deleting name key in dictionary
del my_dict['name']
print(my_dict)

# my tweet dictionary
my_tweet = {"tweet_id":1138,
    "coordinates": (-75, 40),
    "visited_countries": ["GR", "HK", "MY"]
    }
print(my_tweet)

# Printing number of visited countries
print(len(my_tweet['visited_countries']))

# Adding value to dictionary
my_tweet['visited_countries'] = "GR", "HK", "MY", "CH"
print(my_tweet)

# Checking if "US" is in the dictionary using .get() method
print('US' in my_tweet)

# Changing the coordinates in my_tweet
my_tweet['coordinates'] = (-81,45)
print(my_tweet)