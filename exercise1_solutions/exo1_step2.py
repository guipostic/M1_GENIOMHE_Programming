
alphabet = ["A", "T", "C", "G"]

seq_init = "N"

mylist0 = ["foo"]
mylist1 = []

for ele in mylist0:
    for letter in alphabet:
        seq_extended = seq_init+letter
        mylist1.append(seq_extended)

print(mylist1)
# ['NA', 'NT', 'NC', 'NG']

mylist2 = []

for ele in mylist1:
    for letter in alphabet:
        seq_extended = ele+letter
        mylist2.append(seq_extended)

print(mylist2)
# ['NAA', 'NAT', 'NAC', 'NAG', 'NTA', 'NTT', 'NTC', 'NTG', 'NCA', 'NCT', 'NCC', 'NCG', 'NGA', 'NGT', 'NGC', 'NGG']

mylist3 = []

for ele in mylist2:
    for letter in alphabet:
        seq_extended = ele+letter
        mylist3.append(seq_extended)

print(mylist3)
# ['NAAA', 'NAAT', 'NAAC', 'NAAG', 'NATA', 'NATT', 'NATC', 'NATG', 'NACA', 'NACT', 'NACC', 'NACG', 'NAGA', 'NAGT', 'NAGC', 'NAGG', 'NTAA', 'NTAT', 'NTAC', 'NTAG', 'NTTA', 'NTTT', 'NTTC', 'NTTG', 'NTCA', 'NTCT', 'NTCC', 'NTCG', 'NTGA', 'NTGT', 'NTGC', 'NTGG', 'NCAA', 'NCAT', 'NCAC', 'NCAG', 'NCTA', 'NCTT', 'NCTC', 'NCTG', 'NCCA', 'NCCT', 'NCCC', 'NCCG', 'NCGA', 'NCGT', 'NCGC', 'NCGG', 'NGAA', 'NGAT', 'NGAC', 'NGAG', 'NGTA', 'NGTT', 'NGTC', 'NGTG', 'NGCA', 'NGCT', 'NGCC', 'NGCG', 'NGGA', 'NGGT', 'NGGC', 'NGGG']

