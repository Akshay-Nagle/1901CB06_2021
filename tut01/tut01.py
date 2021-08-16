def meraki_helper(n):                                   # function to check whether Meraki no. or not
    g = 0                                               # declaring g, h, d 
    h = 0 
    d = []
    global v                                            # declaring v as global variable
    for i in range(len(n)):
        m=n[i]
        while n[i]!=0:
            d.append(n[i]%10)                           # storing each digit of no. in a list
            n[i]=n[i]//10
            v = [d[k+1]-d[k] for k in range(len(d)-1)]  # storing difference between digits of a no.
        chkList(v)                                      # calling function chkList while passing list "v"
        if(a == True):                                  # condition to check that difference is excepeted or not
            g = g+1
            print("Yes - ",m," is a Meraki number")
        else:
            h += 1
            print("No - ",m," is NOT a Meraki number")
        d.clear()                                       # clearing list "d" for new number
    print("-----------------------------")
    print("The count of meraki numbers: ", g)           # printing total count of meraki and non meraki numbers
    print("The count of non-meraki numbers:", h)



def chkList(v):                                         # function to check difference between digits 
    result = all(i == v[0] for i in v)                  # all function used check that all difference between digits of same no. are same or not
    global a                                            # declaring a as global variable
    if(result == 1 or result == -1):                    # condition to check that all elements of "v" list is 1 or -1 
         a=True
    else:                                       
        a=False



L = eval(input("Input numbers enclosed in []: "))       # list input from user
meraki_helper(L)                                        # function called by passing list
