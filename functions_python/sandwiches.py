def make_sandwich(*items):
    print("\nToday, I am gonna make a sandwich for my breakfast")

    for item in items:
        print(f"...adding {item.title()} into my lovely sandwich")

    print("Nice!!")

    return items

make_sandwich('tuna', 'chicken')
make_sandwich('roast beef')
make_sandwich('makarel', 'eggs', 'salad')