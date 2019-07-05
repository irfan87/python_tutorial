greeter_prompt = "If you tell us who you are, we can personalize the messages you see"
greeter_prompt += f"\nPlease enter your name: "

name = input(greeter_prompt)

age = "Please tell me your age: "
age = input(age)
age = int(age)

print(f"\nAssalamualaikum {name.title()}.")

if age > 40:
    print(f"You are {age} and an adult")
else:
    print(f"You are {age} and still a young child")
