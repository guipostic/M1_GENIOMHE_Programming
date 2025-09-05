
def try_to_modify_list(input_list):
    input_list.append('lol')

mylist = ['A', 'B', 'C']
try_to_modify_list(mylist)
print(mylist)

# CONCLUSION 1: no need for a return in the function

# ------------------------------------------------------------------------------

def try_to_modify_charchain(input_charchain):
    input_charchain = input_charchain + 'lol'
    return input_charchain

mycharchain = 'ABCD'
foo = try_to_modify_charchain(mycharchain)
print(mycharchain)
print(foo)

# CONCLUSION 2: need for a return in the function
