import click
from Database import session  # Make sure the import path is correct
from models import Customer, Accounts, Transactions
from methods import deposit,withdraw,check_balance


@click.group()
def cli():
    pass

@cli.command()
def login():
    """Log in to an existing bank account."""
    phone_number = click.prompt("Enter your phone number")

    customer = session.query(Customer).filter_by(phone_number=phone_number).first()
    if not customer:
        click.echo("Account not found.")
    else:
        click.echo(f"Welcome, {customer.name}!")

        while True:
            choice = click.prompt(
                "Choose an option:\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Quit"
            )

            if choice == "1":
                amount = click.prompt("Enter the deposit amount")
                deposit(customer, amount)
            elif choice == "2":
                amount = click.prompt("Enter the withdrawal amount")
                withdraw(customer, amount)
            elif choice == "3":
                check_balance(customer)
            elif choice == "4":
                break
            else:
                click.echo("Invalid choice. Please select a valid option.")