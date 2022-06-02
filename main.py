import pandas as pd

# read students's grades 

df = pd.read_csv('grades.csv')

# Welcome screen & menu option

print("\t \t Wellcome \n\n")
print("\tMenu of options\n")
print("1.Show Data \n")
print("2.Count Students \n")
print("3.Compute final score \n")
print("4.Show grades \n")
print("5.Column statistics \n")
print("6.Show students of grade A \n")
print("7.Search By name \n")
print("8.Exit \n")

# handling options 

def choose():

    ch = int(input("Enter option number then press enter\n"))
    if(ch==1):
        show_data()
    elif(ch==2):
        count_stud()
    elif(ch==3):
        calc_Fscore()
    elif(ch==4):
        show_grades()
    elif(ch==5):
        stats()
    elif(ch==6):
        grade_A()
    elif(ch==7):
        search()
    elif(ch==8):
        exit()
    else:
        print("please Enter integer number 1:8\n")
        choose()

#   showing data function

def show_data():
    print(df)
    print("\n\n")
    choose()

#   count students (first colmn)

def count_stud():
    ndf=pd.DataFrame(df.count(0))
    nofstd = ndf.iat[0,0]
    print(f"there are {nofstd} students\n\n")
    choose()

#   calc final score adding midterm & class work grades in a new colmn

def calc_Fscore():
    finalscoredf = df.assign(final_score=lambda x:x.midterm_grade + x.classwork_grade)
    print(finalscoredf)
    choose()

#   detect grades depends on final score

def show_grades():
    grades =[]
    finalscoredf = df.assign(final_score=lambda x:x.midterm_grade + x.classwork_grade)
    final_scores = finalscoredf['final_score'].tolist()
    for i in range(len(final_scores)):
        if int(final_scores[i]) >= 90:
            grades.append("A")
        elif 90>int(final_scores[i]) & int(final_scores[i])>=75:
            grades.append("B")
        elif 75>int(final_scores[i]) & int(final_scores[i])>=60:
            grades.append("C")
        elif 60>int(final_scores[i]) & int(final_scores[i])>=50:
            grades.append("D")
        elif 50>int(final_scores[i]):
            grades.append("F")
    gradedf= finalscoredf.assign(grade=grades)
    print(gradedf)
    choose()

#   calc statistics using descibe func ==> average , min , max , standard dev , median (50%) ,count
#   var ==> variance

def stats():
    finalscoredf = df.assign(final_score=lambda x:x.midterm_grade + x.classwork_grade)
    finalscoreonlydf= finalscoredf.loc[:,'final_score']
    print("\n\n statistics")
    print(finalscoreonlydf.describe())
    variance = finalscoreonlydf.var()
    print(f"\n\n variance = {variance} \n\n\n")
    choose()

#   filtering dataframe final score > 89 ==> (grade A)

def grade_A():
    grades =[]
    finalscoredf = df.assign(final_score=lambda x:x.midterm_grade + x.classwork_grade)
    final_scores = finalscoredf['final_score'].tolist()
    for i in range(len(final_scores)):
        if int(final_scores[i]) >= 90:
            grades.append("A")
        elif 90>int(final_scores[i]) & int(final_scores[i])>=75:
            grades.append("B")
        elif 75>int(final_scores[i]) & int(final_scores[i])>=60:
            grades.append("C")
        elif 60>int(final_scores[i]) & int(final_scores[i])>=50:
            grades.append("D")
        elif 50>int(final_scores[i]):
            grades.append("F")
        
    
    gradedf= finalscoredf.assign(grade=grades)
    print(gradedf[gradedf['final_score']>89])
    choose()

#   filtering dataframe names contains data entered

def search():
    studname = input("\n\nEnter student name then press enter \n\n").strip().lower()
    grades =[]
    finalscoredf = df.assign(final_score=lambda x:x.midterm_grade + x.classwork_grade)
    final_scores = finalscoredf['final_score'].tolist()
    for i in range(len(final_scores)):
        if int(final_scores[i]) >= 90:
            grades.append("A")
        elif 90>int(final_scores[i]) & int(final_scores[i])>=75:
            grades.append("B")
        elif 75>int(final_scores[i]) & int(final_scores[i])>=60:
            grades.append("C")
        elif 60>int(final_scores[i]) & int(final_scores[i])>=50:
            grades.append("D")
        elif 50>int(final_scores[i]):
            grades.append("F")
    
    gradedf= finalscoredf.assign(grade=grades)
    print(gradedf[gradedf['name'].str.contains(studname)])
    choose()    

#   say good bye and exit program

def exit():
    print("good-bye")
    quit()

#   calling choose function 

choose()