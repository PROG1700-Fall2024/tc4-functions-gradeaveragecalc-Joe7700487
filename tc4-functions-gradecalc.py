############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Joseph Petrash



# OUTPUT -------------------------------------------------------------

# start up message
def intro():
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")    

# display the grade to the user taking the course name and grade as input
def outputGrade(courses):
    grade = 1
    name = 0
    print("Course   | Grade")
    print("________________")
    for courseNum in range(len(courses[grade])):
        # variables for readability
        courseName = courses[name][courseNum]
        courseGrade = courses[grade][courseNum]

        # output values
        print("{0} | {1:.1f}".format(courseName, courseGrade))

# display gpa to user taking gpa as input
def outputGPA(gpa):
    print("GPA: {0:.1f}".format(gpa)) 

# PROCESS ------------------------------------------------------------

# convert letter grades to numeric grades taking the letter as input
def convertLetter(letterGrade):
     # Determine base numeric value of the grade
    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
        numericGrade = 0.0
    else:
        #If an invalid entry is made
        print("You entered an invalid letter grade.")
    return numericGrade

# add the modifier to the grade taking the modifier, letter grade, and numeric grade as input
def addModifier(modifier, letterGrade, numericGrade):
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3
    return numericGrade

# calculate the average in a list taking the list as input
def getAverage(grades):
    sum = 0
    # sum all items in list
    for grade in grades:
        sum = grade + sum 
    # divide the sum by the length of the list
    avg = sum / len(grades)
    return avg

# combination of above functions to calculate the final numeric grade for the respective course in a single function
def getNumericGrade(course):
    # init variables
    numericGrade = 0.0
    # get letter grade from user
    letterGrade = input("Please enter a letter grade for {0} : ".format(course)).upper()
    # get modifier from user
    modifier = input("Please enter a modifier (+, - or nothing) : ")
    # conver the letter grade to numeric
    numericGrade = convertLetter(letterGrade)
    # add the modifier to the numeric letter grade
    numericGrade = addModifier(modifier, letterGrade, numericGrade)
    return numericGrade

# INPUT ---------------------------------------------------------------------
def getLetterGrade():
    pass

def getModifier():
    pass


# main() FUNCTION
def gradePointCalculator():
    # variables to make navigating the courses list more intuitive
    courseCode = 0
    grade = 1

    # Intro
    intro()

    # define table for courses and their grades     courses[courseCode] =  list of course names
    #                                               courses[grade]      = list of course grades
    courses = [["PROG1700", "NETW1700", "OSYS1200", "WEBD1000", "COMM1700", "DBAS1007"],
               [0,           0,          0,          0,          0,          0        ]]
    
    # for every course in the list ask the user what grade they got for it and convert it to a number
    for course in courses[courseCode]:
        #get the index of the current course
        index = courses[courseCode].index(course)
        # get letter to numeric grade from user
        numericGrade = getNumericGrade(course)
        # set the corresponding course grade equal to the numeric grade
        courses[grade][index] = numericGrade
        
    # output what the numeric grade was for each corrosponding course
    outputGrade(courses)

    # calculate and output the average of all the numeric grades
    outputGPA(getAverage(courses[grade]))    

    
#PROGRAM EXECUTION STARTS HERE
gradePointCalculator()