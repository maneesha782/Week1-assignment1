from datetime import datetime

name = input("Enter your name: ")

print("Hello", name)

while True:

    print("\n1. Study Tip")
    print("2. Motivation Quote")
    print("3. Date and Time")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        result = "Practice coding daily."
        print(result)

    elif choice == "2":
        result = "Never give up."
        print(result)

    elif choice == "3":
        result = str(datetime.now())
        print(result)

    elif choice == "4":
        print("Goodbye")
        break

    else:
        result = "Invalid choice"
        print(result)

    with open("output.txt", "a") as file:
        file.write(result + "\n")