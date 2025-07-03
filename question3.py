def calculate_average(scores):
    return sum(scores)/len(scores)

def get_letter_grade(average):
    if (average>=90):
        return "A"
    elif (average>=80):
        return "B"
    elif (average>=70):
        return "C"
    elif (average>=60):
        return "D"
    return "F"

while(True):
    scores = []
    numscores = int(input("How many test scores do you want to enter? "))
    for x in range(numscores):
        scores.append(int(input(f"Enter score {x+1}: ")))
    
    print("\n=== GRADE REPORT ===")
    print(f"Test Scores: {scores}")
    print(f"Average Score: {calculate_average(scores)}")
    print(f"Letter Grade: {get_letter_grade(calculate_average(scores))}\n")
    