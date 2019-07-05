prompt_message = "Welcome to the roller coaster land"
print(prompt_message)

height = input("Please enter your height: ")
height = int(height)

if height >= 48:
    print(f"\nYou are tall enough to ride")
else:
    print(f"\nYou are too short to ride")