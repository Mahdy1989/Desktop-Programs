import re

# The pattern to be remoevd here is a string named "Batch"

f = 'Check_for_duplicates.txt'
pattern = re.compile('Batch[0-9]{6}')

dict1 = dict()

openFile = open(f, 'r')
fw = open('Checked.txt', 'w')


fw.write('Duplicates Files/lines: \n')
for row in openFile.readlines():
    a = pattern.search(str(row))
    if a is not None:
        w = a.group()
        z = row.replace(w, '')
        if z in dict1:
            count = dict1[z]
            count+=1
            dict1[z] = count
        elif z not in dict1:
            dict1[z] = 1
    

for k, v in dict1.items():
    if v > 1:
        fw.write('\t' + str(k) + '\t\t' + str(v) + '\n')


openFile.close()
fw.close()
