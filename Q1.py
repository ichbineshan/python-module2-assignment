#Create a function to read csv file and convert to python data structure (dict, list, set)
# first_name, last_name,roll
# John,Ken,11
# Ronny,Baggs,12
# Sam,Shone,13

import csv

f=open("data.csv")
csvreader= csv.reader(f)
header = next(csvreader)

dicts=[]
matrix=[]
sets=[]

matrix.append(header)    #initialising using header
sets.append(set(header))

for line in csvreader:
    d=dict()
    d[header[0]]=line[0]
    d[header[1]]=line[1]
    d[header[2]]=line[2]
    dicts.append(d)
    
    matrix.append(line)  
      
    sets.append(set(line))
    
print(dicts,"\n")    
print(matrix,"\n")    
print(sets,"\n")    
     
    