"""
Mini Student Grading System (Expert Refactor)

- Input 5 subject marks
- Compute average
- Assign grade (A, B, C, D, F)
"""

def get_valid_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def main():
    print("Input 5 subject marks")

    total_marks = 0

    for i in range(5):
        total_marks += get_valid_score(f"Subject {i+1} score: ")

    average = total_marks / 5
    grade = calculate_grade(average)

    print(f"\nAverage: {average:.2f}")
    print(f"Final Grade: {grade}")

if __name__ == "__main__":
    main()