import os                                                                               #importing os module


#general function which help in generating required files
def general(index):                                         
    file = open("F:/5th sem/Python/1901CB06_2021/tut03/regtable_old.csv","r")               #open function to open the file in read mode
    data = file.readlines()                                                             #readling all the lines of file and storing it into variable "data"                                                           
    data.sort()                                                                         #sort() function to arrange all data in ascending order
    L = []                                                                              #intialization of list L
    if index == 0:                                                                      #condition to generate required files with the help of index
        dir = "output_individual_roll/"
    else:
        dir = "output_by_subject/"
    for m in range(len(data)):                                                          #loop from 0 to length of data
        L.append(data[m].split(","))                                                    #storing data in list form with the help of split function splited by ","
        no = str(L[m][index])                                                           #storing values from data, list into string form
        route = "F:/5th sem/Python/1901CB06_2021/tut03/" + dir + no + ".csv"                #path in which file is going to be store
        if os.path.isfile(route) == False:                                              #cecking whether that file is  alread present or not
            no = open(route,"a")                                                        
            no.write("rollno,register_sem,subno,sub_type\n")                            #appending required values in file

        no = open(route,"a")
        result = str(L[m][0]) + "," + str(L[m][1]) +"," + str(L[m][3]) + "," + str(L[m][8])
        no.write(result)                                                                #appending required values in file
        no.close()                                                                      #close function to close the file
    file.close()
    return 


#function to generate file by subject
def output_by_subject():                
    general(3)                                                                          #passing arguement "3"
    return


#function to generate file by individual rollnos
def output_individual_roll():
    general(0)                                                                          #passing arguement "0"
    return


#driver's code
output_by_subject()
output_individual_roll()
