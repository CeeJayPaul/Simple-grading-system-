def get_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score < 70:
        return "B"
    elif 50 <= score < 60:
        return "C"
    elif 45 <= score < 50:
        return "D"
    elif 40 <= score < 45:
        return "E"
    else:
        return "F"

def main():
    try:
        score = int(input("Enter your score (0-100): "))
        if 0 <= score <= 100:
            grade = get_grade(score)
            print(f"Your grade is: {grade}")
        else:
            print("Score must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
