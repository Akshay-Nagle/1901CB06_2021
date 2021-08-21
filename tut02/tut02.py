from random import *                                                              #importing package random to generate random nos.

def get_memory_score(M):                                                          #function to return score value when we pass list
  score = 0                                                                       #intialization of variables
  k = []
  for i in range(len(M)):                                                         #loop to traverse each element of passed list
    if (M[i] not in k):                                                           #condition to compare elements in both list
      k.append(M[i])                            
      k=k[-5:]                                                                    #limiting the size of list
    else:                                                                         #when above condition is false; this part will execute
      score += 1                                                                  #increase the value of score by 1
  return score                                                                    #returning value of score where it is called



#n = int(input("Enter total no of times game will play: "))                       #commenting - may be use to accept user input later
#input_nums=[]
input_nums = [3, 4, 1, 6, 3, 3, 9, 0, 0, 0]                                       #intialization of variables
L = []

#commenting - useful when user provide input
"""for i in range(n):                                                             
    input_nums.append(randint(0,9))
    input_nums = input_nums[-10:]
print(*input_nums)"""

for i in range(len(input_nums)):                                                  #loop to traverse each element of list
    a = isinstance(input_nums[i], int)                                            #isinstance() used to check whether element is int type or not
    if (a == False):                                                              #condition when element is not int type
      L.append(input_nums[i])                                                     #storing in list
if (len(L)>0):                                                                    #to check whether elements are present or not
    print("Please enter a valid input list. Invalid inputs dected: ",L)

res = get_memory_score(input_nums)                                                #passing list to function in order to calculate score and receiving return value
print("Score:",res)                                                               #displaying score

