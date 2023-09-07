import click
from login import login
from create_account import create_account



if __name__ == "__main__":
    while True:
        user_choice = click.prompt("Choose an option:\n1. Create Account\n2. Login\n3. Quit")

        if user_choice == "1":
            create_account()
        elif user_choice == "2":
            login()
        elif user_choice == "3":
            break
        else:
            click.echo("Invalid choice. Please select a valid option.")
