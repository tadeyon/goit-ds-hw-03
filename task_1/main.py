from commands import COMMANDS

def main():
    print("Welcome to Cat Database Management System!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        if not user_input:
            continue
        if user_input in ["exit", "quit"]:
            print("Exiting... Goodbye!")
            break

        parts = user_input.split()
        name, args = parts[0], parts[1:]

        command = COMMANDS.get(name)
        
        if command:
            print(command(args))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()