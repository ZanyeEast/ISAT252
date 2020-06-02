"""
Lab 9 classes
"""


#3.1
class my_stat():
    # sigma
    def cal_sigma(self,m,n):
        self.result = 0
        for i in range (n,m+1):
            self.result = self.result + i
        return self.result
    # pi    
    def cal_pi(self,m,n):
        self.result = 1
        for i in range(n,m+1):
            self.result = self.result * i
        return self.result
    # factorial
    def cal_f(self,m):
        if m == 0:
            return 1
        else:
            return m* self.cal_f(m-1)
    # Permutation
    def cal_p(self,m,n):
        return self.cal_f(m)/self.cal_f(m-n)
    
    
#3.2
# printing sigma
my_cal_sigma = my_stat()
print(my_cal_sigma.cal_sigma(5,3))

# Printing pi
my_cal_pi = my_stat()
print(my_cal_pi.cal_pi(5,3))

# Printing factorial
my_cal_f = my_stat()
print(my_cal_f.cal_f(5))

# Printing Permutation
my_cal_p = my_stat()
print(my_cal_p.cal_p(5,3))