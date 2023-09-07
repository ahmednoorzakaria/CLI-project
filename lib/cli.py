import click
from Database import session  # Make sure the import path is correct
from models import Customer, Accounts, Transactions

@click.group()
def cli():
    pass

@cli.command()
def create_account():
    # ...
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")

    existing_customer = session.query(Customer).filter_by(phone_number=phone_number).first()

    if existing_customer:
        print("Customer with this phone number already exists.")
    else:
        # Create a new customer and an associated account with a zero balance
        new_customer = Customer(name=name, phone_number=phone_number)
        new_account = Accounts(balance=0)
        new_customer.accounts.append(new_account)
        
        # Add the new customer and account to the database
        session.add(new_customer)
        session.commit()
        
        print(f"Customer '{name}' has been created with an account and a zero balance.")

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

def deposit(customer, amount):
    account = customer.accounts[0]  # Assuming one account per customer
    account.balance += int(amount)
    transactions = Transactions(account=account, amount=int(amount), type="deposit")
    session.add(transactions)
    session.commit()
    click.echo(f"Deposited ${amount} successfully. New balance: ${account.balance}")

def withdraw(customer, amount):
    account = customer.accounts[0]  # Assuming one account per customer

    if account.balance < int(amount):
        click.echo("Insufficient funds.")
    else:
        account.balance -= int(amount)
        transactions = Transactions(account=account, amount=int(amount), type="withdraw")
        session.add(transactions)
        session.commit()
        click.echo(f"Withdrew ${amount} successfully. New balance: ${account.balance}")

def check_balance(customer):
    account = customer.accounts[0]  # Assuming one account per customer
    click.echo(f"Your account balance: ${account.balance}")

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
