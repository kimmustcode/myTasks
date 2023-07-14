import xlwt 
from xlwt import Workbook 

wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')
ctr = 0

upeople = ["Ethan", "Leon", "Will", "Evan"]
dpeople = ["Kim", "Jack", "Nat"]
totalpeop = ["Kim", "Jack", "Ethan", "Leon", "Will", "Evan", "Nat"] 

ubath = ""
dbath = ""

chores = [ "", "", "", ""]
choresNames =  ["Main Bathroom", "Kitchen", "Trash", "Vacuum"] 



''' 
    Chores:
     -UBath
     -Vacuuming
     -Kitchen 
     -Trash
     -DBath
     -MBath
'''

pointerall = 0 
pointeru = 0
pointerd = 0


for i in range(30): 

    ubath = upeople[pointeru]
    dbath = dpeople[pointerd]

    sheet1.write(ctr, 0, "Upstairs Bathroom")
    sheet1.write(ctr, 1, ubath)
    ctr += 1 
    sheet1.write(ctr, 0, "Downstairs Bathroom")
    sheet1.write(ctr, 1, dbath)
    ctr += 1 

    if(pointeru == 3):
        pointeru = 0
    else:
        pointeru += 1 

    if(pointerd == 2):
        pointerd = 0
    else:
        pointerd += 1 






    for choreptr in range(4):
        if(totalpeop[pointerall] == ubath or totalpeop[pointerall] == dbath):
            
            if(pointerall != 6):
                pointerall += 1
            else:
                pointerall = 0
            if(totalpeop[pointerall] == ubath or totalpeop[pointerall] == dbath):
                if(pointerall != 6):
                    pointerall += 1
                else:
                    pointerall = 0 
        
        
        sheet1.write(ctr, 0, choresNames[choreptr])
        sheet1.write(ctr, 1, totalpeop[pointerall])
        ctr += 1 
        chores[choreptr] = totalpeop[pointerall]
        choreptr += 1 
        if(pointerall != 6):
            pointerall += 1
        else:
            pointerall = 0

    sheet1.write(ctr, 0, " ")
    sheet1.write(ctr, 1, " ")
    ctr += 1 

for x in range(len(chores)):
    print(chores[x])
print(dbath)
print(ubath)


wb.save('choresFormatTest.xlsx')
