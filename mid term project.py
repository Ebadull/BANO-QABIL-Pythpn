
def guess_number():
    # Step 2: Generate random number
    random_number = random.randint(1, 100)
    
    while True:
        # Step 3: Get user input
        guess = input("Guess a number between 1 and 100: ")
        
        # Step 4: Convert input to integer
        guess = int(guess)
        
        # Step 5: Compare numbers
        if guess < random_number:
            print("Too low! Guess higher.")
        elif guess > random_number:
            print("Too high! Guess lower.")
        else:
            print("Congratulations! You guessed the number!")
            break  # Exit the loop if the guess is correct

# Step 7: Call the function to start the game
guess_number()