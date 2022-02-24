#user data
programme = input("Programme :")
semester = input("Semester :")
uic = int(input("Unique Identification Code :"))
name = input("Student Name :")
fname = input("Father Name : ")
mname = input("Mother Name :")
term = input("Term :")
roll_no = input("Exam Roll No :")
dob = input("Date of Birth :")
gender = input("Gender :")

#marks input
while True:
    t1 = int(input("Enter DSP marks :"))
    if t1 > 0 and t1 < 80:
        break
    else:
        print("Wrong Input : Enter marks between 0-80:")
    
while True:
    t2 = int(input("Enter AIC marks :"))
    if t2 > 0 and t2 < 80:
        break
    else:
        print("Wrong Input :Enter marks between 0-80:")
while True:
    t3 = int(input("Enter CS marks :" ))
    if t3 > 0 and t3 < 80:
        break
    else:
        print("Wrong Input : Enter marks between 0-80:")
while True:
    t4 = int(input("Enter AML marks :" ))
    if t4 > 0 and t4 < 80:
        break
    else:
        print("Wrong Input : Enter marks between 0-80:")
while True:
    t5 = int(input("Enter FOM marks :" ))
    if t5 > 0 and t5 < 80:
        break
    else:
        print("Wrong Input : Enter marks between 0-80:")
print("---------------------------------------------------------------------------------------------")

while True:
    a1 = int(input("Enter DSP assignment marks :" ))
    if a1 > 0 and a1 < 20:
        break
    else:
        print("Wrong Input : Enter marks between 0-20:")

while True:
    a2 = int(input("Enter LDSP assignment marks :" ))
    if a2 > 0 and a2 < 20:
        break
    else:
        print("Wrong Input : Enter marks between 0-20:")
while True:
    a3 = int(input("Enter AIC assignment marks :" ))
    if a2 > 0 and a3 < 20:
        break
    else:
        print("Wrong Input : Enter marks between 0-20:")
while True:
    a4 = int(input("Enter LAIC assignment marks :" ))
    if a4 > 0 and a4 < 20:
        break
    else:
        print("Wrong Input : Enter marks between 0-20:")
while True:
    a5 = int(input("Enter CS assignment marks :" ))
    if a5 > 0 and a5 < 20:
        break
    else:
        print("Wrong Input : Enter marks between 0-20:")
while True:
    a6 = int(input("Enter AML assignment marks :" ))
    if a6 > 0 and a6 < 20:
        break
    else:
        print("Wrong Input : Enter marks between 0-20:")
while True:
    a7 = int(input("Enter LAML assignment marks :" ))
    if a7 > 0 and a7 < 20:
        break
    else:
        print("Wrong Input : Enter marks between 0-20:")
while True:
    a8 = int(input("Enter FOM assignment marks :" ))
    if a8 > 0 and a8 < 20:
        break
    else:
        print("Wrong Input : Enter marks between 0-20:")
print("-----------------------------------------------------------------------------------------------")

while True:
    p1 = int(input("Enter PDSP practical marks :" ))
    if p1 > 0 and p1 < 80:
        break
    else:
        print("Wrong Input : Enter marks between 0-80:")
while True:
    p2 = int(input("Enter PAIC practical marks :" ))
    if p2 > 0 and p2 < 80:
        break
    else:
        print("Wrong Input : Enter marks between 0-80:")
while True:
    p3 = int(input("Enter PAML practical marks :" ))
    if p3 > 0 and p3 < 80:
        break
    else:
        print("Wrong Input : Enter marks between 0-80:")
print("------------------------------------------------------------------------------")

#indiviual grading
tot_dsp = t1 + a1 
if tot_dsp >= 81 and tot_dsp <= 100:
        g_dsp = "A"
elif tot_dsp >= 61 and tot_dsp <= 80:
        g_dsp = "B"
elif tot_dsp >= 41 and tot_dsp <= 60:
        g_dsp = "C"
elif tot_dsp >= 61 and tot_dsp <= 40:
        g_dsp = "D"
else:
        g_dsp = "F"
print (tot_dsp)
print (g_dsp)

tot_aic = t2 + a3 
if tot_aic >= 81 and tot_aic <= 100:
        g_aic = "A"
elif tot_aic >= 61 and tot_aic <= 80:
        g_aic = "B"
elif tot_aic >= 41 and tot_aic <= 60:
        g_aic = "C"
elif tot_aic >= 61 and tot_aic <= 40:
        g_aic = "D"
else:
        g_aic = "F"
print (tot_aic)
print (g_aic)

tot_cs = t3 + a5 
if tot_cs >= 81 and tot_cs <= 100:
        g_cs = "A"
elif tot_cs >= 61 and tot_cs <= 80:
        g_cs = "B"
elif tot_cs >= 41 and tot_cs <= 60:
        g_cs = "C"
elif tot_cs >= 61 and tot_cs <= 40:
        g_cs = "D"
else:
        g_cs= "F"
print (tot_cs)
print (g_cs)

tot_aml = t4 + a6
if tot_aml >= 81 and tot_aml <= 100:
        g_aml = "A"
elif tot_aml >= 61 and tot_aml <= 80:
        g_aml = "B"
elif tot_aml >= 41 and tot_aml <= 60:
        g_aml = "C"
elif tot_aml >= 61 and tot_aml <= 40:
        g_aml = "D"
else:
        g_aml = "F"
print (tot_aml)
print (g_aml)                  

tot_fom = t5 + a8 
if tot_fom >= 81 and tot_fom <= 100:
        g_fom = "A"
elif tot_fom >= 61 and tot_fom <= 80:
        g_fom = "B"
elif tot_fom >= 41 and tot_fom <= 60:
        g_fom = "C"
elif tot_fom >= 61 and tot_fom <= 40:
        g_fom = "D"
else:
        g_fom = "F"
print (tot_fom)
print (g_fom)

tot_ldsp = p1 + a2 
if tot_ldsp >= 81 and tot_ldsp <= 100:
        g_ldsp = "A"
elif tot_ldsp >= 61 and tot_ldsp <= 80:
        g_ldsp = "B"
elif tot_ldsp >= 41 and tot_ldsp <= 60:
        g_ldsp = "C"
elif tot_ldsp >= 61 and tot_ldsp <= 40:
        g_ldsp = "D"
else:
        g_ldsp = "F"
print (tot_ldsp)
print (g_ldsp)

tot_laic = p2 + a4 
if tot_laic >= 81 and tot_laic <= 100:
        g_laic = "A"
elif tot_laic >= 61 and tot_laic <= 80:
        g_laic = "B"
elif tot_laic >= 41 and tot_laic <= 60:
        g_laic = "C"
elif tot_laic >= 61 and tot_laic <= 40:
        g_laic = "D"
else:
        g_laic = "F"
print (tot_laic)
print (g_laic)

tot_laml = p2 + a7 
if tot_laml >= 81 and tot_laml <= 100:
        g_laml = "A"
elif tot_laml >= 61 and tot_laml <= 80:
        g_laml = "B"
elif tot_laml >= 41 and tot_laml <= 60:
        g_laml = "C"
elif tot_laml >= 61 and tot_laml <= 40:
        g_laml = "D"
else:
        g_laml = "F"
print (tot_laml)
print (g_laml)

#total
T_marks = t1+t2+t3+t4+t5 
A_marks = a1+a2+a3+a4+a5+a6+a7+a8
P_marks = p1+p2+p3

print(T_marks)
print(A_marks)
print(P_marks)

Obtained_marks = T_marks + A_marks + P_marks
print(Obtained_marks)
#percentage
max_marks = 800
percentage = float(Obtained_marks/max_marks)*100
print(percentage)

if percentage < 45:
    Result = "FAIL"
else:
    Result = "PASS"
#cgpa
cgpa = (percentage/9.5)
print(cgpa)

#show marksheet
print("=================================================================================================")
print("                             Nagar Yuwak Shikshan Sanstha's                                      ")
print("                        YESHWANTRAO CHAVAN COLLEGE OF ENGINEERING                                ")
print("                  Hingana Road, Wanadongri, Nagpur - 441110(INDIA), www.ycce.edu                           ")
print("                       (An Autonomous Institution under UGC Act 1956)                            ")
print('No.YCCE/ODD 2020-2021/5751',end="                                              ")                                                                 
print("Sr.No. : 169645"                                                                       )
print("                                   SEMESTER GRADE REPORT                           ")
print(f'Programme : {programme}')
print(f'Semester : {semester}')
print(f'Unique Identification Code : {uic}')
print(f'Student Name : {name}')
print(f'Father Name : {fname}',end="                                                     ")
print(f'Term : {term}')
print(f'Mother Name : {mname} ',end="                                                    ")
print(f'Exam Roll No : {roll_no}')
print(f'Date of Birth : {dob}',end="                                                ")
print(f'Gender : {gender}')
print("-------------------------------------------------------------------------------------------------")
print('Current Semester Courses')
print("---------------------------------------------------------------------------------------------------------------------------------------------------")

print("  |Sr.|              SUBJECT              |             MAX_MARKS              |          OBTAINED_MARKS            |  TOTAL_MARKS|GRADE    |")
print("  |No |               NAME                |THEORY_MARKS|ASSIGN_MARKS|PRAC_MARKS|THEORY_MARKS|ASSIGN_MARKS|PRAC_MARKS|    OBTAINED |(REMARKS)|")
print(f" | 1.|Digital Signal Processing          |80          |20          |-         |{t1}        |{a1}        |-         |{tot_dsp}    |{g_dsp}  |")
print(f" | 2.|Lab:Digital Signal Processing      |-           |20          |80        |-           |{a2}        |{p1}      |{tot_ldsp}   |{g_ldsp} |")
print(f" | 3.|Analog & integrated circuits       |80          |20          |-         |{t2}        |{a3}        |-         |{tot_aic}    |{g_aic}  |")
print(f" | 4.|Lab:Analog & integrated circuits   |-           |20          |80        |-           |{a4}        |{p2}      |{tot_laic}   |{g_laic} |")
print(f" | 5.|Control System                     |80          |20          |-         |{t3}        |{a5}        |-         |{tot_cs}     |{g_cs}   |")
print(f" | 6.|Applied Machine Learning           |80          |20          |-         |{t4}        |{a6}        |-         |{tot_aml}    |{g_aml}  |")
print(f" | 7.|Lab:Applied Machine Learning       |-           |20          |80        |-           |{a7}        |{p3}      |{tot_laml}   |{g_laml} |")
print(f" | 8.|Fundamentals of Management         |80          |20          |-         |{t5}        |{a8}        |-         |{tot_fom}    |{g_fom}  |")
print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print(f" |       TOTAL MARKS                     |    400     |  160       | 240      |{T_marks}   | {A_marks}  |{P_marks} |{Obtained_marks}|{Result} |")                           



print("                             |-------------------------------------------|")
print("                             |         Current Semester Record           |")
print("                             |------------------------------------------ |")
print("                             |Obtained Marks  |Percentage    |CGPA       |")
print(f"                            |{Obtained_marks}             |{percentage}         |{cgpa}    |")
print("                             |-------------------------------------------|")
print(f"                                               {Result}")



