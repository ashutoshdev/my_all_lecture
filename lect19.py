from inspect import trace


check_age = [18,19,20,30]

def test(xyz):
    if xyz== 18:
        return True
    else:
        return False

check_test =  filter(test,check_age)      

for i in check_test:
    print(i)     