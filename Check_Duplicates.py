import re

# The Batch number is removed.
# for this check to be valid, no other information should be deleted or changed

f = 'DupCheck.txt'
batchp = re.compile('Batch[0-9]{3}')

d = {}

openFile = open(f, 'r')
w = open('Checked.txt', 'w')


w.write('Duplicates Files/lines: \n')
for row in openFile.readlines():
    a = batchp.search(str(row))
    if a is not None:
        w = a.group()
        z = row.replace(w, '')
        if z in d:
            c = d[z]
            c+=1
            d[z] = c
        elif z not in d:
            d[z] = 1
    

for k, v in d.iteritems():
    if v > 1:
        w.write('\t' + str(k) + '\t\t' + str(v) + '\n')


openFile.close()
w.close()
