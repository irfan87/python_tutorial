magicians = ['david copperfield', 'david blane', 'alice', 'john', 'sam']

insert_new_magicians = magicians.insert(-1, 'carolina')

magicians.sort()

print("\nAlacadabra!!!\n")

for magician in magicians:
    print(f"{magician.title()}, that was an amazing trick!!!")
    print(f"I cannot wait to see your next trick, {magician.title()}!\n")

print("Thank you, everyone! That was a great trick!\n")

magicians_size = len(magicians)

print(f"The size of magicians: {magicians_size}")
