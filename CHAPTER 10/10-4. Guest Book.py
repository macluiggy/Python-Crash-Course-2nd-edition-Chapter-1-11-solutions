filename = 'guest_book.txt'

n = 1
print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"Visit number {n}: {name}\n")
        print(f"Hi {name}, you've been added to the guest book.")
        n += 1