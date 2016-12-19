# import csv
import csv
import math

# open csvfile
csvfile = open('csvtriangle.csv', 'w')

# create csvwriter
csvwriter = csv.writer(csvfile, delimiter = ',')

# write to file

for a in range(1,101):
    for b in range(a,101):
        hypotenuse = sqrt((a**2) + (b**2))
        csvwriter.writerow([a,b, hypotenuse])

# close file
csvfile.close()
