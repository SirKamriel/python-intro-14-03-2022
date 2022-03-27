value = 666
new_value = value ** 0.5 if value < 100 else value * (-1)
print(new_value)
#####################################################
value = 666
new_value = 1 if value < 100 else 0
print(new_value)
#####################################################
value = 666
new_value = True if value < 100 else False
print(new_value)
#####################################################
value = -123
my_str = str(value) if value > 0 else str(value)[::-1]
print(my_str)
#####################################################
my_str = "qwer"
my_str = my_str * 2 if len(my_str) <5 else my_str
print(my_str)
#####################################################
my_str = "qwer"
my_str = my_str + my_str[::-1] if len(my_str) <5 else my_str
print(my_str)