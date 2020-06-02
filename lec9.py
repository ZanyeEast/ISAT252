"""
Lecture 9 Classes
Self method should be the first argument
"""
class car:  # car is the class name
    
    maker = 'toyota' #attribute
    
    def __init__(self,input_model):
        self.model = input_model
        
    def report(self):
        #return the attribute of the instance
        return self.maker,self.model

my_car = car('corolla')
print(my_car.report())

my_car.maker = 'ford'
print(my_car.report())

''' def report_maker(self): #method
        return(self.maker)

my_car = car() #Create an instance/object

#print(my_car.maker) # has same output as code below.
print(my_car.report_maker())'''