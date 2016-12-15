file = open('list.txt','w')

for x in range(10):
    file.write(str(x + 1) + ". " + input("What do you want to add to the list? ") +  '\n')
    
file.close()