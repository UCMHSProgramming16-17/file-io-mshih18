# open a new file named 'list.txt'
file = open('list.txt','w')

# loop ten times
for x in range(10):
    
    # get user input, write it to file, create new line
    file.write(str(x + 1) + ". " + input("What do you want to add to the list? ") +  '\n')
  
# close the file 
file.close()