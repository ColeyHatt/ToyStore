toys = open('toys.txt')
#opens the text
directory = {}
#creates a dictionary, named directory
for line in toys:
  #checks the lines in the text document
    key, value = line.rstrip("\n").split(',')
    #converts said lines into key & values while removing , and \n
    directory[key] = value
    #adds the keys and values to previously said directory