# Nested Lists - Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade. Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    
    # Creat an empty list to store the students information
    students = []
    
    # inputing information here first, given to me. 
    for _ in range(int(input())):
        name = input()
        score = float(input())

        # Add the student information to the list 
        students.append([name, score])

    # Sort the list by score, using sort() and lamda functions
    students.sort(key=lambda x: x[1]) # x[1] sorts students by scores in ascending order by default because nature of sort()

    # Get the second lowest score an store in a var
    # This uses list comprehension ex: new_list = [expression for item in iterable]
    second_lowest = sorted(set([student[1] for student in students]))[1]
    # sorted() has strings sorted alphabetically and numbers sorted numerically. 
    # set() creates a set object {} that stores the floats values of each student. 

    # Print the names of students with the second lowest score 
    for student in sorted([student[0] for student in students if student[1] == second_lowest]):
    # sorted() again sorts students names alphabetically, called with student[0], has a conditional at the end of the list in an if statement. if statement is checking if the student in the iterable's score is equal to the value of the second_lowest score. 
        print(student)
        

# Finding the percentage - The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # retrieve the marks from the dict and store in a var
    marks = student_marks[query_name]
    
    # calculate the average of the student we're quering for and store in var
    average = sum(marks) / len(marks)    
    
    # prints the average marks with two decimal places. 
    print("{:.2f}".format(average))
    # the '{:.2f}' is a format specifier that tell python to format the number as a float with 2 decimal places.