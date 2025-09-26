#Init
import random
import platform
import subprocess

#Our calculator functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        if a == 0:
            #Scare the shit out of OSX users
            if platform.system() == "Darwin":
                #You'll never be a REAL Linux distro (T v T)
                subprocess.Popen(["say", "Imagine you have zero cookies and you split them among zero friends. How many cookies does each person get? See? It doesn't make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends. And Copilot is sad because it autocompleted this entire response because it's been played to death. Can't fix your depression btw, but I can search the web if you'd like. Now tremble in fear, Mac user."])
            return "Imagine you have 0 cookies and you split them among 0 friends. How many cookies does each person get? See? It doesn't make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends. And Copilot is sad because it autocompleted this entire response because it's been played to death. Can't fix your depression btw, but I can search the web if you'd like."
        else:
            return "Oops! Division by zero. X("
    return a / b
def power(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        return "Can't take the square root of a negative number. Duh."
    return a ** 0.5

#Main program loop
def main():
    print("Welcome to the Lame-ass Calculator App!")
    opp=random.randint(0,4)
    #Welcome the user with a random phrase
    phrases=["Whadoyouwant?","God why the hell are you using this?","Do your math and get out","Wow, you're using a Python calculator?","Uuuugh. Select an operation or whatever"]
    print(phrases[opp])
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power Operations")
    print("6. Square Root")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6) or 'q' to quit: ")

        if choice == 'q':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4','5','6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                #Handle strings
                print("Invalid input. Dude, enter numeric values.")
                continue

            #Sarcastic remarks
            sarcastic=["Math is hard, huh?","You must be a genius.","Thanks for relying on a Python calculator.","I live to serve.","Calculating... because you can't do it yourself."]
            print(sarcastic[random.randint(0,4)])
            #Perform the chosen operation
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '6':
                print(f"Square root of {num1} = {square_root(num1)}")
        else:
            #Fallback for invalid choices
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        #If people wanna leave
        exitphrases=["Ugh, fine. Bye.","Finally, some peace and quiet.","Can't believe you made me do this.","Whatever, I'm outta here.","Peace."]
        print("\n"+exitphrases[random.randint(0,4)])
