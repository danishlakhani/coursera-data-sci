import csv
test_file_object = csv.reader(open('test.csv', 'rb'))
open_file_object = csv.writer(open("treemodel.csv", "wb"))
header = test_file_object.next()

pclass = 0
sex = 2
age = 3

for row in test_file_object:  
    print str(row)
    if row[age] == '':
        row.insert(3,'25')
    if row[pclass] == '1':
        if row[sex] == 'female':
            row.insert(0,'1')
        if row[sex] == 'male' and float(row[age]) < 5:
            row.insert(0,'1')
        else: 
            row.insert(0,'0')
    if row[pclass] == '2':
        if row[sex] == 'female':
            row.insert(0,'1')
        if row[sex] == 'male':
            row.insert(0,'0')  
    if row[pclass] == '3':   
        row.insert(0,'0')   
    open_file_object.writerow(row) 
