# student_dict = {'student1':[45,70,80],
#                 'student2':[60,78,87],
#                 'student3':[30,34,56],
#                 'student4':[89,98,92],
#                 'student5':[45,60,70]}

student_dict={}

for i in range(1,6):
    marks=[]
    name=input(f"Enter the student{i} name: ")
    for j in range(1,4):
        score=int(input(f"Enter the student marks for subject {j}: "))
        marks.append(score)
    student_dict[name] = marks
def calc_avg(marks):
    return sum(marks)/len(marks)

def get_grade(avg):
    if avg>=90:
        return 'A'
    elif avg>=75:
        return 'B'
    elif avg>=60:
        return 'C'
    else:
        return 'F'
    
top_scorer_name = ""
top_scorer_marks = -1

for name,marks in student_dict.items():
    avg = calc_avg(marks)
    grade = get_grade(avg)

    if avg>top_scorer_marks:
        top_scorer_marks =avg
        top_scorer_name = name
    print(f"{name} | {avg:.2f} | {grade}")

print(f"Top scorer: {top_scorer_name} with an average score of {top_scorer_marks:.2f}")