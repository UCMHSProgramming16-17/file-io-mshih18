# import requests and csv module
import requests
import csv

# open the csv file and set up csvwriter
csvfile = open('typefrequency.csv','w')
csvwriter = csv.writer(csvfile, delimiter = ',')


# make endpoint for api
endpoint = "http://pokeapi.co/api/v2/type/"

# make a new url for each type
for x in range(1,19):
    typenum = str(x)
    url = endpoint + typenum + "/"
    
    # send request
    r = requests.get(url)

    # assign type name and amount of pokemon with that type to variabes
    type = r.json()
    typename = (type['name'])
    amount = str((len(type['pokemon'])))
    
    # write rows containing the type name and the amount of pokemon
    csvwriter.writerow([typename, amount])
    
    # updates user on progress of program
    print("Finished gathering " + typename + "-type pokemon")
    
# close csvfile
csvfile.close()

# print message once program is finished
print("Job's done!")