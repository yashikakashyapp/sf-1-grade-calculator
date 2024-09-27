# inputs
labs= int(input("Enter the number of labs completed"))
quiz = int(input("Enter the number of quizzes completed"))
a_one = float(input("Enter the grade for Assignment 1"))
a_two = float(input("Enter the grade for Assignment 2"))
a_three = float(input("Enter the grade for ussignment 3"))
a_four = float(input("Enter the grade for Assignment 4"))
mt_one = float(input("Enter the grade for Midterm 1"))
mt_two = float(input("Enter the grade for Midterm 2"))
final = float(input("Enter grade for Final Exam:"))
exam_prep = float(input("Enter grade for Midterms and Final Preparation:"))
#functions
def labs_done(labs_completed: int) -> float:
    if labs_completed < 6:
        return ((labs/6)*20)
    elif labs_completed >= 6:
        return 20
def quiz_done(quiz_completed: int) -> float:
    if quiz_completed < 6:
        return ((labs/6)*15)
    elif quiz_completed >= 6:
        return 15
#calculations
final_grade = labs_done(labs) + quiz_done(quiz) + (a_one*0.04) + (a_two*0.04) + (a_three*0.04) + (a_four*0.04)) + ((mt_one*0.125) + (mt_two*0.125)) + (final*0.18) + (exam_prep*0.06)
#output
print("Your grade is : ", round(final_grade, 2))

