from datetime import date, datetime

def calculate_age(birthdate_str):
    """
    Calculate age from birthdate string (format: YYYY-MM-DD)
    """
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    except ValueError:
        return None

if __name__ == "__main__":
    birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
    age = calculate_age(birthdate_input)
    if age is not None:
        print(f"You are {age} years old.")
    else:
        print("Invalid date format. Please use YYYY-MM-DD.")

if birthdate_input < age:
    print("Its not future")