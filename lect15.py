#function

def funct_add(x,y,a):
    z = int(x)+int(y)+int(a)
    return z


def funct_multiply(x,y):
    z = int(x)*int(y)
    return z


def funct_divison(x,y):
    z = int(x)/int(y)
    return z


def funct_list(my_list):
    for i in my_list:
        print(len(i))
        if i == 1:
            print("I am here")
        print(i)

my_list = [1,2,3,4,5,6,7,7,8,88,9,99,9]

print(funct_list(my_list))


#print(funct_add(2,5,6))

#print(funct_multiply(2,5))

#print(funct_divison(2,5))



