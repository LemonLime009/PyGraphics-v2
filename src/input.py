import sys

def main():
    print("Listening for input. Press Ctrl+C to exit.")
    
    try:
        while True:
            user_input = input()
            
            # Check for specific keys
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            elif user_input.lower() == "hello":
                print("Hello there!")
            else:
                print("Unknown command:", user_input)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
