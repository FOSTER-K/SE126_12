#Week 4: Intro to Lists

#Lists can hold multiple points of data and store them to "Memory" to be used later on in our program

#below is hand-populated list (not from file)
#list1 holds a series of names

list1= ["Sam", "Mary", "Bill", "Adam", "Betty"]

#print full list - looks like print(rec) in data import demo
 
print(list1)
#List: store multiple data values (of the same type) to RAM 
print() #for spacing in console

#print the list each data point at a time
#0 --> First Index


print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

print()

num_records = len(list1) #len() is a Lenght Function
#len() returns the lenght of the list/item you pass it

print("\nNum Records in LIST1: ", num_records)
print() #SPACE FOR CONSOLE
print() #SPACE FOR CONSOLE
#the length of a list is always +1 more than the highest index 
    #(position in the list! starts at 0)

#A better way to print (and Process) a full list with contents is using the .. FOR LOOP

#FOT LOOPS WERE MADE FOR LISTS 
print("Pricing from a For Loop!\n")

for index in range(0, num_records):
    #the loop starts at index 0 ( [0] ) and it will for num_records # of time (includes 0)
    #IE te loop will run num_records number of times, or for each position held by a list item 

    print("INDEX#", index, "\t" , list1[index])

#three new lists, now different types of data
list2 = ["Sam", "18", "32000"]
list3 = ["Mary", "21", "34000"]
list4 = ["Tom", "24", "38000"]
#lists above look like a RECORD as opposed to a Filed when considering a text file

#Record ---> multiple data values, all different kinds
#Filed ---> multiple data values. all some kind

#to store a data file's record (which are read as lists) into actual lists (values stored to RAM)

#Step1: Create Empty Lists
#each Field Should have its own list
name = [] #empty list called 'name'
age = []   #empty list called 'age'
salary = [] #empty list called 'salary'
#the above lists are EMPTY -- they have no values stored in them 

#Step2: ADD ELEMENS TO THE LIST (POPULATING THE LISTS)
name.append(list2[0]) #adds index0 of list 2 to 'na mame'
name.append(list3[0])
name.append(list4[0])

print()
print("List 'name' contents: ", name)
print("name[1]: ", name[1])

for index in range(0, 3):
    print("INDEX: ", index, "\t", name[index])

print("Part 1 of demo complete .... \n\n")

#PART 2 --------- File Import Review / Appending Data From Files to LIST ----------------------------)

print("-----------------------------------------------------------------------")
print("\n\n")

#BEFORE STARTING: CHECK THE TEXT/CSV FILE!

#Step 1: import csv library

import csv 

#Step 2: initialize num_records so it can count the records
num_records = 0

#Step 3: Create empty lists to populate with text file data 
#MAKE SURE THIS HAPPENS BEFORE YOU CONNECT TO THE FILE

name =[]
age = []
salary = []
#NOTE: there is one list for each field in the file

#STEP 4: connect to data file
with open("C:/Users/008006057/OneDrive - New England Institute of Technology/SE 126.02/Week 4/example-1.csv") as csvfile:


    #STEP 5: ALLOW DATA TO BE "READ"
    FILE = csv.reader(csvfile)

    #STEP 6: process data in a for loop
    for rec in FILE:

    #STEP 7: INCRREMENT (+1) NUM_RECORDS
        num_records += 1 #num records = num_records + 1

    #STEP 8: append (add values from each other field of the record to their correspeonding lists

    name.append(rec[0])
    age.append(int(rec[1]))
    salary.append(float(rec[2]))

print("Finished processing file. \n\n")
    #rec[1] and rec[2] have been CAST as they arer appended for easier numeric processing

    #rec[#] represents the FIELD of DATA, rec is one full record of data

for index in range(0, num_records):

    print("Index: ", index, "\t", name[index], "\t", age[index], "\t $", salary[index])

print("Finished processing lists for: printing. \n\n")

#process the lists to find average salary
sal_total = 0

for index in range(0, num_records):
    sal_total += salary[index] #adds each value of salary list to 

avg_sal = sal_total / num_records
print("Avg SALARY in List ${:.2f}")

