import csv
import time
#you need to download the errors dump first, from https://keepright.at/keepright_errors.txt.bz2 and unzip it
#make sure you have python 3+ installed
print ("Welcome to the keepright error filter")
workDir = input("insert the path where keepright_errors.txt file can be found:")
print(workDir)
print (
    """
        non-closed areas ----- 30
        dead-ended one-ways ----- 40
        almost-junctions ----- 50
        missing tags ----- 70
        motorways without ref ----- 90
        places of worship without religion ----- 100
        point of interest without name ----- 110
        ways without nodes ----- 120
        floating islands ----- 130
        railway crossings without tag ----- 150
        wrongly used railway crossing tag ----- 160
        fixme-tagged items ----- 170
        relations without type ----- 180
        highway-highway ----- 191
        highway-highway ----- 201
        loopings ----- 210
        misspelled tags ----- 220
        mixed layers intersections ----- 231
        strange layers ----- 232
        motorways connected directly ----- 270
        missing name ----- 281
        not closed loop ----- 283
        
        TURN RESTRICTIONS
        missing type ----- 291
        missing from way ----- 292
        missing to way ----- 293
        from or to not a way ----- 294
        via is not on the way ends ----- 295
        wrong restriction angle ----- 296
        wrong direction of to member ----- 297
        already restricted by oneway ----- 298
        
        not closed loop ----- 311
        wrong direction ----- 312
        faintly connected ----- 313
        *_link-connections ----- 320
        bridge-tags ----- 350
        missing turn restriction ----- 401
        impossible angles ----- 402
        domain hijacking ----- 412
        deprecated tags ----- 60
        missing maxspeed ----- 300
    """
)
ErrOpt = input ("Enter values for the category you want separated by commas ex: 210,300 :  ")
print(ErrOpt)
ErrOpt = ErrOpt.split((","))
print(ErrOpt)
second_col=[]
print(
    """
    USA  21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67
    CANADA 20,21,22,23
    """
)
AreaOpt = input ("Enter the values for your area of interest separated by coma :    ")
AreaOpt = AreaOpt.split((","))
timestr = time.strftime("%Y%m%d-%H%M%S")  #timestamp for file
with open(str(workDir) + '/keepright_errors.txt', encoding='latin-1', newline='') as csvfile, open(str(workDir) + '/keepright-' + timestr + '.csv', 'w', encoding='latin-1') as o:
    citire = csv.reader(csvfile, delimiter='\t')
    next(citire, None)
    scriere = csv.writer(o, delimiter='\t')
    for row in citire:
        row[11] = int(row[11]) / (10 ** 7) #transforming lat/long from integer to float
        row[12] = int(row[12]) / (10 ** 7)
        if row[2] in (ErrOpt):
            if row[0] in (AreaOpt):
                scriere.writerow(row)
                
