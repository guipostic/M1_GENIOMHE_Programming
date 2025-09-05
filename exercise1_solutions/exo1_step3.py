# NOTE: function defined at the top
def add_each_letter(input_list0, input_list1):
"""
This function iteratively adds each letter of the alphabet
to each element of the input list 0
"""
    for ele in input_list0:
        for letter in alphabet:
            seq_extended = ele+letter
            #print(seq_extended)
            input_list1.append(seq_extended)

alphabet = ["A", "T", "C", "G"] # NOTE: Global variable
sequence_length = 3
mylist0 = [""] # Not empty, otherwise there would be zero iteration in "for ele" loop
mylist1 = []

for i in range(sequence_length):
    add_each_letter(mylist0, mylist1) # mylist1 will have each of its element extended by 1 char
    #mylist0 = mylist1.copy()
    mylist0 = mylist1 # Works with list copy as well
    mylist1 = []

print(mylist0)
print(len(mylist0))
