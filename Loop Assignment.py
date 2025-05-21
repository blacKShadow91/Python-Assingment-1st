            # Loop Question Solutions:


            #Ans to the Q.No-05


# for loop

for i in range(1, 6):
    print(str(i) * i)



# while loop
    i = 1
while i <= 5:
    print(str(i) * i)
    i += 1





                  #Ans to the Q.No-06
 #Fibonacci Sequence using for loop:                 
        
n = int(input("Enter the number of terms (N): "))

# First two terms
a, b = 0, 1

print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")  # Print current term
    a, b = b, a + b    # Update terms (next term = sum of previous two)


                    #Ans to the Q.No-07
#Password Check with 3 Attempts
correct_password = "Secure123"  # Predefined password
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Wrong password! {remaining_attempts} attempts left.")
else:  # Runs if loop completes without breaking (all attempts failed)
    print("Account locked! Too many failed attempts.")


                    #Ans to the Q.No-08
#Guess the Number Game (while loop): 


import random

secret_number = random.randint(1, 10)  # Random number between 1-10
attempts = 0

print("Guess the number between 1 and 10!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


                    #Ans to the Q.No-04

num = input("Enter an integer: ")
sum_digits = sum(int(digit) for digit in num if digit.isdigit())
print(f"Sum of digits: {sum_digits}")

            #Ans to the Q.No-03

num = int(input("Enter an integer: "))
reversed_num = 0
temp = abs(num)  # Handle negative numbers

while temp > 0:
    digit = temp % 10  # Extract the last digit
    reversed_num = reversed_num * 10 + digit  # Build the reversed number
    temp = temp // 10  # Remove the last digit

# Restore the sign if the original number was negative
if num < 0:
    reversed_num = -reversed_num

print(f"Reversed number: {reversed_num}")


                        #Ans to the Q.No-02

number = input("Enter a number: ")
num_length = len(number)
sum_of_powers = 0

for digit in number:
    sum_of_powers += int(digit) ** num_length

if sum_of_powers == int(number):
    print(f"{number} is an Armstrong number!")
else:
    print(f"{number} is not an Armstrong number.")



                #Ans to the Q.No-01


for num in range(1, 101):
    if num % 15 == 0:  # Check for multiples of both 3 and 5 first
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)



