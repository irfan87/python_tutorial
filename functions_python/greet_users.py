def greet_users(names):
    for name in names:
        msg = f"\nHello, {name.title()}!"
        print(msg)

usernames = ['ali', 'hassan', 'john', 'jane', 'doe']
greet_users(usernames)