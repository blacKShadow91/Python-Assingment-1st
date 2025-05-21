                # Conditional Statement Question Solutions: 
           
    #Ans to the Q.No-02
def classify_age():
    """
    Takes a person's age as input and prints out their age category.
    """
    while True:
        try:
            age = int(input("Enter the person's age: "))
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number for age.")

    if 0 <= age <= 1:
        print("They are an infant.")
    elif 2 <= age <= 3:
        print("They are a toddler.")
    elif 4 <= age <= 12:
        print("They are a child.")
    elif 13 <= age <= 19:
        print("They are a teenager.")
    else:  # age >= 20
        print("They are an adult.")

if __name__ == "__main__":
    classify_age()

