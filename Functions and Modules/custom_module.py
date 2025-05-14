def greetings(name):
    print(f"Hello, {name}!")
    print("Hello " + name)

print(__name__)
#print("I am inside custom_module")

if __name__ == "__main__":
    # This block will only execute if the script is run directly
    print("This script is being run directly")
   