import os
import string
import random
import platform
from rich.console import Console
from rich.panel import Panel

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

console = Console()

logo = Panel(""" [bold green]
\t</>    Developer: mapher      </>
\t</>    Github: hacksking07        </>
\t</>    Insta: @hacksking07        </>
""", width=50, style="bold hot_pink2", title="PASSGEN")

def get_strength():
    while True:
        try:
            length = int(input("Enter password length (default: 8): "))
            if length <= 0:
                print("Password length must be greater than 0.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_complexity():
    print("[+] Select requirement options")
    print("""
    1. Numbers Only
    2. Letters only
    3. Numbers + letters
    4. Numbers + letters + special chars
    """)
    while True:
        try:
            opt = int(input("Select option: "))
            if 1 <= opt <= 4:
                return opt
            else:
                print("Invalid option. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_password(length, complexity):
    characters = ""
    if complexity in (1, 3, 4):
        characters += string.digits
    if complexity in (2, 3, 4):
        characters += string.ascii_letters
    if complexity == 4:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    clear_screen()
    console.print(logo)

    length = get_strength()
    complexity = get_complexity()

    password = generate_password(length, complexity)
    print("Your Password: \n\t"+password)

if __name__ == "__main__":
    main()
