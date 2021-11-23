#Program to figure out the students who doesn't fill the feedback form

#importing libraries
import os
import csv
import openpyxl

#storing the path of required files in variable inorder to use later
course_registered_by_all_students = os.path.join(os.getcwd(), "course_registered_by_all_students.csv")              
course_feedback_submitted_by_students = os.path.join(os.getcwd(), "course_feedback_submitted_by_students.csv")
studentinfo = os.path.join(os.getcwd(), "studentinfo.csv")
course_master = os.path.join(os.getcwd(), "course_master_dont_open_in_excel.csv")

#initializing global variables
global LTS_dic, sud_info, subject_dic, roll_dic
LTS_dic, sud_info, subject_dic, roll_dic = {}, {}, {}, {}

#function to create list of non-zero bits by passing LTS from .csv file
def feedback(LTS):
    feedback = []
    LTS = LTS.split("-")
    for i in range(0, 3):
        if LTS[i] != "0":
            feedback.append(str(i + 1))
    return feedback

#function to create dictionary
def dics():
    
    #loop will help in storing non-zero bits of LTS
    for ind, line in enumerate(csv.reader(open(course_master))):
        if ind > 0:
            LTS_dic[line[0]] = feedback(line[2])

    #loop will help in storing register amd schedule sem
    for ind, line in enumerate(csv.reader(open(course_registered_by_all_students))):
        if ind > 0:
            if line[0] not in subject_dic:
                subject_dic[line[0]] = {}
            if line[3] not in subject_dic[line[0]]:
                subject_dic[line[0]][line[3]] = []
            subject_dic[line[0]][line[3]] = [line[1], line[2]]

    #loop will help in storing roll no, email, aemail, contact no
    for ind, line in enumerate(csv.reader(open(studentinfo))):
        if ind > 0:
            sud_info[line[1]] = [line[0], line[8], line[9], line[10]]

    #loop will check whether feedback is submitted by student or not
    for ind, line in enumerate(csv.reader(open(course_feedback_submitted_by_students))):
        if ind > 0:
            if line[3] not in roll_dic:
                roll_dic[line[3]] = {}
            if line[4] not in roll_dic[line[3]]:
                roll_dic[line[3]][line[4]] = []
            fb_subs = roll_dic[line[3]][line[4]]
            if ([subject_dic[line[3]][line[4]][1], line[5]] not in fb_subs and line[5] in LTS_dic[line[4]] and line[3] in subject_dic):
                fb_subs.append([subject_dic[line[3]][line[4]][1], line[5]])
    return

#function to generate list of students who doesn't submitted feedback 
def feedback_not_submitted():
    course_feedback_remaining = os.path.join(os.getcwd(), "course_feedback_remaining.xlsx")
    
    if os.path.exists(course_feedback_remaining):
        os.remove(course_feedback_remaining)

    wb = openpyxl.Workbook()
    header = ["rollno","reg_sem","schedule_sem","subno","name","email","aemail","contact"]
    sheet = wb.active
    sheet.append(header)

    for roll in subject_dic:
        for sub in subject_dic[roll]:
            if roll not in roll_dic:
                if roll in sud_info:
                    name = sud_info[roll][0]
                    email = sud_info[roll][1]
                    aemail = sud_info[roll][2]
                    contact = sud_info[roll][3]
                else:
                    name = "NA_IN_STUDENT_INFO"
                    aemail = "NA_IN_STUDENT_INFO"
                    contact = "NA_IN_STUDENT_INFO"
                    email = "NA_IN_STUDENT_INFO"

                if len(LTS_dic[sub]) > 0:
                    sheet.append([roll,subject_dic[roll][sub][0],subject_dic[roll][sub][1],sub,name,email,aemail,contact])

            elif sub not in roll_dic[roll].keys():
                if roll in sud_info:
                    name = sud_info[roll][0]
                    email = sud_info[roll][1]
                    aemail = sud_info[roll][2]
                    contact = sud_info[roll][3]
                else:
                    name = "NA_IN_STUDENT_INFO"
                    aemail = "NA_IN_STUDENT_INFO"
                    contact = "NA_IN_STUDENT_INFO"
                    email = "NA_IN_STUDENT_INFO"
                    
                if sub in LTS_dic and len(LTS_dic[sub]) > 0:
                    sheet.append([roll,subject_dic[roll][sub][0],subject_dic[roll][sub][1],sub,name,email,aemail,contact])
            else:
                k = []
                for i in roll_dic[roll][sub]:
                    for j in i:
                        if j not in k:
                            k.append(i[1])
                if roll in sud_info:
                    name = sud_info[roll][0]
                    email = sud_info[roll][1]
                    aemail = sud_info[roll][2]
                    contact = sud_info[roll][3]
                else:
                    name = "NA_IN_STUDENT_INFO"
                    aemail = "NA_IN_STUDENT_INFO"
                    contact = "NA_IN_STUDENT_INFO"
                    email = "NA_IN_STUDENT_INFO"
                    
                x, y = sorted(k), sorted(LTS_dic[sub])
                length = len(LTS_dic[sub])
                if length > 0 and y != x:
                    sheet.append([roll,subject_dic[roll][sub][0],subject_dic[roll][sub][1],sub,name,email,aemail,contact])
    wb.save(course_feedback_remaining)

#driver function
dics()
feedback_not_submitted()
