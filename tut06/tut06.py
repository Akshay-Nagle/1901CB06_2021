import os                                                                                                           
import shutil                                                                                                                   #importing modules
import re


wrongDir = os.path.join(os.getcwd(), "srt")                                                                                     #joining path with the given string and writing here to ease up our work
rightDir = os.path.join(os.getcwd(), "rightDir_srt")

#function to rename Breaking Bad .mp4+.srt files
def BreakingBad():
    Root = os.path.join(wrongDir, "Breaking Bad")                                                                               #joining path with given string to differentiate between folders
    Dir = os.path.join(rightDir, "Breaking Bad")

    if os.path.exists(Dir):                                                                                                     #condition to check whether required folder is already created
        shutil.rmtree(Dir)                                                                                                      #if created then delete the entire folder
    os.mkdir(Dir)                                                                                                               #make new folder with the same name

    for filename in os.listdir(Root):                                                                                           #loop to traverse through all the files in require folder
        init = re.split(" 7..*dr", filename)                                                                                    #spliting as per requirement
        info = re.split(" se?", init[0])                                                                                        #spliting as per requirement

        SEPs = list(map(int, re.split("e", info[1])))                                                                           #spliting the episode and season number, then mapping them andd storing
        result = (info[0]+ " Season "+ str(SEPs[0]).zfill(s_pad)+ " Episode "+ str(SEPs[1]).zfill(e_pad)+ init[1])              #desired result
        
        wrongpath = os.path.join(Root, filename)                                                                                #original files name
        rightpath = os.path.join(Dir, result)                                                                                   #required files name
        shutil.copy(wrongpath, rightpath)                                                                                       #shutil.copy(source,destination) used to copy source content to destination 
    return

#function to rename Game of Thrones .mp4+.srt files
def GOT():
    Root = os.path.join(wrongDir, "Game of Thrones")                                                                             #joining path with given string to differentiate between folders
    Dir = os.path.join(rightDir, "Game of Thrones")

    if os.path.exists(Dir):                                                                                                      #condition to check whether required folder is already created
        shutil.rmtree(Dir)                                                                                                       #if created then delete the entire folder
    os.mkdir(Dir)                                                                                                                #make new folder with the same name

    for filename in os.listdir(Root):                                                                                            #loop to traverse through all the files in require folder
        init = re.split("\..*en", filename)                                                                                      #spliting as per requirement
        info = re.split(" \- ", init[0])                                                                                         #spliting as per requirement

        SEPs = list(map(int, re.split("x", info[1])))                                                                            #spliting the episode and season number, then mapping them andd storing
        result = ("Game of Thrones"+ " - Season "+ str(int(SEPs[0])).zfill(s_pad)+ " Episode "+ str(int(SEPs[1])).zfill(e_pad)+ info[2]+ init[1])   #desired result

        wrongpath = os.path.join(Root, filename)                                                                                 #original files name
        rightpath = os.path.join(Dir, result)                                                                                    #required files name
        shutil.copy(wrongpath, rightpath)                                                                                        #shutil.copy(source,destination) used to copy source content to destination 
    return

#function to rename Lucifer .mp4+.srt files
def Lucifer():
    Root = os.path.join(wrongDir, "Lucifer")                                                                                     #joining path with given string to differentiate between folders
    Dir = os.path.join(rightDir, "Lucifer")

    if os.path.exists(Dir):                                                                                                      #condition to check whether required folder is already created
        shutil.rmtree(Dir)                                                                                                       #if created then delete the entire folder
    os.mkdir(Dir)                                                                                                                #make new folder with the same nametraverse

    for filename in os.listdir(Root):                                                                                            #loop to traverse through all the files in require folder
        init = re.split("\..*en", filename)                                                                                      #spliting as per requirement
        details = re.split(" \- ", init[0])                                                                                      #spliting as per requirement

        SEPs = list(map(int, re.split("x", details[1])))                                                                         #spliting the episode and season number, then mapping them andd storing
        result = (details[0]+ " - Season "+ str(int(SEPs[0])).zfill(s_pad)+ " Episode "+ str(int(SEPs[1])).zfill(e_pad)+ " - "+ details[2]+ init[1])    #desired result
        
        wrongFilePath = os.path.join(Root, filename)                                                                             #original files name
        rightpath = os.path.join(Dir, result)                                                                                    #required files name
        shutil.copy(wrongFilePath, rightpath)                                                                                    #required files name#shutil.copy(source,destination) used to copy source content to destination 
    return

#function to display and call all other function to display required result
def subtitles_renamer():
    print("--------------------------------")                                                                                    #displaying list to get user input
    print("1. Breaking Bad")
    print("2. Game of Thrones")
    print("3. Lucifer")
    
    webseries_no = int(input("Choose TV-Series which subtitles needed to be renamed: "))                                         #user providing a number from above list
    global s_pad, e_pad                                                                                                          #declaring variables global inorder to remove access it outside the function
    s_pad = int(input("Enter the Season Number Padding: "))                                                                      #user provide season number padding
    e_pad = int(input("Enter the Episode Number Padding: "))                                                                     #user provide episode number padding

    if not os.path.exists(rightDir):                                                                                             #condition to check whether directory is present or not
        os.mkdir(rightDir)                                                                                                       #if not present, create required directory

    if webseries_no == 1:                                                                                                        #conditions to call desired function
        BreakingBad()
    elif webseries_no == 2:
        GOT()
    elif webseries_no == 3:
        Lucifer()
    else:
        print("Please enter number from given list only")                                                                        #print default case if no input no. from the above list


#Driver's Code
subtitles_renamer()

# for 1st input values - 1  1   1
# for 2nd input values - 2  2   2
# for 3rd input values - 3  3   3  