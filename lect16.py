#lambda

# x = lambda y:y+10

# print(x(5))

# x = lambda y,z:y+z

# print(x(5,6))




def my_test(n):
    return lambda y:y*n

test2 = my_test(12)   

print(test2(6))




